import { createBrowserRouter } from "react-router-dom";
import GameSettings from "./GameSettings";
import GameBoard from "./GameBoard";

export const router = createBrowserRouter([
  { path: "/", element: <GameSettings /> },
  { path: "/game", element: <GameBoard /> },
]);
