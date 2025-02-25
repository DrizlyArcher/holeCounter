def summary(finalScoresArray, playerNamesArray, totalParValue):
    
    for index, player in enumerate(playerNamesArray):
        print(f'{player} scored {finalScoresArray[index]}/{totalParValue} \n\n')
        
    return

