from assets import Assets
import time
player = 'X'
board = [
	['11', '21', '31'],
	['12', '22', '32'],
	['13', '23', '33']
]

print('These are the coordinates for each space in the board')
Assets.print_board(board, 'start')
next = input('Press enter to continue >')
Assets.clear()
board = [
	[' ', ' ', ' '],
	[' ', ' ', ' '],
	[' ', ' ', ' ']
]
def game(player, board):
	while True:
		Assets.clear()
		Assets.print_board(board, 'reg')
		if Assets.check_win(board) != True:
			print(f'Player {player}, it\'s your turn!')
			coordinates = input('Please enter the coordinates for your space >')
			x = int(coordinates[0]) - 1
			y = int(coordinates[1]) - 1
			if board[y][x] == ' ':
				board[y][x] = player
			else:
				print('That spot\'s already taken!')
				time.sleep(0.8)
				game(player, board)
			if player == 'X':
				player = 'O'
			elif player == 'O':
				player = 'X'
		else:
			if player == 'X':
				player = 'O'
			elif player == 'O':
				player = 'X'
			print(f'Player {player} wins')
			break

game(player, board)
