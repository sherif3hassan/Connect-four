import "./css/boardStyle.css";
import Piece from "./Piece";
import { useEffect } from "react";
import { getTurnPlayer } from "./utils";
import { useGameContext } from "./GameContext";
import { useNavigate } from "react-router-dom";
import { useRef } from "react";

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
  const navigate = useNavigate();
  const { board, setBoard, playNextMove, playRandomMove, getWinner, winner } =
    useGameContext();

  async function handleReset() {
    const response = await fetch(`http://localhost:8000/reset/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    setBoard(data.board);
    nextMoveRef.current.disabled = false;
    winnerRef.current.style.visibility = "hidden";
  }

  useEffect(() => {
    handleReset();
    getBoard().then((board) => {
      if (board) {
        setBoard(board);
      }
    });
  }, []);

  const nextMoveRef = useRef(null);
  const winnerRef = useRef(null);

  function handleNextMove() {
    nextMoveRef.current.disabled = true;
    playNextMove().then((board) => {
      if (board) {
        setBoard(board);
        playRandomMove().then((board) => {
          if (board) {
            setBoard(board);
            if (winnerRef.current.style.visibility === "visible") {
              nextMoveRef.current.disabled = true;
            } else {
              nextMoveRef.current.disabled = false;
            }
          }
        });
      }
    });
  }

  function handleBack() {
    navigate("/");
  }

  const Pieces = [];
  if (board) {
    for (let i = 0; i < board.length; i++) {
      const row = board[i];
      for (let j = 0; j < row.length; j++) {
        const piece = row[j];
        const turn = getTurnPlayer(piece);
        if (piece !== 0) {
          Pieces.push(<Piece key={i * 7 + j} x={j} y={i} turn={turn} />);
        }
      }
    }
  }

  useEffect(() => {
    getWinner().then((winner) => {
      if (winner !== 0) {
        winnerRef.current.style.visibility = "visible";
        nextMoveRef.current.disabled = true;
        winnerRef.current.style.color =
          winner === 1 ? "red" : winner === 2 ? "blue" : "white";
      }
    });
  }, [board]);
  return (
    <>
      <div className='board-container'>
        <div className='winner' ref={winnerRef}>
          {winner} won!
        </div>
        <div className='piece-container'>
          <div className='board'></div>
          {Pieces}
        </div>
        <div className='button-container'>
          <button className='btn back-btn' onClick={handleBack}>
            Back
          </button>
          <button
            className='btn next-btn'
            ref={nextMoveRef}
            onClick={handleNextMove}
          >
            Next Move
          </button>
          <button className='btn reset-btn' onClick={handleReset}>
            Reset Board
          </button>
        </div>
      </div>
    </>
  );
}

export default GameBoard;
