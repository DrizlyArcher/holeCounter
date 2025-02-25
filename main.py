from getPlayerNames import getPlayerNames
from getHoleCount import getHoleCount
from scoring import scoring
from summariseScores import summary

def main():

    playerCount = input("How many players?")

    players = getPlayerNames(playerCount) 

    holeCount = getHoleCount()

    finalScores = scoring(holeCount, players)

    totalPar = finalScores[1]
    finalPlayerScores = finalScores[0]

    summary(finalPlayerScores, players, totalPar)

    input("ENTER to close...")

if __name__ == "__main__":
    main()
