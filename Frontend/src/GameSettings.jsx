import React, { useState } from "react";

function GameSettings(props) {
  const [algorithmType, setAlgorithmType] = useState("minimax"); // default algorithm type is minimax
  const [difficultyLevel, setDifficultyLevel] = useState("easy"); // default difficulty level is easy

  function handleAlgorithmTypeChange(event) {
    const response=await fetch(`http://localhost:8000/algorithm/`,{
    setAlgorithmType(event.target.value);
  }

  async function handleDifficultyLevelChange(event) {
    
    const response=await fetch(`http://localhost:8000/difficulty/`,{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({difficulty: event.target.value}),
      
    } );
    const data=await response.json();
    setDifficultyLevel(data.difficulty);
  }

  function handleStartGameClick() {
    // handle this
  }

  return (
    <div>
      <h2>Game Settings</h2>
      <div>
        <label htmlFor='algorithmTypeSelect'>Algorithm Type:</label>
        <select
          id='algorithmTypeSelect'
          value={algorithmType}
          onChange={handleAlgorithmTypeChange}
        >
          <option value='minimax'>Minimax</option>
          <option value='alpha-beta'>Alpha-Beta Pruning</option>
        </select>
      </div>
      <div>
        <label htmlFor='difficultyLevelSelect'>Difficulty Level:</label>
        <select
          id='difficultyLevelSelect'
          value={difficultyLevel}
          onChange={handleDifficultyLevelChange}
        >
          <option value='easy'>Easy</option>
          <option value='medium'>Medium</option>
          <option value='hard'>Hard</option>
        </select>
      </div>
      <button onClick={handleStartGameClick}>Start Game</button>
    </div>
  );
}

export default GameSettings;
