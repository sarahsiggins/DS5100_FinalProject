# Monte Carlo Package:

## Metadata:
Sarah Christen - DS 5100 Final Project (Monte Carlo Module)

## Synopsis:
The **``Monte Carlo Package``** is a Python package with three classes: ``Die``, ``Game``, and ``Analyzer``. Class descriptions and demonstration code are included below to demo how to install, import, and use the code to (1) create dice, (2) play a game, and (3) analyze a game.

## Classes and attributes:

### Die Class:
The Die object takes a numpy array to create a die. Each value in the input array becomes a face of the created die. Each face must have a unique value. The die initally created will be "fair" (each side has a weight on 1).
#### Attributes:
- None
#### Methods:
##### ``__init__(self, faces)``:
Initializer that takes an array of ``faces`` of any length, initializes weights to 1.
###### Parameters:
- ``faces``: numpy array
###### Raises:
- ``TypeError`` if faces input is not a numpy array.
- ``ValueError`` if faces array does not contain unique values.
##### ``change_weight(self,change_face,new_weight)``:
A method to change the weight of a single side.
###### Parameters:
- ``change_face``: str or number
- ``new_weight``: number
###### Raises:
- ``IndexError`` if change_face inputted is not a face contained in the die array.
- ``ValueError``  if new_weight is not a number.
##### ``roll_die(self,n_rolls = 1)``:
A method to roll the die.
###### Parameters:
- ``n_rolls``: number
###### Returns:
A list of results of the die rolls.
##### ``die_current_state(self)``:
A method to show the die’s current state.
###### Parameters:
- None
###### Returns:
A dataframe with the current faces and weights of the die.



### Game Class:
The Game object takes in a list of die to make a game. A game consists of rolling of one or more dice (Die objects) one or more times.
#### Attributes:
- None
#### Methods:
##### ``__init__(self,die_list)``:
Initializer that takes a single parameter — a list of already instantiated Die objects.
###### Parameters:
- ``die_list``: list
##### ``play(self,n_rolls)``:
A method to play the game, roll each die for a given amount of rolls.
###### Parameters:
- ``n_rolls``: number
##### ``show_previous_result(self,form = "wide")``:
A method to show the user the results of the most recent play.
###### Parameters:
- ``form``: string
###### Raises:
- ``ValueError`` if the value of form is not "narrow" or "wide"
###### Returns:
A dataframe of the most recent result from the play method.
        


### Analyzer Class:
The Analyzer object takes the results of a single game and computes various descriptive statistical properties about it.
#### Attributes:
- None
#### Methods:
##### ``__init__(self, game)``:
Initializer that takes a game object as its input parameter.
###### Parameters:
- ``game``: object.
###### Raises:
- ``ValueError`` if game is not an object
##### ``jackpot(self)``:
 A method to compute how many times the game resulted in a jackpot.
###### Parameters:
- None
###### Returns:
A dataframe of the number of jackpots in the game.
##### ``face_counts(self)``:
A method to compute how many times a given face is rolled in each game.
###### Parameters:
- None
###### Returns:
A dataframe that has an index of the roll number, face values as columns, and count values in the cells.
##### ``combo_count(self)``:
A method to compute the distinct combinations of faces rolled, along with their counts. Combinations are order-independent and may contain repetitions.
###### Parameters:
- None
###### Returns:
A dataframe that has a MultiIndex of distinct combinations and a column for the associated counts.
##### ``perm_count(self)``:
A method to compute the distinct permutations of faces rolled, along with their counts. Permutations are order-dependent and may contain repetitions.
###### Parameters:
- None
###### Returns:
A dataframe that has a MultiIndex of distinct permutations and a column for the associated counts.

    



- - - -
## Installing:
```python
!pip install -e .
```
## Importing: 
```python
import montecarlo
from montecarlo import montecarlo
```
## Creating dice:
- Create the die object called ``testDie``:

```python
testDie = montecarlo.Die(np.array(["H", "T"]))
```

- Change the weight of ``"H"``:

```python
testDie.change_weight("H", 3)
```

- Show the current faces and weights of ``testDie``:

```python
testDie.die_current_state()
```

- Roll ``myDie`` five times:

```python
testDie.roll_die(n_rolls = 5)
```
## Playing games:
- Create the game object ``testGame``:

```python
testGame = montecarlo.Game(die_list = [testDie, testDie]) 
```

- Play the game using ``testGame``, input value in the ``n_rolls`` parameter to specify number of times each die is to be rolled:

```python
testGame.play(n_rolls = 100)
```

- Show the results of ``play``, input either 'wide' or 'narrow' for the ``form`` parameter to specify the format of the df of results to be shown (defaults to wide).

```python
testGame.show_previous_result(form = "narrow")
```
## Analyzing games:
- Create the analyzer object ``testAnalyzer`` using ``testGame``:

```python
testAnalyzer = montecarlo.Analyzer(testGame)
```

- Find out how many times a jackpot occurred:

```python
testAnalyzer.jackpot()
```

- Return a df with counts for the occurrence of each face value per roll:

```python
testAnalyzer.face_counts()
```

- Find out the combinations of faces rolled and their counts:

```python
testAnalyzer.combo_count()
```

- Find out the permutations of faces rolled and their counts:

```python
testAnalyzer.perm_count()
```