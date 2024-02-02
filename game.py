import math
import time

from player import humanPlayer, computerPlayer

class tictactoe():
    def __init__(self):
        self.board = self.makeBoard()
        self.gameWinner = None
        
    @staticmethod
    def makeBoard():
        return [' ' for _ in range(9)]
    
    def printBoard(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod        
    def printBoardNums():
        rows = [[str(i) for i in range(r*3, (r+1)*3)] for r in range(3)]
        for row in rows:
            print('| ' + ' | '.join(row) + ' |')
    
    def validMove(self, name, position):
        if self.board[position] == ' ':
            self.board[position] = name
            if self.winner(name, position):
                self.gameWinner = name
            return True
        return False
    
    def winner(self, name, position):
        
        # row check
        rowId = math.floor(position / 3)
        vals = self.board[rowId*3:(rowId + 1)*3]
        if all([r == name for r in vals]):
            return True
        
        # column check
        colId = position % 3
        vals = [self.board[colId + (r * 3)] for r in range(3)]
        if all([c == name for c in vals]):
            return True
        
        # diagonal check
        if position % 2 == 0:
            # left-right diagonal --> [0, 4, 8] indexes
            vals = [self.board[i] for i in [0, 4, 8]]
            if all([d1 == name for d1 in vals]):
                return True
            
            # right-left diagonal --> [2, 4, 6] indexes
            vals = [self.board[i] for i in [2, 4, 6]]
            if all([d2 == name for d2 in vals]):
                return True
        
        return False
                
    def availableMoves(self):
        return [i for i in range(9) if self.board[i] == ' ']
    

def play(game, x_player, o_player):
    
    name = "x"    # let x  be the first player to take a move

    while len(game.availableMoves()) > 0:
        if name == "x":
            game.printBoardNums()
            pos = x_player.getMove(game)
        else:
            pos = o_player.getMove(game)
        
        if game.validMove(name, pos):
            print(f"\n{name} player made a move to position {pos}.")
            
            print("\ncurrent grid:")
            game.printBoard()
            print(" ")
            
        if game.gameWinner:
            print(f"Player {name} wins! Well played.")
            return name
        
        name = "o" if name == "x" else "x"
        
        time.sleep(1)
            
    print("It's a tie!")


if __name__ == '__main__':
    x_player = humanPlayer("x")
    o_player = computerPlayer("o")
    game = tictactoe()
    play(game, x_player, o_player)
    