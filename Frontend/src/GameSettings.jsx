import React, { useState, useCallback } from "react";
import { difficultyConverter, getDifficulty } from "./utils";
import { useNavigate } from "react-router-dom";
function GameSettings() {
  const [algorithmType, setAlgorithmType] = useState("minimax"); // default algorithm type is minimax
  const [difficultyLevel, setDifficultyLevel] = useState("easy"); // default difficulty level is easy
  const navigate = useNavigate();
  

  // recreate playNextMove only when algorithmType changes
  // useCallback(playNextMove, [algorithmType])

  async function playNextMove() {
    const response = await fetch(`http://localhost:8000/next/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        flag: algorithmType !== "minimax",
      }),
    });

    const data = await response.json();
    return data.board;
  }

  function handleAlgorithmTypeChange(event) {
    setAlgorithmType(event.target.value);
  }

  async function handleDifficultyLevelChange(event) {
    setDifficultyLevel(event.target.value);
    const response = await fetch(`http://localhost:8000/difficulty/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        difficulty: difficultyConverter(event.target.value),
      }),
    });
    const data = await response.json();

    setDifficultyLevel(getDifficulty(data.difficulty));
  }

  function handleStartGameClick() {
    navigate("/game");
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
