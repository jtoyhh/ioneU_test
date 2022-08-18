import sqlite3
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
from pytrends.request import TrendReq
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'ioneu/index.html') 

# 2. views 함수 생성

# 메인페이지 - (1) 복지 해시태그 선택시 해당 회사 목록 보여주기
@api_view(['GET'])
def WelfareCompany(request, hashtag):
    # 회사 리스트 생성
    company = []

    # SQLite DB 연결
    conn = sqlite3.connect("../../Data/Data_Processing/Data/IONEJOB.db")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    # SQL 쿼리 실행
    cur.execute(f"""
    select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 주요사업, 산업1, 산업2, 성과보상, 열린문화, 건강한삶, 역량성장
    from Company
    where {hashtag} = 1;
    """)

    # 데이타 Fetch
    rows = cur.fetchall()
    for row in rows:
        company.append(row)
    
    # Connection 닫기
    conn.close()

    return Response(company)


# 메인페이지 - (2) 기업정책 탭 클릭시 금융 태그 관련 3개 정책 제공
@api_view(['GET'])
def FinancePolicy(request):
    # 기업 정책(금융) 리스트 생성
    finance_policy = []

    # SQLite DB 연결
    conn = sqlite3.connect("../../Data/Data_Processing/Data/IONEJOB.db")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    # SQL 쿼리 실행
    cur.execute(f"""
    select b.해시태그, a.pblancNm as 정책명
    from 기업정책 as a
    join Company as b
    on b.해시태그 = a.pldirSportRealmLclasCodeNm
    where b.해시태그 = '금융'
    group by a.pblancNm
    limit 3
    ;
    """)

    # 데이타 Fetch
    rows = cur.fetchall()
    for row in rows:
        finance_policy.append(row)
    
    # Connection 닫기
    conn.close()

    return Response(finance_policy)


# 메인페이지 - (2) 기업정책 내 해시태그(내수, 수출, 인력, 창업...) 별 기업정책 3개 제공 
@api_view(['GET'])
def CompanyPolicy(request, hashtag):
    # 기업정책(내수, 수출, 인력, 창업...) 리스트 생성
    policy = []

    # SQLite DB 연결
    conn = sqlite3.connect("../../Data/Data_Processing/Data/IONEJOB.db")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    # SQL 쿼리 실행
    cur.execute(f"""
    select b.해시태그, a.pblancNm as 정책명
    from 기업정책 as a
    join Company as b
    on b.해시태그 = a.pldirSportRealmLclasCodeNm
    where b.해시태그 = "{hashtag}"
    group by a.pblancNm
    limit 3
    ;
    """)

    # 데이타 Fetch
    rows = cur.fetchall()
    for row in rows:
        policy.append(row)
    
    # Connection 닫기
    conn.close()

    return Response(policy)


# 메인페이지 - (3) 청년정책 내 해시태그(서울) 별 기업정책 3개 제공 
@api_view(['GET'])
def SeoulPolicy(request):
    # 청년정책(서울) 리스트 생성
    policy = []

    # SQLite DB 연결
    conn = sqlite3.connect("../../Data/Data_Processing/Data/IONEJOB.db")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    # SQL 쿼리 실행
    cur.execute(f"""
    select polyBizSjnm, polyBizSecd
    from 청년정책_v3
    where polyBizSecd = '서울'
    limit 3
    ;
    """)

    # 데이타 Fetch
    rows = cur.fetchall()
    for row in rows:
        policy.append(row)
    
    # Connection 닫기
    conn.close()

    return Response(policy)



# 메인페이지 - (3) 청년정책 내 해시태그(서울, 대구, 부산, ...) 별 기업정책 3개 제공 
@api_view(['GET'])
def YouthPolicy(request, hashtag):
    # 청년정책(서울, 대구, 부산, ...) 리스트 생성
    policy = []

    # SQLite DB 연결
    conn = sqlite3.connect("../../Data/Data_Processing/Data/IONEJOB.db")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    # SQL 쿼리 실행
    cur.execute(f"""
    select polyBizSjnm, polyBizSecd, polyItcnCn
    from 청년정책_v3
    where polyBizSecd = '{hashtag}'
    ;
    """)

    # 데이타 Fetch
    rows = cur.fetchall()
    for row in rows:
        policy.append(row)
    
    # Connection 닫기
    conn.close()

    return Response(policy)


# 상세페이지 - 특정 기업 시각화 자료 제공
@api_view(['GET'])
def CompanyInfo(request, company):

    # 기업의 산업을 Company Table에서 산업1,2,3,4 로 받아와야함
    industries = []

    conn = sqlite3.connect("../../Data/Data_Processing/Data/IONEJOB.db")

    cur = conn.cursor()

    cur.execute(f"""
    select 산업1, 산업2, 산업3, 산업4
    from Company
    where 기업명 = '{company}'
    ;
    """)

    rows = cur.fetchall()
    for row in rows:
        industries.append(row)

    

    pytrends = TrendReq(hl='ko', tz=540)

    pytrends.build_payload(kw_list = [industries], cat=0, timeframe="today 5-y", geo="KR", gprop="")

    # GoogleTrends(RelatedQueries) 워드클라우드
    data_queries = pytrends.related_queries()
    data_queries = data_queries[industries]['top']
    for i in range(len(data_queries)):
        data_queries['query'][i] = data_queries['query'][i].replace(" ", "")
        freq = dict(zip(data_queries["query"], data_queries["value"]))
        wordcloud = WordCloud(font_path = "C:\ioneU\Data\Data_Processing\Fonts\NotoSansKR-Regular.otf", background_color="white")

        word = plt.figure(figsize=(15,10))
        word = plt.imshow(wordcloud.generate_from_frequencies(freq))
        word = plt.axis("off")
        word = plt.savefig('C:/Django/Data_Processing/Data/cloud_%s.png' % industries)

    # GoogleTrends(InterestOverTime) 산업 추이 그래프()
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'
    matplotlib.rcParams['axes.unicode_minus'] = False

    data = pytrends.interest_over_time()

    image = data.plot(title = '관심도[%s]' % industries)
    fig = image.get_figure()
    fig.savefig('C:/ioneU/Data/Data_Processing/Data/interest_%s.png' % industries)

    # NaverNews 테이블 제공



    return Response(policy)
