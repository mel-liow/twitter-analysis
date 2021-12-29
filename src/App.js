import React, { useState } from "react"
import { Chart, ArcElement } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
import { WordCloud } from "./components";
import "./App.css"

Chart.register(ArcElement);

const App = () => {
  const [twitterHandle, setTwitterHandle] = useState("")
  const [words, setWords] = useState([])
  const [sentiment, setSentiment] = useState([])

  const handleChange = (e) => {
    const twitterHandle = e.target.value
    setTwitterHandle(twitterHandle)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    return fetch("/twitter", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ twitterHandle }),
    })
      .then((res) => res.json())
      .then((data) => {
        let {words, scores} = data

        const scores_array = [scores['neg'], scores['neu'], scores['neg']]
        const cloud_words = JSON.parse(words).map((word) => {
          return {
            text: word[0],
            value: word[1],
          }
        })

        setWords(cloud_words)
        setSentiment(scores_array)
      })
  }

  return (
    <div className="app">
      <header className="header">
        <form className="form" onSubmit={handleSubmit}>
          <label className="label">Enter Twitter handle below to generate a word cloud</label>
          <div>
            <input
              type="text"
              name="twitter"
              value={twitterHandle}
              onChange={handleChange}
            />
            <input type="submit" value="Submit" />
          </div>
        </form>
        <div className="twitterHandle">{twitterHandle}</div>
      </header>
      <div className="body">
        <div className="wordCloud">
          <WordCloud data={words}/>
        </div>
        <div className="wordSentiment">
          <Doughnut 
            data={{
              labels:['Negative', 'Neutral', 'Positive'],
              datasets: [{
                label: 'Sentiment',
                data: sentiment,
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
      </div>
    </div>
  )
}

export default App
