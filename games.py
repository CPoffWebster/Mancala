# ______________________________________________________________________________
# Minimax Search

def minimax_decision(state, game):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states"""

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):  # if the game is over
            return game.utility(state, player)
        v = -infinity
        for (a, s) in game.successors(state):
            v = max(v, min_value(s))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        for (a, s) in game.successors(state):
            v = min(v, max_value(s))
        return v

    # Body of minimax_decision starts here:
    action, state = argmax(game.successors(state),
                           lambda a, s: min_value(s))
    return action




def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):  # evaluate function
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(game, state)
        v = -infinity
        for (a, s) in game.successors(state):
            v = max(v, min_value(s, alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(game, state)
        v = infinity
        for (a, s) in game.successors(state):
            v = min(v, max_value(s, alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state, depth: depth > d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda game, state: game.utility(state, player))
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.legal_moves(state):
        # because we are assuming the root of the tree is a max node,
        # the first level of recursion is to min_value
        v = min_value(game.make_move(a, state), best_score, beta, 1)
        if v > best_score:  # Here we do the maximizing for the root explicitly
            best_score = v
            best_action = a
    return best_action


# ______________________________________________________________________________
# Players for Games

def query_player(game, state, display=True):
    "Make a move by querying standard input."
    if display: game.display(state)
    return num_or_str(input('Your move? '))


def query_player_py_exp(game, state, display=True):
    """
    Make a move by querying standard input. The input string is evaluated as a
    Python expression and returned
    """
    if display: game.display(state)
    return eval(input('Your move? '))  # eval as python, ask if legal


def random_player(game, state, display=True):
    "A player that chooses a legal move at random."
    if display: game.display(state)
    return random.choice(game.legal_moves(state))


def alphabeta_full_player(game, state, display=True):
    if display: game.display(state)
    return alphabeta_full_search(state, game)


def alphabeta_player(game, state, display=True):
    if display: game.display(state)
    return alphabeta_search(state, game)


def alphabeta_player2(game, state, eval_fn, display=True):  # eval_fn
    if display: game.display(state)
    return alphabeta_search(state, game, eval_fn=eval_fn)  # evaluate(game, state)


def evaluate(game, state):
    """Return a value from a given state
        This is used by the minimax algorithm in games.py"""

    return game.utility2(state)


def play_game2(game, named_players):
    """Play an n-person game where moves don't have to alternate.
    game is a Game instance;
    named_players is a tuple of pairs (player_name, player_function)
    player_functions take a game and a state and return a move to make (see above)"""

    # This is play_game with stuff added so players don't alternate only when it is there turn
    state = game.initial
    game_over = False
    while not game_over:
        named_player = named_players[game.to_move(state)]
        player_name, player_function = named_player
        if player_function == alphabeta_player2:
            move = player_function(game, state, evaluate)
        else:
            move = player_function(game, state)
        state = game.make_move(move, state)
        if game.terminal_test(state):
            print("final score: ", game.report(state))
            print("Game over - last move was by player %s" % (player_name,))
            game.display(state)
            game_over = True

    final = []
    for named_player in named_players:
        player_name, player_function = named_player
        final.append((player_name, game.utility(state, player_name)))
    return dict(final)
