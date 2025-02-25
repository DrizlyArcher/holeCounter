def getPlayerNames(playerCount):
    currentCount = 1
    playerNames = []

    print(f"Number of players: {playerCount}")

    while currentCount <= int(playerCount):
            
        playerName = input(f"What is player {currentCount}'s name?")

        currentCount += 1
        
        playerNames.append(playerName)

    return playerNames 
