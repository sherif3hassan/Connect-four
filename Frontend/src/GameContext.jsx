import { createContext, useContext } from "react";
import { useState } from "react";

const GameContext = createContext();

export function useGameContext() {
  return useContext(GameContext);
}

export function GameContextProvider({ children }) {
  const [algorithmType, setAlgorithmType] = useState("minimax"); // default algorithm type is minimax
  const [difficultyLevel, setDifficultyLevel] = useState("easy"); // default difficulty level is easy
  const [board, setBoard] = useState([]);

  async function playNextMove() {
    const response = await fetch(`http://localhost:8000/next/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    return data ? data.board : null;
  }

  const value = {
    playNextMove,
    algorithmType,
    setAlgorithmType,
    difficultyLevel,
    setDifficultyLevel,
    board,
    setBoard,
  };

  return <GameContext.Provider value={value}>{children}</GameContext.Provider>;
}
