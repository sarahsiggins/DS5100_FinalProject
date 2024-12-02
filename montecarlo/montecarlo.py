import pandas as pd
import numpy as np
import random

class Die:
    '''
    The Die object takes a numpy array to create a die. 
    Each value in the input array becomes a face of the created die. Each face must have a unique value.
    The die initally created will be "fair" (each side has a weight on 1).
    '''
    def __init__(self,faces):
        '''
        Parameters
        ----------
        faces : numpy array
            The inputted array should be a data type of strings or numbers.
        
        Raises
        ------
        TypeError
            if faces input is not a numpy array
        ValueError
            if faces array does not contain unique values
        '''
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces array must be a NumPy array")      
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Faces array contains non-distinct values.")        
        self.faces = faces
        self.weights = np.full(np.shape(self.faces),1)
        self._face_weight = pd.DataFrame({'faces':self.faces,'weights':self.weights})
        self._face_weight = self._face_weight.set_index(['faces'])
    
    def change_weight(self,change_face,new_weight):
        '''
        A method to change the weight of a single side.

        Parameters
        ----------
        change_face : str or number
            selected face to change weight of
        new_weight : number
            the new weight of the chosen face

        Raises
        ------
        IndexError
            if change_face inputted is not a face contained in the die array
        ValueError
            if new_weight is not a number

        Returns
        -------
        None
        '''
        if not (change_face in list(self._face_weight.index)):
            raise IndexError("That face is not a valid value. It is not in the die array.")
        if not isinstance(new_weight, (int, float)):
            raise TypeError("New weight value must be a number")
        else:
            self._face_weight.loc[change_face]= new_weight
        
    def roll_die(self,n_rolls = 1):
        '''
        A method to roll the die.

        Parameters
        ----------
        n_rolls: number
            number of times to roll die
            defaults to 1

        Returns
        -------
        results: list
            Results of die rolls
        '''
        results = random.choices(self._face_weight.index.values, weights=self._face_weight["weights"].values, k=n_rolls)
        return results        
    
    def die_current_state(self):
        '''
        A method to show the die’s current state.

        Parameters
        ----------
        None

        Returns
        -------
        _face_weight: private dataframe
            current faces and weights of die
        '''
        return self._face_weight


class Game:
    '''
    The Game object takes in a list of die to make a game. 
    A game consists of rolling of one or more dice (Die objects) one or more times.
    '''
    
    def __init__(self,die_list):
        '''
        Parameters
        ----------
        die_list : list
            list containing objects of the Die type
        '''     
        self.die_list = die_list
        self._played_games = pd.DataFrame()
        
    def play(self,n_rolls):
        '''
        A method to play the game, roll each die for a given amount of rolls.

        Parameters
        ----------
        n_rolls: number
            number of rolls or times to play the game

        Returns
        -------
        None
        '''     
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
        '''
        A method to show the user the results of the most recent play.

        Parameters
        ----------
        form: str; "narrow" or "wide"
            format to view results; defaults to "wide"
        
        Raises
        ------
        ValueError
            if the value of form is not "narrow" or "wide"
        
        Returns
        -------
        _played_games: dataframe
            dataframe of the most recent result from the play method 
            
        '''  
        if not (form == "wide" or form == "narrow"):
            raise ValueError("Invalid form input, must be wide or narrow")
        elif form == "wide":
            return self._played_games
        elif form == "narrow":
            return self._played_games.stack().to_frame("Face Rolled")

class Analyzer:
    '''
    The Analyzer object takes the results of a single game and computes various descriptive statistical properties about it.
    '''
    
    def __init__(self,game):
        '''
        Parameters
        ----------
        game : object
            game is a Game object
        
        Raises
        ------
        ValueError
            if game is not an object
        '''        
        if not isinstance(game, object):
            raise ValueError("Game input must be an object") 
        self.game = game

    def jackpot(self):
        '''
        A method to compute how many times the game resulted in a jackpot.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        jp_count: dataframe
            number of jackpots in the game
        '''
        self.jp_df = pd.DataFrame()
        for i in range(1,self.game.show_previous_result().T.shape[1]+1):
            if ((len(set(self.game.show_previous_result().loc[[i]].values[0].flatten())))==1):
                temp = self.game.show_previous_result().loc[[i]]
                self.jp_df = pd.concat([self.jp_df, temp], axis=0)
        self.jp_count = int(self.jp_df.shape[0])
        return self.jp_count
    
    def face_counts(self):
        '''
        A method to compute how many times a given face is rolled in each game.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        counts_df: dataframe
            has an index of the roll number, face values as columns, and count values in the cells
        '''
        self.face_counts = self.game_.show_previous_result().apply(lambda x: x.value_counts(), axis = 1).fillna(int(0))
        self.counts_df = self.face_counts
        self.counts_df.index.name = 'Roll'
        self.counts_df.columns.name = "Die Face"
        return self.counts_df
    
    def combo_count(self):
        '''
        A method to compute the distinct combinations of faces rolled, along with their counts. 
        Combinations are order-independent and may contain repetitions
        
        Parameters
        ----------
        None
        
        Returns
        -------
        combo_df: dataframe
            has a MultiIndex of distinct combinations and a column for the associated counts
        '''       
        self.combo_df = pd.DataFrame()
        self.combo_df = self.game.show_previous_result().apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Occurrence')
        self.combo_df.index.names = ["Face Value #"+str(i) for i in range(1, len(self._game._list_of_die)+1)]
        return self.combo_df
    
    def perm_count(self):
        '''
        A method to compute the distinct permutations of faces rolled, along with their counts. 
        Permutations are order-dependent and may contain repetitions.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        dataframe
            has a MultiIndex of distinct permutations and a column for the associated counts.
        '''   
        self.perm_df = pd.DataFrame()
        new_names = ["#"+str(i)+" die's value" for i in range(1, len(self.game.die_list)+1)]
        temp_df = self.game.show_previous_result()
        temp_df.columns = new_names
        x = list(range(len(self.game.die_list)))
        return temp_df.set_index(new_names).sort_index().groupby(level=x).size().to_frame("Occurence")