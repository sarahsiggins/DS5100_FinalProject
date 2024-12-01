import pandas as pd
import numpy as np

class Analyzer:
    
    def __init__(self,game):
        if not isinstance(game, object):
            raise ValueError("Game input must be an object") 
        self.game = game

    def jackpot(self):
        self.jp_df = pd.DataFrame()
        for i in range(1,self.game.show_previous_result().T.shape[1]+1):
            if ((len(set(self.game.show__previous_result().loc[[i]].values[0].flatten())))==1):
                temp = self.game.show_previouw_result().loc[[i]]
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
        temp_df = self._game.show_previous_result()
        temp_df.columns = new_names
        x = list(range(len(self.game.die_list)))
        return temp_df.set_index(new_names).sort_index().groupby(level=x).size().to_frame("Occurence")