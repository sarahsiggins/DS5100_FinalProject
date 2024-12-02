import pandas as pd
import numpy as np
import random

class Die:
    
    "This is a class to create, roll, and change a die of N sides, or faces, that is weighted fair or unfair."
    
    def __init__(self,faces):
        # saves faces and weights in private data frame with faces as index
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces array must be a NumPy array")      
        #if not isinstance(faces.dtype, (str, int, float)):
         #   raise TypeError("Faces array values must be a string or number")
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Faces array contains non-distinct values.")        
        self.faces = faces
        self.weights = np.full(np.shape(self.faces),1)
        self._face_weight = pd.DataFrame({'faces':self.faces,'weights':self.weights})
        self._face_weight = self._face_weight.set_index(['faces'])
    
    def change_weight(self,change_face,new_weight):
        if not (change_face in list(self._face_weight.index)):
            raise IndexError("That face is not a valid value. It is not in the die array.")
        if not isinstance(new_weight, (int, float)):
            raise TypeError("New weight value must be a number")
        else:
            self._face_weight.loc[change_face]= new_weight
        
    def roll_die(self,n_rolls = 1):
        "Roll the die using the object's specified number of rolls______. Save as list of outcome do not store internally"
        results = random.choices(self._face_weight.index.values, weights=self._face_weight["weights"].values, k=n_rolls)
        return results        
        #results = self._face_weight.sample(n=n_rolls,weights = "weights",replace = True)
        #return results #list(results['faces'])
    
    def die_current_state(self):
        return self._face_weight


class Game:
    
    def __init__(self,die_list):
        self.die_list = die_list
        self._played_games = pd.DataFrame()
        
    def play(self,n_rolls):
        self._played_games = pd.DataFrame()
        x = 0
        
        for i in range(len(self.die_list)):
            new_result = pd.DataFrame(self.die_list[i].roll_die(n_rolls))
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

class Analyzer:
    
    def __init__(self,game):
        if not isinstance(game, object):
            raise ValueError("Game input must be an object") 
        self.game = game
        
        #self.jp_count = 0
        #self.jp_df = pd.DataFrame()
        #self.combo_df = pd.DataFrame()
        #self.face_count = pd.DataFrame()
        #self.die_type = type(game._list_of_die[0])

    def jackpot(self):
        self.jp_df = pd.DataFrame()
        for i in range(1,self.game.show_previous_result().T.shape[1]+1):
            if ((len(set(self.game.show_previous_result().loc[[i]].values[0].flatten())))==1):
                temp = self.game.show_previous_result().loc[[i]]
                self.jp_df = pd.concat([self.jp_df, temp], axis=0)
        self.jp_count = int(self.jp_df.shape[0])
        return self.jp_count
    
    def face_counts(self):
        self.face_counts = self.game_.show_previous_result().apply(lambda x: x.value_counts(), axis = 1).fillna(int(0))
        self.counts_df = self.face_counts
        self.counts_df.index.name = 'Roll'
        self.counts_df.columns.name = "Die Face"
        return self.counts_df
    
    def combo_count(self):
        self.combo_df = pd.DataFrame()
        self.combo_df = self.game.show_previous_result().apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Occurrence')
        self.combo_df.index.names = ["Face Value #"+str(i) for i in range(1, len(self._game._list_of_die)+1)]
        return self.combo_df
    
    def perm_count(self):
        self.perm_df = pd.DataFrame()
        new_names = ["#"+str(i)+" die's value" for i in range(1, len(self.game.die_list)+1)]
        temp_df = self.game.show_previous_result()
        temp_df.columns = new_names
        x = list(range(len(self.game.die_list)))
        return temp_df.set_index(new_names).sort_index().groupby(level=x).size().to_frame("Occurence")