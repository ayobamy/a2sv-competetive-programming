def heads_tic_tac_toe(board):
    team_count = 0
    individual_count = 0

    for r in board:
        heads_count = {}
        for letter in r:
            if letter in heads_count:
                heads_count[letter] += 1
            heads_count[letter] = 0

        if len(heads_count) == 1:
            individual_count += 1
        elif len(heads_count) == 2:
            team_count += 1
    
    for j in range(3):
        heads_count = {}
        for i in range(3):
            char = board[i][j]
            if char not in heads_count:
                heads_count[char] = 0
            heads_count[char] += 1

        if len(heads_count) == 1:
            individual_count += 1
        elif len(heads_count) == 2:
            team_count += 1
    
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]

    heads_count = {}
    for char in diagonal1:
        if char not in heads_count:
            heads_count[char] = 0
        heads_count[char] += 1

    if len(heads_count) == 1:
        individual_count += 1
    elif len(heads_count) == 2:
        team_count += 1

    heads_count = {}
    for char in diagonal2:
        if char not in heads_count:
            heads_count[char] = 0
        heads_count[char] += 1

    if len(heads_count) == 1:
        individual_count += 1
    elif len(heads_count) == 2:
        team_count += 1

    return individual_count, team_count

# Tests
board = []
for _ in range(3):
    r = input().strip()
    board.append(r)

individual_count, team_count = heads_tic_tac_toe(board)
print(individual_count)
print(team_count)
