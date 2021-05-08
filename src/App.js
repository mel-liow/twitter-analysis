import React, { useState } from "react"

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
        const words = JSON.parse(data)
        setWords(words)
      })
  }

  return (
    <div className="App">
      <header className="App-header">
        <div>{twitterHandle}</div>
        <form onSubmit={handleSubmit}>
          <label>
            Enter Twitter handle:
            <input
              type="text"
              name="twitter"
              value={twitterHandle}
              onChange={handleChange}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>
        <div className="words">
          {words.map((word) => (
            <div>{word}</div>
          ))}
        </div>
      </header>
    </div>
  )
}

export default App
