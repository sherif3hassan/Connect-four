import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.jsx'
import GameSettings from './GameSettings';

const rootElement = document.getElementById('root');

const reactStartingPoint = ReactDOM.createRoot(rootElement);

reactStartingPoint.render(<GameSettings />);
