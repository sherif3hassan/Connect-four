import React, { useEffect } from "react";
import "./css/pieceStyle.css";
import { useRef } from "react";

export default function Piece({ x, y, turn }) {
  // Delay the rendering of the piece until the x and y coordinates are set
  const pieceRef = useRef(null);
  useEffect(() => {
    pieceRef.current.style.left = `${x}px`;
    pieceRef.current.style.top = `${y}px`;
  }, [x, y]);

  return <div ref={pieceRef} className={`piece piece-${turn}`}></div>;
}
