import React from "react"
import { Chart, ArcElement, Tooltip, Legend  } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

import './SentimentChart.css'

Chart.register(ArcElement, Tooltip, Legend );

export const SentimentChart = ({ data }) => {

    const chartData = {
        labels: ['Negative', 'Neutral', 'Positive'],
        datasets: [{
            label: 'ho',
            data: data, 
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
                ],
            hoverOffset: 4}],
    }

    const options = {
        responsive: true,
        maintainAspectRatio: true,
        legend: {
            display: true,
        },
        datalabels: {
            display: true,
            color: "black",
        },
    }

    return (
        <>
            Sentiment Analysis
            <div className='chart'>
                <Doughnut 
                    options={options}
                    data={chartData}
                />
            </div>
        </>
    )
}

