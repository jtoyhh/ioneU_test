import React, { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Link from "next/link";

import { useNavigate } from 'react-router-dom';

export default function SimplePaper() {

  const hashtags = ['역량성장', '열린문화',
  '건강한삶', '성과보상']

    const [tag, setTag] = useState('');
    // const navigate = useNavigate();

    const onClick = (hashtag : any) => {
      // console.log(hashtag)
      setTag(hashtag)
      // navigate(`list/${tag}`);
    } 

  
    // useEffect(()=> {
    //   axios
    //     .get(
    //       `http://127.0.0.1:8000/ioneu/main/wealfare/${'역량성장'}`, 
    //     )
    //     .then((response) => {
    //       console.log(response.data)
    //       // setTag(response.data)
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // }, [])


  return (
    <>
    <Typography variant="h5">
        맞춤기업 해시태그
      </Typography>
    <br />
      <Stack spacing={2} direction="row">
      {hashtags.map((hashtag) => (
        <Button
        onClick={() => onClick(hashtag)}
        key={hashtag}
        variant="outlined"
        sx={{
          ':hover': {
            bgcolor: 'primary.main', 
            color: 'white',
          },
        }}
        >
          <Link href={{ pathname: 'list', query: { id: hashtag } }}>
            <a style={{
            textDecoration : 'none',
          }}>
            #{hashtag}
            
            </a>
          </Link>
            {/* #{hashtag} */}

        </Button>

      )
      )}
     
    </Stack>
    </>
   
  );
}