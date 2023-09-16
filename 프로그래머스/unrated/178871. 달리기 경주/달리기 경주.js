function solution(players, callings) {
    const playerIndexes = new Map();
    for (let i = 0; i < players.length; i++) {
        playerIndexes.set(players[i], i);
    }

    const orderedPlayers = Array.from(players);

    for (const j of callings) {
        var position = playerIndexes.get(j);
        if (position > 0) {
            const swappedPlayer = orderedPlayers[position - 1];
            [orderedPlayers[position - 1], orderedPlayers[position]] =
                [orderedPlayers[position], orderedPlayers[position - 1]];
            
            playerIndexes.set(swappedPlayer, position);
            playerIndexes.set(j, position - 1);
        }
    }

    return orderedPlayers;
}
