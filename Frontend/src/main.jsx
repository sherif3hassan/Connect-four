import React from "react";
import ReactDOM from "react-dom/client";
import "./css/index.css";
import { RouterProvider } from "react-router-dom";
import { router } from "./router";

const rootElement = document.getElementById("root");

const reactStartingPoint = ReactDOM.createRoot(rootElement);

reactStartingPoint.render(<RouterProvider router={router} />);
