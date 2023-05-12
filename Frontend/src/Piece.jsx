import { useEffect } from "react";
import "./css/pieceStyle.css";
import { useRef } from "react";

function mapXPosToPercent(x) {
    switch (x) {
        case 0:
            return 1.9;
        case 1:
            return 15.9;
        case 2:
            return 29.9;
        case 3:
            return 43.9;
        case 4:
            return 57.9;
        case 5:
            return 71.9;
        case 6:
            return 86;
        default:
            throw new Error("Invalid x position");
    }
}

function mapYPosToPercent(y) {
    switch (y) {
        case 0:
            return 0.5;
        case 1:
            return 17.5;
        case 2:
            return 33.5;
        case 3:
            return 50.5;
        case 4:
            return 67.5;
        case 5:
            return 83.5;
        default:
            throw new Error("Invalid y position");
    }
}

export default function Piece({ x, y, turn }) {
    // Delay the rendering of the piece until the x and y coordinates are set
    const pieceRef = useRef(null);
    useEffect(() => {
        pieceRef.current.style.left = `${mapXPosToPercent(x)}%`;
        pieceRef.current.style.top = `${mapYPosToPercent(y)}%`;
    }, [x, y]);

    return <div ref={pieceRef} className={`piece piece-${turn}`}></div>;
}
