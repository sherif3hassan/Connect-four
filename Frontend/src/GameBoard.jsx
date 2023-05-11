import React, { useState } from "react";
import "./css/boardStyle.css";
import Piece from "./Piece";
import { useEffect } from "react";
import { getTurnPlayer } from "./utils";

async function getBoard() {
  const response = await fetch(`http://localhost:8000/board/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data.board;
}

// <Piece key={x} x={x * 120 + 15} y={114} turn={} />

function GameBoard() {
  const [board, setBoard] = useState([]);
  useEffect(() => {
    getBoard().then((board) => {
      setBoard(board);
    });
  }, []);

  const Pieces = [];
  for (let i = 0; i < board.length; i++) {
    const row = board[i];
    for (let j = 0; j < row.length; j++) {
      const piece = row[j];
      const turn = getTurnPlayer(piece);
      if (piece !== 0) {
        Pieces.push(
          <Piece key={i * 7 + j} x={j * 120 + 15} y={i * 108} turn={turn} />
        );
      }
    }
  }
  return (
    <>
      <div className='board-container'>
        <div className='piece-container'>
          <div className='board'></div>

          {Pieces}
        </div>
      </div>
    </>
  );
}

export default GameBoard;
