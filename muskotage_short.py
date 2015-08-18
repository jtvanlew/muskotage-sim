mission_dict = {
			  "10": {"1": [  3,   1], "3": [  4,   1], "2": [  4,   1], "5": [  5,   1], "4": [  5,   2]
			  }, 
			  "5": {"1": [  2,   1], "3": [  2,   1], "2": [  3,   1], "5": [  3,   1], "4": [  3,   1]
			  }, 
			  "7": {"1": [  2,   1], "3": [  3,   1], "2": [  3,   1], "5": [  4,   1], "4": [  4,   2]
			  }, 
			  "6": {"1": [  2,   1], "3": [  4,   1], "2": [  3,   1], "5": [  4,   1], "4": [  3,   1]
			  }, 
			  "9": {"1": [  3,   1], "3": [  4,   1], "2": [  4,   1], "5": [  5,   1], "4": [  5,   2]
			  }, 
			  "8": {"1": [  3,   1], "3": [  4,   1], "2": [  4,   1], "5": [  5,   1], "4": [  5,   2]
			  }
			}



def muskotage(N, paranoia_level):
	# N 			 = number of players
	# paranoia_level = equals array of paranoia level for each player

	try:
		import random
	except:
		print "error no random module"
		return None
	if N < 5 or N > 10:
		print "Error: number of players must be between 5 and 10"
		return None

	outbound_texts = 0
	incoming_texts = 0


	# 1 - everyone texted assignment
	outbound_texts += N



	score1 = 0
	score2 = 0
	mission_number = 1
	# loop until a team wins
	while score1 < 3 and score2 < 3:
		

		# 5a - mission members only vote
		mission_member_size = mission_dict[str(N)][str(mission_number)][0]
		outbound_texts += mission_member_size
		# print "number of mission members: %s, on mission number: %s"%(mission_member_size, mission_number)
		# 5b - mission members only respond
		incoming_texts += mission_member_size


		# just do random success or failure because who cares for this
		success = bool(random.getrandbits(1))
		if success == True:
			score1 += 1
		else:
			score2 += 1
		mission_number += 1



	
	verbose = False
	if verbose == True:
		if score1 == 3:
			print "Colonists win in %s rounds"%(mission_number-1)
		else:
			print "Saboteurs win in %s rounds"%(mission_number-1)


	return [outbound_texts, incoming_texts]


import numpy as np
K = 10000
players = range(5,11)

total_outgoing = np.zeros([len(players),2,K])
total_outgoing_average = np.zeros([len(players),2])
total_outgoing_max = np.zeros([len(players),2])
total_outgoing_min = np.zeros([len(players),2])

total_incoming = np.zeros([len(players),2,K])
total_incoming_average = np.zeros([len(players),2])
total_incoming_max = np.zeros([len(players),2])
total_incoming_min = np.zeros([len(players),2])

# paranoia level 0
for j in players:
    for i in range(0, K):
   	total_outgoing[j-5,0,i], total_incoming[j-5,0,i] = muskotage(j, 0)
   	total_outgoing[j-5,1,i], total_incoming[j-5,1,i] = muskotage(j, 1)

    total_outgoing_average[j-5,0] = np.mean(total_outgoing[j-5,0,:])
    total_outgoing_max[j-5,0] = np.amax(total_outgoing[j-5,0,:])
    total_outgoing_min[j-5,0] = np.amin(total_outgoing[j-5,0,:])
    
    total_outgoing_average[j-5,1] = np.mean(total_outgoing[j-5,1,:]) 
    total_outgoing_max[j-5,1] = np.amax(total_outgoing[j-5,1,:])
    total_outgoing_min[j-5,1] = np.amin(total_outgoing[j-5,1,:])

    total_incoming_average[j-5,0] = np.mean(total_incoming[j-5,0,:])
    total_incoming_max[j-5,0] = np.amax(total_incoming[j-5,0,:])
    total_incoming_min[j-5,0] = np.amin(total_incoming[j-5,0,:])
    
    total_incoming_average[j-5,1] = np.mean(total_incoming[j-5,1,:]) 
    total_incoming_max[j-5,1] = np.amax(total_incoming[j-5,1,:])
    total_incoming_min[j-5,1] = np.amin(total_incoming[j-5,1,:])

import matplotlib.pyplot as plt

# plot it!
fig, ax = plt.subplots(1)
ax.plot(players,total_outgoing_average[:,0],\
        label='team always accepted', color='c')
ax.plot(players,total_outgoing_average[:,1],\
        label='team always rejected', color='k')
ax.fill_between(players,\
                total_outgoing_max[:,0],\
                total_outgoing_min[:,0],\
                facecolor='c', alpha=0.3)
ax.fill_between(players,\
                total_outgoing_max[:,1],\
                total_outgoing_min[:,1],\
                facecolor='k', alpha=0.3)

ax.set_title('Results of %s trials'%(K))
ax.legend(loc='best')
ax.set_xlabel("Number of players in game")
ax.set_ylabel("Outgoing text messages")
ax.grid()

fig2, ax2 = plt.subplots(1)
ax2.plot(players,total_incoming_average[:,0],\
        label='team always accepted', color='m')
ax2.plot(players,total_incoming_average[:,1],\
        label='team always rejected', color='b')
ax2.fill_between(players,\
                total_incoming_max[:,0],\
                total_incoming_min[:,0],\
                facecolor='m', alpha=0.3)
ax2.fill_between(players,\
                total_incoming_max[:,1],\
                total_incoming_min[:,1],\
                facecolor='b', alpha=0.3)

ax2.set_title('Results of %s trials'%(K))
ax2.legend(loc='best')
ax2.set_xlabel("Number of players in game")
ax2.set_ylabel("Incoming text messages")
ax2.grid()

# plot it!
fig3, ax3 = plt.subplots(1)
ax3.plot(players,total_outgoing_average[:,0],\
        label='accepted, outgoing', color='k', linestyle = '--')
ax3.plot(players,total_outgoing_average[:,1],\
        label='rejected, outgoing', color='k')
        
ax3.plot(players,total_incoming_average[:,0],\
        label='accepted, incoming', color='b', linestyle = '--')
ax3.plot(players,total_incoming_average[:,1],\
        label='rejected, incoming', color='b')

ax3.plot(players,total_outgoing_average[:,0]+total_incoming_average[:,0],\
        label='accepted, total', color='g')
ax3.plot(players,total_outgoing_average[:,1]+total_incoming_average[:,1],\
        label='rejected, total', color='r')
ax3.fill_between(players,\
                total_outgoing_max[:,0]+total_incoming_max[:,0],\
                total_outgoing_min[:,0]+total_incoming_min[:,0],\
                facecolor='g', alpha=0.3)
ax3.fill_between(players,\
                total_outgoing_max[:,1]+total_incoming_max[:,1],\
                total_outgoing_min[:,1]+total_incoming_min[:,1],\
                facecolor='r', alpha=0.3)

ax3.set_title('Results of %s trials'%(K))
ax3.legend(loc='best')
ax3.set_xlabel("Number of players in game")
ax3.set_ylabel("Text messages sent in a game")
ax3.grid()

plt.show()
