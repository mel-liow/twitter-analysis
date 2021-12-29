import React from "react"
import { Chart, ArcElement } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

Chart.register(ArcElement);

export const SentimentChart = ({ data }) => {

  return (
    <div>
        <Doughnut 
            data={{
              labels:['Negative', 'Neutral', 'Positive'],
              datasets: [{
                label: 'Sentiment',
                data: data,
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)',
                  'rgb(255, 205, 86)'
                ],
                hoverOffset: 4
                
              }]
            }}
          />
    </div>
  )
}

