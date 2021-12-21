from copy import deepcopy
from ai import AI
from player import Player
import random
winner = [
0, 1, 2,  #row1
3, 4, 5,  #row2
6, 7, 8,  #row3
0, 3, 6,  #column1
1, 4, 7,  #column2
2, 5, 8,  #column3
2, 4, 6,  #cross1
0, 4, 8,  #cross2
]

class Game:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.moving = 'o'  
        self.temp = 0      
        
    def start(self):
        print("\nWelcome to the game.\n")    
        print("Menu:")    
        print("1.Play player vs player")  
        print("2.Play player vs computer\n")
        x = int(input())
        rnd = random.uniform(0, 1)
        ai1 = AI(self, 'o')
        ai2 = AI(self, 'x')
        player1 = Player(self, 'o')
        player2 = Player(self, 'x')
        self.player1 = player1
        self.player2 = ai2
        self.print_board()

    def available_moves(self):
        self.available_moves_handler = [index for index, item in enumerate(self.board) if item == ' ']

    def check_win(self):
        global winner
        for x in range(0, 22, 3):
            if(self.board[winner[x]]=='o' and self.board[winner[x+1]]=='o' and self.board[winner[x+2]]=='o'): 
                print("Player o wins.\n")
                self.__init__()
            if(self.board[winner[x]]=='x' and self.board[winner[x+1]]=='x' and self.board[winner[x+2]]=='x'):
                print("Player x wins.\n")
                self.__init__()
    def print_board(self):
        for x in range(0, 8, 3):
            print("|", self.board[x], "|",self.board[x+1], "|", self.board[x+2], "|")
        print("\nChoose a move from 0-8:\n")
        if self.moving == 'o':
            self.player1.move()
        else:
            self.player2.move()

    def move(self, move):
        self.available_moves()
        for i in self.available_moves_handler:
            if i == move:
                self.board[i] = self.moving
                if self.moving == 'o':
                    self.moving = 'x'
                else:
                    self.moving = 'o'
        self.check_win()
        self.print_board()     
        

game = Game()
game.start()
