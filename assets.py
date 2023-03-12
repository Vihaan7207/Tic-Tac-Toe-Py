import sys, os

class Assets:
	def print_board(board, type):
		if type == 'start':
			print('----------')
		elif type == 'reg':
			print('-------')
		for i in range(3):
			sys.stdout.write('|')
			for j in range(3):
				sys.stdout.write(board[i][j] + '|')
			sys.stdout.write('\n')
		if type == 'start':
			print('----------')
		elif type == 'reg':
			print('-------')

	def check_win(board):
		# Check first row
		if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
			if ((board[0][0] or board[0][1] or board[0][2]) == ' '):
				return False
			else:
				return True
		# Check second row
		elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
			if ((board[1][0] or board[1][1] or board[1][2]) == ' '):
				return False
			else:
				return True
		# Check third row
		elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
			if ((board[2][0] or board[2][1] or board[2][2]) == ' '):
				return False
			else:
				return True
		# Check first column
		elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
			if ((board[0][0] or board[1][0] or board[2][0]) == ' '):
				return False
			else:
				return True
		# Check second column
		elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
			if ((board[0][1] or board[1][1] or board[2][1]) == ' '):
				return False
			else:
				return True
		# Check third column
		elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
			if ((board[0][2] or board[1][2] or board[2][2]) == ' '):
				return False
			else:
				return True
		# Check top-left to bottom-right
		elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
			if((board[0][0] or board[1][1] or board[2][2]) == ' '):
				return False
			else:
				return True
		# Check top-right to bottom-left
		elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
			if((board[0][2] or board[1][1] or board[2][0]) == ' '):
				return False
			else:
				return True

	def clear():
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
