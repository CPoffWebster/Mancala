##############################################################################
#
# File:         test1.py
# Date:         Thu  6 Oct 2011  15:39
# Author:       Ken Basye
# Description:
#
##############################################################################

# Note no doctesting in this file; we want to run this as main to play

import games
import mancala

"""Given, for game TicTacToe

def test1():
    game = games.TicTacToe()
    named_players = (('X', games.query_player_py_exp), ('O', games.random_player))
    games.play_game(game, named_players)

def test2():
    game = games.TicTacToe()
    named_players = (('X', games.query_player_py_exp), ('O', games.alphabeta_player))
    games.play_game(game, named_players)

def test3():
    game = games.TicTacToe()
    named_players = (('X', games.random_player), ('O', games.alphabeta_player))
    games.play_game(game, named_players)

def test4():
    game = games.TicTacToe()
    named_players = (('X', games.alphabeta_full_player), ('O', games.alphabeta_player))
    games.play_game(game, named_players)
    
    """

def test1():
    game = mancala.MancalaGame()
    named_players = (('Max', games.query_player_py_exp), ('Min', games.random_player))
    games.play_game2(game, named_players)

def test2():
    game = mancala.MancalaGame()
    named_players = (('X', games.random_player), ('O', games.alphabeta_player))
    games.play_game2(game, named_players)

def test3():
    game = mancala.MancalaGame()
    named_players = (('X', games.alphabeta_player2), ('O', games.random_player))
    games.play_game2(game, named_players)

def test4():
    game = mancala.MancalaGame()
    named_players = (('X', games.alphabeta_full_player), ('O', games.alphabeta_player))
    games.play_game2(game, named_players)

if __name__ == '__main__':
    test1()
    test2()
    test3()
    for i in range(10):
        test4()