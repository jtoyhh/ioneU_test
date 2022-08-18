import React from 'react';
import Chart from 'chart.js/auto';
import { BarController, PieController } from 'chart.js';
import { Pie, Line } from 'react-chartjs-2';
import { Typography } from '@mui/material';
export default function Graph() {

  Chart.register(BarController, PieController);
  
  const data = {
    labels: [
      '중소기업 재직자 90%',
      '대기업 재직자 10%',
    ],

    datasets: [{
      label: 'My First Dataset',
      data: [90, 10],

      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 205, 86)'
      ],
    }]
  };

  const config = {
    type: 'pie',
    data: data,
  };

  return (
    <>
    <Typography variant="h5">
        전체 기업 종사자 수
      </Typography>
      <br />
    <div style={{ width: '15vw' }}>
      <Pie data={data} />
    </div>
    </>
  )
};
