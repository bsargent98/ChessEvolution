#open 'data/game_list.csv' for reading
#iterate through all games. For each game:
	#Record result and number of moves
	#use dict where key is length in moves and value is list of dim 3
		#First element is #of white wins for games of that length, 2nd is # of black wins, third, is # of draws
	
#For each key in dict:
	#Find proportion of each result and store in list where i-th element is distribution for i-length games
#Save all of these distributions in a csv so we don't have to repeat computation to see/plot the results again

#Plot that shit and check for a 'drop-off' point where games are more likely to end in draw

import math
import time


e4_dists = {}
not_e4_dists = {}

e4_games = 0
not_e4_games = 0

e4_diff_total = 0
e4_diff_abs = 0
not_e4_diff_total = 0
not_e4_diff_abs = 0

t1 = time.time()
with open('data/game_list.csv', 'r') as fp:
	line = fp.readline()
	line = fp.readline()
	
	while line:
		data = line.split(',')
		
		#for datum in data:
		#	if datum[0:2] == '1.':
		#		moves = datum.split()
		
		moves = data[-2].split()
		
		length = math.ceil(len(moves)/3)
		
		if len(moves) < 2:
			line = fp.readline()
			continue
		
		result = data[-1].strip()
		
		whiteElo = int(data[-4])
		blackElo = int(data[-3])
		eloDiff = whiteElo - blackElo
		absEloDiff = abs(whiteElo - blackElo)
		
		
		if result == '1-0':
			print('white')
			if moves[1] == 'e4':
				e4_games = e4_games + 1
				e4_diff_total = e4_diff_total + eloDiff
				e4_diff_abs = e4_diff_abs + absEloDiff
				
				print('e4')
				if length not in e4_dists:
					e4_dists[length] = [1, 0, 0, 0]
				else:
					e4_dists[length][0] = e4_dists[length][0] + 1
			else:
				not_e4_games = not_e4_games + 1
				not_e4_diff_total = not_e4_diff_total + eloDiff
				not_e4_diff_abs = not_e4_diff_abs + absEloDiff
				
				print('not e4')
				if length not in not_e4_dists:
					not_e4_dists[length] = [1, 0, 0, 0]
				else:
					not_e4_dists[length][0] = not_e4_dists[length][0] + 1
				
		elif result == '0-1':
			print('black')
			if moves[1] == 'e4':
				e4_games = e4_games + 1
				e4_diff_total = e4_diff_total + eloDiff
				e4_diff_abs = e4_diff_abs + absEloDiff
				
				print('e4')
				if length not in e4_dists:
					e4_dists[length] = [0, 1, 0, 0]
				else:
					e4_dists[length][1] = e4_dists[length][1] + 1
			else:
				not_e4_games = not_e4_games + 1
				not_e4_diff_total = not_e4_diff_total + eloDiff
				not_e4_diff_abs = not_e4_diff_abs + absEloDiff
				
				print('not e4')
				if length not in not_e4_dists:
					not_e4_dists[length] = [0, 1, 0, 0]
				else:
					not_e4_dists[length][1] = not_e4_dists[length][1] + 1
				
		elif result == '1/2-1/2':
			print('draw')
			if moves[1] == 'e4':
				e4_games = e4_games + 1
				e4_diff_total = e4_diff_total + eloDiff
				e4_diff_abs = e4_diff_abs + absEloDiff
				
				print('e4')
				if length not in e4_dists:
					e4_dists[length] = [0, 0, 1, 0]
				else:
					e4_dists[length][2] = e4_dists[length][2] + 1
			else:
				not_e4_games = not_e4_games + 1
				not_e4_diff_total = not_e4_diff_total + eloDiff
				not_e4_diff_abs = not_e4_diff_abs + absEloDiff
				
				print('not e4')
				if length not in not_e4_dists:
					not_e4_dists[length] = [0, 0, 1, 0]
				else:
					not_e4_dists[length][2] = not_e4_dists[length][2] + 1
				
		elif result == '*':
			print('unknown')
			if moves[1] == 'e4':
				e4_games = e4_games + 1
				e4_diff_total = e4_diff_total + eloDiff
				e4_diff_abs = e4_diff_abs + absEloDiff
				
				print('e4')
				if length not in e4_dists:
					e4_dists[length] = [0, 0, 0, 1]
				else:
					e4_dists[length][3] = e4_dists[length][3] + 1
			else:
				not_e4_games = not_e4_games + 1
				not_e4_diff_total = not_e4_diff_total + eloDiff
				not_e4_diff_abs = not_e4_diff_abs + absEloDiff
				
				print('not e4')
				if length not in not_e4_dists:
					not_e4_dists[length] = [0, 0, 0, 1]
				else:
					not_e4_dists[length][3] = not_e4_dists[length][3] + 1
				
		else:
			print('ERROR! UNKNOWN RESULT: {}'.format(result))
			exit(0)
	
		line = fp.readline()
t2 = time.time()

print('Time to count game results: {}. Writing...'.format(t2-t1))
			
t3 = time.time()
with open('data/e4_dists.csv', 'w') as fp:
	fp.write('length,white,black,draw,unknown\n')
	for key in e4_dists:
		fp.write('{},{},{},{},{}\n'.format(key, e4_dists[key][0], e4_dists[key][1], e4_dists[key][2], e4_dists[key][3]))
		
with open('data/not_e4_dists.csv', 'w') as fp:
	fp.write('length,white,black,draw,unknown\n')
	for key in not_e4_dists:
		fp.write('{},{},{},{},{}\n'.format(key, not_e4_dists[key][0], not_e4_dists[key][1], not_e4_dists[key][2], not_e4_dists[key][3]))
		
with open('data/avg_elo_diff_by_opening.txt', 'w') as fp:
	fp.write('e4: {} total elo differential over {} games; {} is average differential'.format(e4_diff_total, e4_games, e4_diff_total/e4_games))
	fp.write('e4: {} abs elo differential over {} games; {} is average differential'.format(e4_diff_abs, e4_games, e4_diff_abs/e4_games))
	fp.write('not e4: {} total elo differential over {} games; {} is average differential'.format(not_e4_diff_total, not_e4_games, not_e4_diff_total/not_e4_games))
	fp.write('not e4: {} abs elo differential over {} games; {} is average differential'.format(not_e4_diff_abs, not_e4_games, not_e4_diff_abs/not_e4_games))
t4 = time.time()
		
print('Time to write: {}. Thank you for using this shitty code.'.format(t4-t3))