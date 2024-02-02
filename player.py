import random
import math

class player():
    def __init__(self, name):
        self.name = name
    def getMove(self, game):
        pass
    
class humanPlayer(player):
    def __init__(self, name):
        super().__init__(name)
    
    def getMove(self, game):
        valid = False
        pos = None
        while not valid:
            p = input(f"{self.name} 's turn! Which position(0-8) you want to place your move: ")
            try:
                pos = int(p)
                if pos not in game.availableMoves():
                    raise ValueError
                
                valid = True
            except ValueError:
                print("Invalid position! Try again")
        return pos
    
class computerPlayer(player):
    def __init__(self, name):
        super().__init__(name)
        
    def getMove(self, game):
        pos = random.choice(game.availableMoves())
        return pos
        
    