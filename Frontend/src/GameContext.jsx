import { createContext, useContext } from "react";
import { useState } from "react";
import { getTurnPlayer } from "./utils";

const GameContext = createContext();

export function useGameContext() {
    return useContext(GameContext);
}

export function GameContextProvider({ children }) {
    const [algorithmType, setAlgorithmType] = useState("minimax"); // default algorithm type is minimax
    const [difficultyLevel, setDifficultyLevel] = useState("easy"); // default difficulty level is easy
    const [board, setBoard] = useState([]);
    const [winner, setWinner] = useState(null); // winner is either "1" or "2" or null
    const [loading, setLoading] = useState(false); // loading is either true or false

    async function playNextMove() {
        setLoading(true);
        const response = await fetch(`http://localhost:8000/next/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        });

        const data = await response.json();
        setLoading(false);
        return data ? data.board : null;
    }

    async function getWinner() {
        const response = await fetch(`http://localhost:8000/winner/`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });
        const data = await response.json();

        setWinner(getTurnPlayer(data.winner));
        return data.winner;
    }

    async function playHumanMove(column) {
        const response = await fetch(`http://localhost:8000/play/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                column: column,
            }),
        });

        const data = await response.json();
        setLoading(false);
        return data ? data.board : null;
    }

    async function playRandomMove() {
        setLoading(true);
        const response = await fetch(`http://localhost:8000/randomplay/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        });

        const data = await response.json();
        setLoading(false);
        return data ? data.board : null;
    }

    const value = {
        loading,
        playNextMove,
        playHumanMove,
        playRandomMove,
        winner,
        getWinner,
        algorithmType,
        setAlgorithmType,
        difficultyLevel,
        setDifficultyLevel,
        board,
        setBoard,
    };

    return <GameContext.Provider value={value}>{children}</GameContext.Provider>;
}
