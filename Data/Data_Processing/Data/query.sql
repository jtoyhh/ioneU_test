<<<<<<< HEAD
/*
해시태그(내수, 수출, 인력...) 기반 기업정책 및 기업명 제공
*/
select a.pblancNm as 정책명, replace(replace(replace(b.기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, b.해시태그
from 기업정책 as a
join Company as b
on b.정책 = a.pblancNm
;

/*
지역(polyBizSecd) 기반 청년정책 제공
*/
select polyBizSjnm, polyBizSecd, polyItcnCn, sporCn, rqutUrla
from 청년정책_v3
;

/*
해시태그(내수, 수출, 인력...) 기반 청년정책 제공
*/
select polyBizSjnm as 정책명, plcyTpNm as 해시태그
from 청년정책
order by 해시태그
;

/*
해시태그(내수, 수출, 인력...) 기반 기업명 제공
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 해시태그
from Company
;

/*
성과보상
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 성과보상, 해시태그
from Company
where 성과보상 = 1
;

/*
열린문화
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 열린문화, 해시태그
from Company
where 열린문화 = 1
;

/*
건강한삶
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 건강한삶, 해시태그
from Company
where 건강한삶 = 1
;

/*
역량성장
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 역량성장, 해시태그
from Company
where 역량성장 = 1
;
=======
/*
해시태그(내수, 수출, 인력...) 기반 기업정책 및 기업명 제공
*/
select a.pblancNm as 정책명, replace(replace(replace(b.기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, b.해시태그, b.산업1, b.산업2, b.산업3, b.산업4
from 기업정책 as a
join Company as b
on b.정책 = a.pblancNm
;

/*
지역(polyBizSecd) 기반 청년정책 제공
*/
select polyBizSjnm, polyBizSecd, polyItcnCn, sporCn, rqutUrla
from 청년정책_v3
;

/*
해시태그(내수, 수출, 인력...) 기반 청년정책 제공
*/
select polyBizSjnm as 정책명, plcyTpNm as 해시태그
from 청년정책
order by 해시태그
;

/*
해시태그(내수, 수출, 인력...) 기반 기업명 제공
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 해시태그
from Company
;

/*
성과보상
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 성과보상, 해시태그
from Company
where 성과보상 = 1
;

/*
열린문화
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 열린문화, 해시태그
from Company
where 열린문화 = 1
;

/*
건강한삶
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 건강한삶, 해시태그
from Company
where 건강한삶 = 1
;

/*
역량성장
*/
select replace(replace(replace(기업명, " ", ""), "(주)", ""), "주식회사", "") as 기업명, 역량성장, 해시태그
from Company
where 역량성장 = 1
;
>>>>>>> b35824865dc951377f731489377eb20dc3608b14
