import React, { useState } from "react"

import "./App.css"

const App = () => {
  const [twitterHandle, setTwitterHandle] = useState("")

  const handleSubmit = (e) => {
    const twitterHandle = e.target.value
    setTwitterHandle(twitterHandle)
    e.preventDefault()

    return fetch("/twitter", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ data: twitterHandle }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data)
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
              onChange={handleSubmit}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </header>
    </div>
  )
}

export default App
