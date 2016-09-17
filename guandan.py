# A python program to calculate the ranks of Guandan

nb = raw_input('Please input the number of players: ')
nplayers = int(nb)

if nplayers == 4 :
  while nplayers >1:
    orScore = {'1':4, '2':3, '3':2, '4':1}
    nb = raw_input('Please input the winners order:')
    order = list(nb)
    winScore = (orScore[order[0]] + orScore[order[1]]) * 2 - 10
    print 'The score of winners: ',winScore
    winStep = {4:3, 2:2, 0:1}
    print 'The Steps of winners: ',winStep[winScore]   

elif nplayers == 6:
  while nplayers >1:
    orScore = {'1':6, '2':5, '3':4, '4':3, '5':2, '6':1}
    nb = raw_input('Please input the winners order:')
    order = list(nb)
    winScore = (orScore[order[0]] + orScore[order[1]] + orScore[order[2]]) * 2 - 21
    print 'The score of winners: ',winScore
    winStep = {9:5, 7:4, 5:3, 3:2, 1:1, -1:1, -3:1}
    print 'The Steps of winners: ',winStep[winScore]   

elif nplayers == 8:
  while nplayers >1:
    orScore = orScore = {'1':8, '2':7, '3':6, '4':5, '5':4, '6':3, '7':2, '8':1}
    nb = raw_input('Please input the winners order:')
    order = list(nb)
    winScore = (orScore[order[0]] + orScore[order[1]] + orScore[order[2]] + orScore[order[3]]) * 2 - 36
    print 'The score of winners: ',winScore
    winStep = {16:5, 14:4, 12:4, 10:3, 8:3, 6:2, 4:2, 2:1, 0:1, -2:1, -4:1, -6:1, -8:1, -10:1, -12:1, -14:1 }
    print 'The Steps of winners: ',winStep[winScore]   

else:
  print 'Please input number of players 4, 6 or 8'





