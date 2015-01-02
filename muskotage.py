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


	# 2 - everyone texted leader order
	outbound_texts += N


	score1 = 0
	score2 = 0
	mission_number = 1
	# loop until a team wins
	while score1 < 3 and score2 < 3:
		# loop mission members until accepted
		mission_accept = False
		mission_votes  = 0
		while mission_accept == False:


			# 3a - leader texted to choose mission members
			outbound_texts += 1
			# 3b - leader responds
			incoming_texts += 1


			# 4a - All but leader texted to vote on members
			outbound_texts += N-1
			# 4b - All but leader respond
			incoming_texts += N-1


			# have a function to accept / reject team based on paranoia of players
			# paranoia_function = 0 # team always accepted
			paranoia_function = paranoia_level # team always rejected
			if paranoia_function == 1:
				mission_accept = False
			elif paranoia_function == 0:
				mission_accept = True
                        else:
                            print "choose paranoia level of 0 or 1"

			# kick out of the voting after the fifth 
			mission_votes += 1
			if mission_votes == 4:
				mission_accept = True


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


		# 6 - everyone texted success/failure of mission
		outbound_texts += N


	# 7 - everyone is texted winners of the game
	outbound_texts += N
	
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

# paranoia level 0
for j in players:
    for i in range(0, K):
   	total_outgoing[j-5,0,i], incoming_temp = muskotage(j, 0)
   	total_outgoing[j-5,1,i], incoming_temp = muskotage(j, 1)
    total_outgoing_average[j-5,0] = np.mean(total_outgoing[j-5,0,:])
    total_outgoing_max[j-5,0] = np.amax(total_outgoing[j-5,0,:])
    total_outgoing_min[j-5,0] = np.amin(total_outgoing[j-5,0,:])
    
    total_outgoing_average[j-5,1] = np.mean(total_outgoing[j-5,1,:]) 
    total_outgoing_max[j-5,1] = np.amax(total_outgoing[j-5,1,:])
    total_outgoing_min[j-5,1] = np.amin(total_outgoing[j-5,1,:])


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
ax.set_ylabel("Average number of text messages sent in the game")
ax.grid()




plt.show()
