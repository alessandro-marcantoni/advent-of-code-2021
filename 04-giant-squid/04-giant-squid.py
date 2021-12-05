def draw_number(number, board):
    return [[e if e != number else '' for e in r] for r in board]

def check_board(board):
    return (any([True if all([True if e == '' else False for e in r]) else False for r in board]) 
         or any([True if all([True if e == '' else False for e in [r[i] for r in board]]) else False for i in range(len(board))]))

def score(board):
    return sum([sum([int(e) for e in r if e != '']) for r in board])

file = open('04-giant-squid-input.txt', 'r')
lines = file.readlines()
numbers = lines[0].strip().split(",")
boards = [l.strip().replace("  ", " ").split(" ") for (i, l) in enumerate(lines[1:]) if i % 6 != 0]
boards = [boards[i:i+5] for i in range(0, len(boards), 5)]

for n in numbers:
    for i in range(len(boards)):
        boards[i] = draw_number(n, boards[i])
    for board in [b for b in boards if check_board(b)]:
        print(score(board) * int(n))
        boards.remove(board)