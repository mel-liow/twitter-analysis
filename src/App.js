import React, { useState } from "react"
import ReactWordcloud from "react-wordcloud"

import "./App.css"

const App = () => {
  const [twitterHandle, setTwitterHandle] = useState("")
  const [words, setWords] = useState([])

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
        const words = data.map((word) => {
          return {
            text: word[0],
            value: word[1],
          }
        })
        setWords(words)
      })
  }

  return (
    <div className="app">
      <header className="header">
        <form className="form" onSubmit={handleSubmit}>
          <label className="label">Enter Twitter handle below</label>
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
      <div className="words">
        <ReactWordcloud words={words} />
      </div>
    </div>
  )
}

export default App
