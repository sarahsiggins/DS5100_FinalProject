import pandas as pd
import numpy as np

class Die:
    
    "This is a class to create, roll, and change a die of N sides, or faces, that is weighted fair or unfair."
    
    def __init__(self,faces,weights=np.array()):
        # saves faces and weights in private data frame with faces as index
        if not isinstance(faces, np.array):
            raise TypeError("Faces array must be a NumPy array")      
        if not isinstance(faces, (str, int, float)):
            raise TypeError("Faces array values must be a string or number")
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Faces array contains non-distinct values.")        
        self.faces = faces
        self.weights = np.full(np.shape(self.faces),1)
        self._face_weight = pd.DataFrame({'faces':self.faces,'weights':self.weights})
        self._face_weight = face_weight.set_index(['faces'])
    
    def change_weight(self,change_face,new_weight):
        if not (change_face in list(self._face_weight['faces'])):
            raise IndexError("That face is not a valid value. It is not in the die array.")
        if not isinstance(new_weight, (int, float)):
            raise TypeError("New weight value must be a number")
        else:
            self._face_weight.loc[self._face_weight['faces'] == change_face,'weights']= new_weight
        
    def roll_die(self,n_rolls = 1):
        "Roll the die using the object's specified number of rolls______. Save as list of outcome do not store internally"
        results = self._face_weight.sample(n=n_rolls,weights = "weights",replace = True)
        return list(results['faces'])
    
    def die_current_state(self):
        return self._face_weight
