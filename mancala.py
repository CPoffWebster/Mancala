# Charlie Poff-Webster
# cs210 - AI with Basye
# mancala method for project 2


import cs210_utils


class MancalaGame(object):

    def __init__(self):
        """creates the Mancala Board"""
        self.init_state()
        self.init_player()
        self.initial = self.state

    def init_state(self):

        self.MaxMancala = 0
        self.MinMancala = 0
        self.MaxPots = [4, 4, 4, 4, 4, 4]
        self.MinPots = [4, 4, 4, 4, 4, 4]
        self.turn = 0  # 0 is Max, 1 is Min
        self.state = (self.MaxMancala, self.MinMancala, self.MaxPots, self.MinPots, self.turn)

    def init_player(self):
        self.MaxPlayer = 'X'
        self.MinPlayer = 'O'
        self.player = (self.MaxPlayer, self.MinPlayer)

    def legal_moves(self, state):
        """Return a list of the allowable moves at this point.
        A state represents the number of stones in each pit on the board.

        >>> g = MancalaGame()
        >>> g.legal_moves(g.state)  # doctest: +SKIP
        [4, 4, 4, 4, 4, 4]

        >>> g = MancalaGame()
        >>> g.legal_moves(g.state)  # doctest: +SKIP
        [4, 4, 4, 4, 4, 4]

        """
        # check whos turn it is
        # run through a for loop of all the spots
        # check to see if there are stones in a spot
        # if yes then add to the list
        # return list of spots with stones

        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        # stones on your side of the board
        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        allowable = []
        if turn == 0:
            for pos in range(0, 6):
                if MaxPots[pos] != 0:
                    allowable.append(pos)
        elif turn == 1:
            for pos in range(0, 6):
                if MinPots[pos] != 0:
                    allowable.append(pos)

        return allowable

    def make_move(self, move, state):
        """Return the state that results from making a move from a state.
        For Mancala, a move is an integer in the range 0 to 5, inclusive.

        doctest 1
        (0, 0, [4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], 0)
        to
        (0, 0, [0, 5, 5, 5, 5, 4], [4, 4, 4, 4, 4, 4], 1)
        >>> g = MancalaGame()
        >>> g.make_move(0, g.state)  # doctest: +SKIP
        (0, 0, [0, 5, 5, 5, 5, 4], [4, 4, 4, 4, 4, 4], 1)

        doctest 2
        (0, 0, [4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], 0)
        to
        (1, 0, [4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], 0)
        >>> g = MancalaGame()
        >>> g.make_move(2, g.state)  # doctest: +SKIP
        (1, 0, [4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], 0)

        doctest 3
        (0, 0, [4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4], 0)
        to
        (1, 0, [4, 4, 4, 0, 5, 5], [5, 4, 4, 4, 4, 4], 1)
        >>> g = MancalaGame()
        >>> g.make_move(2, g.state)  # doctest: +SKIP
        (1, 0, [4, 4, 0, 5, 5, 5], [4, 4, 4, 4, 4, 4], 0)

        doctest 4
        (0, 0, [4, 4, 4, 4, 4, 10], [4, 4, 4, 4, 4, 4], 0)
        to
        (1, 0, [5, 5, 5, 4, 4, 0], [5, 5, 5, 5, 5, 5], 1)
        >>> g = MancalaGame()
        >>> g.make_move(5, g.state)  # doctest: +SKIP
        (1, 0, [5, 5, 5, 4, 4, 0], [5, 5, 5, 5, 5, 5], 1)

        doctest 5
        (0, 0, [0, 4, 4, 4, 4, 8], [4, 4, 4, 4, 4, 4], 0)
        to
        (7, 0, [0, 4, 4, 4, 4, 0], [5, 5, 5, 5, 5, 0], 1)
        >>> g = MancalaGame()
        >>> g.make_move(5, g.state)  # doctest: +SKIP
        (7, 0, [0, 4, 4, 4, 4, 0], [5, 5, 5, 5, 5, 0], 1)

        """
        # after the "move"
        # board and whos turn it is
        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        MaxPots = MaxPots.copy()
        MinPots = MinPots.copy()

        if turn == 0:
            stones = MaxPots[move]  # number of stones in the pot
            MaxPots[move] = 0  # update so nothing in that pot
            pots = move

            for x in range(0, stones):
                pots += 1  # drop in a new pot each for each x in range
                if pots == 13:
                    pots = pots - 13  # reset to the original side

                # doctest 1 - just put in own side
                # doctest 4 - go completely around to the original side
                if pots < 6:  # put in MaxPots
                    MaxPots[pots] += 1

                    # doctest 5 - finish in empty pit and steal from other side
                    # if you finish in an empty pot than take all from other side
                    if x == stones - 1 and MaxPots[pots] == 1:  # only one is in the last pot placed (just placed)
                        steal_min = 5 - pots  # pot on other side
                        if MinPots[steal_min] == 0:  # don't steal
                            break
                        else:  # steal
                            steal = MinPots[steal_min] + 1  # +1 for the stone that was just put down
                            MinPots[steal_min] = 0
                            MaxPots[pots] = 0
                            MaxMancala += steal

                # doctest 2 - finish in mancala (also puts in mancala in run through)
                if pots == 6:  # put in mancala
                    MaxMancala += 1
                    # if this is the end of the stones than take another turn
                    if x == stones - 1:  # if x is the last stone in the list
                        state = MaxMancala, MinMancala, MaxPots, MinPots, turn
                        return state

                # doctest 3 - put in other side (will also test 2nd part with mancala run through)
                if 6 < pots < 13:  # put in other MinPots
                    MinPots[pots - 7] += 1  # pots - 7 recognizes the move to the other side of the board

            turn = 1  # switch turns
            state = MaxMancala, MinMancala, MaxPots, MinPots, turn
            return state

        if turn == 1:
            stones = MinPots[move]  # number of stones in the pot
            MinPots[move] = 0  # update so nothing in that pot
            pots = move

            for x in range(0, stones):
                pots += 1  # drop in a new pot each for each x in range
                if pots == 13:
                    pots = pots - 13  # reset to the original side

                # doctest 6 - just put in own side
                if pots < 6:  # put in MaxPots
                    MinPots[pots] += 1

                    # if you finish in an empty pot than take all from other side
                    if x == stones - 1 and MinPots[pots] == 1:  # only one is in the last pot placed (just placed)
                        steal_max = 5 - pots  # pot on other side
                        if MaxPots[steal_max] == 0:  # don't steal
                            break
                        else:  # steal
                            steal = MaxPots[steal_max] + 1  # +1 for the stone that was just put down
                            MaxPots[steal_max] = 0
                            MinPots[pots] = 0
                            MinMancala += steal

                if pots == 6:  # put in mancala
                    MinMancala += 1
                    # if this is the end of the stones than take another turn
                    if x == stones - 1:  # if x is the last stone in the list
                        state = MaxMancala, MinMancala, MaxPots, MinPots, turn
                        return state

                if 6 < pots < 13:  # put in other MinPots
                    MaxPots[pots - 7] += 1  # pots - 7 recognizes the move to the other side of the board

            turn = 0  # switch turns
            state = MaxMancala, MinMancala, MaxPots, MinPots, turn
            return state



    def utility(self, state, player):
        """Return the value of this final state to player.

        >>> g = MancalaGame()
        >>> g.utility(g.state, g.player)  # doctest
        1

        """
        # player != whos turn
        # return Mancala.player - Mancala.Otherplayer
        # winning means it's in positive

        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        if player == 'X':
            utility = MaxMancala - MinMancala
            return utility
        elif player == 'O':
            utility = MinMancala - MaxMancala
            return utility

    def utility2(self, state):
        """To call for evaluate function"""

        # positive values for states that are good for the maximizing player
        # negative values for states that are good for the minimizer
        # regardless of who's move it is in the game.

        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        return MaxMancala - MinMancala  # for testing alphabeta player as Max
        # return MinMancala - MaxMancala  # for testing alphabeta player as Min

    def terminal_test(self, state):
        """"Return True if this is a final state for the game.

        >>> g = MancalaGame()
        >>> g.terminal_test(g.state)  # doctest: +SKIP
        False

        """

        # Only terminate if the players whos turn it is runs out of pieces on their board
        # move all pieces from the other side into the other player's mancala if true

        # look through all of your spots
        # if there are any spots that are full return False
        # at the end if all the spots are empty return True
        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        OtherMancala = 0
        if turn == 0:
            for x in MaxPots:
                if x != 0:
                    return False
            # once terminated the board is the final state
            for y in MinPots:  # puts all stones from other side into Mancala
                OtherMancala += y
            MinMancala += OtherMancala

        elif turn == 1:
            for x in MinPots:
                if x != 0:
                    return False

            for y in MaxPots:
                OtherMancala += y
            MaxMancala += OtherMancala

        return True  # after testing if all pots are full

    def report(self, state):
        """info on who won"""
        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        return MaxMancala - MinMancala


    def to_move(self, state):
        """Return the player whose move it is in this state.

        >>> g = MancalaGame()
        >>> g.to_move(g.state)  # doctest: +SKIP
        0

        """
        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        return turn

    def display(self, state):

        """
        Print or otherwise display the state.

        >>> g = MancalaGame()
        >>> g.display(g.state)  # doctest: +SKIP
          [4, 4, 4, 4, 4, 4]
        0                    0
          [4, 4, 4, 4, 4, 4]

        """
        # print lists with mancala at each end

        MaxMancala, MinMancala, MaxPots, MinPots, turn = state

        reverseMin = MinPots[::-1]
        if turn == 0:
            player_turn = "MaxPlayer"
        else:
            player_turn = "MinPlayer"

        print(player_turn)
        print(" ", reverseMin)
        print(MinMancala, "                  ", MaxMancala)
        print(" ", MaxPots)

    def successors(self, state):  # mancala extend games
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]


if __name__ == '__main__':
    cs210_utils.cs210_mainstartup()