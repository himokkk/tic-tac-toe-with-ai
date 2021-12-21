from copy import deepcopy
class AI:
    def __init__(self, game, o_x):
        self.game = game
        self.o_x = o_x    
        self.temp = 0  
    def print_board(self, board):
        for x in range(0, 8, 3):
            print("|", board[x], "|",board[x+1], "|", board[x+2], "|")
        print('\n') 
    def move(self):
        self.board = self.game.board
        self.move_strength = [-99999999 for _ in range(9)]
        self.win = [True for _ in range(9)]
        board = deepcopy(self.board)
        available_moves = [index for index, item in enumerate(self.board) if item == ' '] 
        for index, item in enumerate(board):
            if item == ' ':
                self.move_strength[index] = 0
        for x in available_moves:
            board_temp = deepcopy(board)
            board_temp[x] = self.o_x
            self.combinate(board_temp, x)
        move = self.move_strength.index(max(self.move_strength))
        self.game.move(move)     

    def combinate(self, board, moved):
        from main import winner 
        available_moves = [index for index, item in enumerate(board) if item == ' ']             
        moving = 'x' if board.count('o') >= board.count('x') else 'o'
        temp = 'o' if self.o_x == 'x' else 'x'
        for i in available_moves:
            run = True
            for x in range(0, 22, 3):
                if(board[winner[x]]==self.o_x and board[winner[x+1]]==self.o_x and board[winner[x+2]]==self.o_x):
                    self.move_strength[moved] += 1*len(available_moves)+1
                        
                    run = False 
                elif(board[winner[x]]==temp and board[winner[x+1]]==temp and board[winner[x+2]]==temp):
                    self.move_strength[moved] -= 1*len(available_moves)+1 
                    self.win[moved] = False
                    run = False 
            if run:
                board_temp = deepcopy(board)
                board_temp[i] = moving                    
                self.combinate(board_temp, moved)


