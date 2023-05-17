export function difficultyConverter(difficulty) {
    switch (difficulty) {
        case "easy":
            return 1;
        case "medium":
            return 3;
        case "hard":
            return 5;
        default:
            return 1;
    }
}

export function getDifficulty(difficulty) {
    switch (difficulty) {
        case 1:
            return "easy";
        case 3:
            return "medium";
        case 5:
            return "hard";
        default:
            return "easy";
    }
}

export function getTurnPlayer(turn) {
    if (turn === 1) {
        return "red";
    } else if (turn === 2) {
        return "blue";
    } else if (turn === 3) {
        return "No one";
    }
}
