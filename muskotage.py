def muskotage(N, M):
	if len(M) != N:
		print "Error: length of paranoia array is not equal to the number of players"
		return None

	outbound_texts = 0
	incoming_texts = 0
	# N = number of players
	# M equals array of paranoia level for each player

	# 1) all texted assignments
	# 2) all texted leader order
	# 3) leader texted to choose mission members
	# 4) all but leader vote on mission members
	# 5)  success -> mission members vote to aid/sab mission
	#      fail          -> goes back to (3) with next leader
	# 6) all texted new scores, goes back to (3) with next leader
	# 7) everyone texted who won game
	# * based on length, some of these could require 2 texts! 

	# 1 - everyone texted assignment
	outbound_texts += N

	# 2 - everyone texted leader order
	outbound_texts += N

	score1 = 0
	score2 = 0
	# loop until a team wins
	while score1 < 3 and score2 < 3:
		
		# loop mission members until accepted
		accept = False
		while accept == False:
			# 3a - leader texted to choose mission members
			outbound_texts += 1
			# 3b - leader responds
			incoming_texts += 1

			# 4a - All but leader texted to vote on members
			outbound_texts += N-1
			# 4b - All but leader respond
			incoming_texts += N-1

			# have a function to accept / reject team based on paranoia of players
			paranoia_function = 0.5
			if paranoia_function > 1:
				accept = False
			else:
				accept = True

		# 5 mission members texted to report success/failure of mission
		outbound_texts += N-3
		success = True
		if success == True:
			score1 += 1
		else:
			score2 += 1
	return [outbound_texts, incoming_texts]






a = muskotage(4, [0, 1, 1, 1])