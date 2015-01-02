import matplotlib.pyplot as plt


players = [5, 6, 7, 8, 9, 10]

# from paranoia level 0
texts0   = [66.68 ,80.25 ,91.36 ,106.58 ,117.98 , 128.95]
# from paranoia level 1
texts1   = [128.49832, 154.55275, 177.81143, 205.61285, 229.3235, 252.9025]

plt.figure(1)
plt.title('Results of 100,000 trials')
plt.xlabel("Number of players in game")
plt.ylabel("Average number of text messages sent in the game")
plt.plot(players,texts0,label='team always accepted', color='c')
plt.plot(players,texts1,label='team always rejected', color='k')
plt.grid()
plt.legend(loc='best')

plt.show()