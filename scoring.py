import os


def scoring(totalHoleCount, playersArray):
    
    currentHole = 0
    playerScores = []
    totalPar = 0

    for player in playersArray:
        startingScore = 0
        playerScores.append(startingScore)
    
    while currentHole < totalHoleCount:
        
        par = input(f'What is par for hole {currentHole + 1}? ')
        for index, player in enumerate(playersArray):
            print(f'Current hole: {currentHole + 1}\n\n')
            
            score = input(f'What did {player} score? \n')

            playerScores[index] = playerScores[index] + int(score)
            totalPar += int(par)
            os.system("clear")

        currentHole += 1

    return playerScores, totalPar

