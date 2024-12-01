import pandas as pd
import numpy as np

class Game:
    
    def __init__(self,die_list):
        self.die_list = die_list
        self._played_games = pd.DataFrame()
        
    def play(self,n_rolls):
        self._played_games = pd.DataFrame()
        x = 0
        
        for i in range(len(self.die_list)):
            new_result = pd.DataFrame(self.die_list[i].rolls(n_rolls))
            new_result.index = [x+1 for x in range(n_rolls)]
            new_result.index.name = "Roll Number"
            new_result.columns = [i+1]
            new_result.columns.name = "Die Number"
            self._played_games = pd.concat([self._played_games,new_result],axis = 1)
            
    def show_previous_result(self,form = "wide"):
        if not (form == "wide" or form == "narrow"):
            raise ValueError("Invalid form input, must be wide or narrow")
        elif form == "wide":
            return self._played_games
        elif form == "narrow":
            return self._played_games.stack().to_frame("Face Rolled")
        