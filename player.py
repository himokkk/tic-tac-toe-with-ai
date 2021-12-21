class Player:
    def __init__(self, game, o_x):
        self.o_x = o_x
        self.game = game
    def move(self):
        self.game.print_board
        x = int(input())
        self.game.move(x) 
