import React from "react";
import ReactDOM from "react-dom/client";
import GameBoard from "./GameBoard";
// import App from './App.jsx'
import GameSettings from "./GameSettings";
import "./css/index.css";

const rootElement = document.getElementById("root");

const reactStartingPoint = ReactDOM.createRoot(rootElement);

reactStartingPoint.render(<GameBoard />);
