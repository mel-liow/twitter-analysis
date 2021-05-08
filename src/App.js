import React, { useState, useEffect } from 'react';

import './App.css';

const  App = () => {

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log('here?', e.target)
		// return fetch('/post', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ data })
    // })
	}

  return (
    <div className="App">
      <header className="App-header">
			<form onSubmit={handleSubmit}>
				<label>
					Enter Twitter handle:
					<input type="text" name="name" />
				</label>
				<input type = "submit" value = "Submit" />
			</form>

      </header>
    </div>
  );
}

export default App;
