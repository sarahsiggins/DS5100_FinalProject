import unittest
import montecarlo
import pandas as pd
import numpy as np

class MonteCarloTestSuite(unittest.TestCase):
    
    def test_die_init(self): 
        self.assertRaises(TypeError, montecarlo.Die,int(3))
        
    def test_die_change_weight(self):
        coin = montecarlo.Die(np.array(["H", "T"]))
        coin.change_weight("H", 5)
        change_test = coin.die_current_state().loc['H'][0]
        expected = 5
        self.assertEqual(change_test, expected)
                
    def test_die_roll_die(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        num_rolls = 5
        num_roll_test = len(coin.roll_die(n_rolls = 5))
        self.assertEqual(num_roll_test, num_rolls)
        
    def test_die_die_current_state(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        df = coin.die_current_state()
        curr_state = isinstance(df, pd.DataFrame)
        self.assertTrue(curr_state)        

    def test_game_init(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        game_init = isinstance(game, object)
        self.assertTrue(game_init)    
        
    def test_game_play(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        game.play(n_rolls = 10)
        game_play = isinstance(game._played_games, pd.DataFrame)
        self.assertTrue(game_play)
        
    def test_game_show_previous_result(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        game.play(n_rolls = 10)
        self.assertRaises(ValueError, game.show_previous_result,"test")

    def test_analyzer_init(self): 
        self.assertRaises(ValueError, montecarlo.Analyzer,str("test"))
        
    def test_analyzer_jackpot(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        analyzer = montecarlo.Analyzer(game)
        analyzer_jackpot = isinstance(analyzer.jackpot(), int)
        self.assertTrue(analyzer_jackpot)

    def test_analyzer_face_counts(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        analyzer = montecarlo.Analyzer(game)
        analyzer_face_counts = isinstance(analyzer.face_counts(), pd.DataFrame)
        self.assertTrue(analyzer_face_counts)
        
    def test_analyzer_combo_count(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        game.play(n_rolls = 10)
        analyzer = montecarlo.Analyzer(game)
        analyzer_combo_count = isinstance(analyzer.combo_count(), pd.DataFrame)
        self.assertTrue(analyzer_combo_count)
        
    def test_analyzer_perm_count(self): 
        coin = montecarlo.Die(np.array(["H", "T"]))
        game = montecarlo.Game(die_list = [coin, coin]) 
        game.play(n_rolls = 10)
        analyzer = montecarlo.Analyzer(game)
        analyzer_perm_count = isinstance(analyzer.perm_count(), pd.DataFrame)
        self.assertTrue(analyzer_perm_count)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)