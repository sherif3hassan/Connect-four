import React, { useState, useCallback } from "react";
import { difficultyConverter, getDifficulty } from "./utils";
import { useNavigate } from "react-router-dom";
import { useGameContext } from "./GameContext";
import "./css/gameSettings.css";
function GameSettings() {
  // const [algorithmType, setAlgorithmType] = useState("minimax"); // default algorithm type is minimax
  // const [difficultyLevel, setDifficultyLevel] = useState("easy"); // default difficulty level is easy

  const {
    algorithmType,
    setAlgorithmType,
    difficultyLevel,
    setDifficultyLevel,
  } = useGameContext();

  const navigate = useNavigate();

  // recreate playNextMove only when algorithmType changes
  // useCallback(playNextMove, [algorithmType])

  async function handleAlgorithmTypeChange(event) {
    const response = await fetch(`http://localhost:8000/switchalgorithm/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        algorithm: event.target.value,
      }),
    });
    const data = await response.json();
    setAlgorithmType(data.algorithm);
  }

  async function handleDifficultyLevelChange(event) {
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
      <h2 className='header'>Game Settings</h2>
      <div className='algoSelect'>
        <label>Algorithm Type:</label>
        <select
          className='algorithmTypeSelect'
          value={algorithmType}
          onChange={handleAlgorithmTypeChange}
        >
          <option value='minimax'>Minimax</option>
          <option value='alpha-beta'>Alpha-Beta Pruning</option>
        </select>
      </div>
      <div className='difficultySelect'>
        <label>Difficulty Level:</label>
        <select
          className='difficultyLevelSelect'
          value={difficultyLevel}
          onChange={handleDifficultyLevelChange}
        >
          <option value='easy'>Easy</option>
          <option value='medium'>Medium</option>
          <option value='hard'>Hard</option>
        </select>
      </div>
      <button className='startBtn' onClick={handleStartGameClick}>
        Start Game
      </button>
    </div>
  );
}

export default GameSettings;
