import React from "react";
import "./css/boardStyle.css";
import Piece from "./Piece";

function GameBoard() {
  return (
    <>
      <div className='board-container'>
        <div className='piece-container'>
          <div className='board'></div>

          {[0, 1, 2, 3, 4, 5, 6].map((x) => {
            return <Piece key={x} x={x * 120 + 15} y={114} />;
          })}
        </div>
      </div>
    </>
  );
}

export default GameBoard;
