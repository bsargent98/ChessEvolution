import os
rootdir = '../pgn_by_id/'

game_set = set()
games_read = 0
games_inset = 0

for subdir, dirs, files in os.walk(rootdir):
	for dir in dirs:
		for subdir2, dirs2, files2 in os.walk(rootdir + dir):
			for file in files2:
				path = rootdir + dir + '/' + file
				with open(path, 'r') as fp:
					line = fp.readline()
					while line:
						if line[:6] == '[Event':
							games_read = games_read + 1
						
							line = line.strip()
							event = line[8:-2]
							#print(event)
							
							line = fp.readline().strip()
							site = line[7:-2]
							#print(site)
							
							line = fp.readline().strip()
							date = line[7:-2]
							#print(date)
							
							line = fp.readline().strip()
							round = line[8:-2]
							#print(round)
							
							line = fp.readline().strip()
							white = line[8:-2]
							#print(white)
							
							line = fp.readline().strip()
							black = line[8:-2]
							#print(black)
							
							line = fp.readline().strip()
							eco = line[6:-2]
							#print(eco)
							
							line = fp.readline().strip()
							whiteElo = line[11:-2]
							#print(whiteElo)
							
							line = fp.readline().strip()
							blackElo = line[11:-2]
							
							line = fp.readline()
							line = fp.readline()
							
							line = fp.readline().strip()
							moves = line
							#print(moves)
							
							line = fp.readline()
							
							line = fp.readline().strip()
							result = line
							print(result)
							
							game = (event, site, date, round, white, black, eco, whiteElo, blackElo, moves, result)
							game_set.add(game)
							
						line = fp.readline()
		
games_inset = len(game_set)

print("Games read: {}".format(games_read))
print("Games in set: {}".format(games_inset))

