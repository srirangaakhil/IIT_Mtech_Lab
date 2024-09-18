if __name__ == '__main__':
	num_match = int(input())
	matches = dict()
	players = dict()

	for i in range(num_match):
		match_line = input().split(':')
		match_name, player_scores = match_line[0], match_line[1]

		matches[match_name] = dict()
		
		for player_score in player_scores.split(','):
			player = player_score.split('-')
			name, score = player[0], int(player[1])

			matches[match_name][name] = score
			if name in players:
				players[name] += score
			else:
				players[name] = score

	players = list(players.items())
	players.sort(key = lambda player: (player[1], player[0]), reverse = True)

	print(matches)
	print(players)