import itertools
from random import choices
from check_state import get_possible_moves, get_pos
print('hello world!')

# Hard coded possible states.
# if board state is == gamestate key value, get key to get value moves. then we could tweak the list values of moves?
game_states = {
    # state0 is the starting state.
    "state0": [['i', 'i', 'i'], [' ', ' ', ' '], ['O', 'O', 'O']],
    "state1": [['i', 'i', 'i'], ['O', ' ', ' '], [' ', 'O', 'O']],
    "state2": [['i', 'i', 'i'], [' ', 'O', ' '], ['O', ' ', 'O']],
    "state3": [[' ', 'i', 'i'], ['i', 'O', 'O'], ['O', ' ', ' ']],
    "state4": [[' ', 'i', 'i'], [' ', 'i', 'O'], ['O', ' ', ' ']],
    "state5": [['i', 'i', ' '], ['O', ' ', 'O'], [' ', ' ', 'O']],
    "state6": [['i', ' ', 'i'], ['O', ' ', ' '], [' ', ' ', 'O']],
    "state7": [['i', 'i', ' '], ['O', 'O', 'i'], [' ', ' ', 'O']],
    "state8": [['i', ' ', 'i'], ['O', 'O', ' '], [' ', 'O', ' ']],
    "state9": [[' ', 'i', 'i'], ['O', 'i', ' '], [' ', ' ', 'O']],
    "state10": [[' ', 'i', 'i'], [' ', 'O', ' '], [' ', ' ', 'O']],
    "state11": [['i', ' ', 'i'], ['i', 'O', ' '], [' ', ' ', 'O']],
    "state12": [['i', ' ', 'i'], ['i', ' ', 'O'], [' ', 'O', ' ']],
    "state13": [[' ', 'i', 'i'], [' ', 'O', ' '], ['O', ' ', ' ']],
    "state14": [[' ', 'i', ' '], ['i', 'O', 'O'], [' ', ' ', ' ']],
    "state15": [['i', ' ', ' '], ['i', 'O', ' '], [' ', ' ', ' ']],
    "state16": [['i', ' ', ' '], ['i', 'i', 'O'], [' ', ' ', ' ']],
    "state17": [['i', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']],
    "state18": [[' ', ' ', 'i'], ['O', 'i', 'i'], [' ', ' ', ' ']],
    "state19": [[' ', 'i', ' '], ['O', 'i', ' '], [' ', ' ', ' ']],
    "state20": [[' ', ' ', 'i'], ['i', 'O', ' '], [' ', ' ', ' ']],
    "state21": [[' ', ' ', 'i'], [' ', 'O', 'i'], [' ', ' ', ' ']],
    "state22": [[' ', 'i', ' '], ['O', 'O', 'i'], [' ', ' ', ' ']],
    "state23": [[' ', ' ', 'i'], ['i', 'i', 'O'], [' ', ' ', ' ']],
    "state24": [[' ', 'i', ' '], [' ', 'i', 'O'], [' ', ' ', ' ']]
}
# coordinate reference
#       0   1   2
#   0   i   i   i
#   1
#   2   O   O   O
ai_moves = {
    # [[[orgin_row, orgin_column], [target_row, target_column], weight],[another move], ...]
    "state1": [[[0, 1], [1, 0], 1], [[0, 1], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state2": [[[0, 0], [1, 0], 1], [[0, 0], [0, 1], 1]],
    "state3": [[[0, 1], [1, 2], 1], [[0, 2], [1, 1], 1]],
    "state4": [[[0, 1], [1, 2], 1], [[1, 1], [2, 0], 1], [[1, 1], [2, 1], 1]],
    "state5": [[[0, 1], [1, 0], 1], [[0, 1], [1, 1], 1], [[0, 1], [1, 2], 1]],
    "state6": [[[0, 2], [1, 2], 1]],
    "state7": [[[0, 0], [1, 1], 1], [[0, 0], [1, 0], 1]],
    "state8": [[[0, 0], [1, 1], 1], [[0, 2], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state9": [[[0, 1], [1, 0], 1], [[1, 1], [2, 1], 1], [[1, 1], [2, 2], 1], [[0, 2], [1, 2], 1]],
    "state10": [[[0, 2], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state11": [[[0, 0], [1, 1], 1], [[0, 2], [1, 2], 1], [[1, 0], [2, 0], 1], [[0, 2], [1, 2], 1]],
    "state12": [[[0, 1], [2, 0], 1], [[0, 1], [2, 1], 1]],
    "state13": [[[0, 2], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state14": [[[1, 0], [2, 0], 1], [[0, 1], [1, 2], 1]],
    "state15": [[[0, 0], [1, 1], 1], [[1, 0], [2, 0], 1]],
    "state16": [[[1, 0], [2, 0], 1], [[1, 1], [2, 1], 1]],
    "state17": [[[0, 0], [1, 1], 1]],
    "state18": [[[1, 1], [2, 1], 1], [[1, 2], [2, 2], 1]],
    "state19": [[[0, 1], [1, 0], 1], [[1, 1], [2, 1], 1]],
    "state20": [[[1, 0], [2, 0], 1], [[0, 2], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state21": [[[0, 2], [1, 1], 1], [[1, 2], [2, 2], 1]],
    "state22": [[[0, 1], [1, 0], 1], [[1, 2], [2, 2], 1]],
    "state23": [[[1, 0], [2, 0], 1], [[1, 1], [2, 1], 1]],
    "state24": [[[0, 1], [1, 2], 1], [[1, 1], [2, 1], 1]]
}

# what the board looks like currently.
board = [['i', 'i', 'i'], [' ', ' ', ' '], ['O', 'O', 'O']]
# stored used moves. state      from       to
# example           ['state4', [0, 1], [1, 2]]
used_moves = []


def reset_board():
    board = [['i', 'i', 'i'], [' ', ' ', ' '], ['O', 'O', 'O']]


def print_board():
    for i, k in itertools.product(range(1), board):
        print(k)
    print('\n')

#   pos[row][column]


def get_position(target):
    if len(target) > 2:
        return False
    if target.endswith('1'):
        if target.lower().startswith('a'):
            target_pos = [0, 0]
        elif target.lower().startswith('b'):
            target_pos = [0, 1]
        else:
            target_pos = [0, 2]

    elif target.endswith('2'):
        if target.lower().startswith('a'):
            target_pos = [1, 0]
        elif target.lower().startswith('b'):
            target_pos = [1, 1]
        else:
            target_pos = [1, 2]
    elif target.endswith('3'):
        if target.lower().startswith('a'):
            target_pos = [2, 0]
        elif target.lower().startswith('b'):
            target_pos = [2, 1]
        else:
            target_pos = [2, 2]
    else:
        return False
    return target_pos


def is_it_forward(targ_pos, piece_pos):
    piece_row = piece_pos[0]
    targ_row = targ_pos[0]
    return (piece_row - 1) == targ_row


def is_it_same_column(targ_pos, piece_pos):
    return piece_pos[1] == targ_pos[1]


def what_is_on_it(targ_pos):
    return board[targ_pos[0]][targ_pos[1]]


def is_it_next_column(targ_pos, piece_pos):
    return (piece_pos[1] - 1) == targ_pos[1] or (piece_pos[1] + 1) == targ_pos[1]


def validity(targ_pos, piece_pos):
    # check if it is a forward movement and if it is on the same column
    if is_it_forward(targ_pos, piece_pos) and is_it_same_column(
        targ_pos, piece_pos
    ):
        # check if the space is empty
        return what_is_on_it(targ_pos) == ' '
        #       if same column, check if space is empty; if true; forward = True : else; return False

    # check if it is a diagonal movement
    elif is_it_forward(targ_pos, piece_pos) and not is_it_same_column(
        targ_pos, piece_pos
    ) and is_it_next_column(targ_pos, piece_pos):
        #   check if it the piece is opposite to the current player piece.
        return what_is_on_it(targ_pos) == 'i'
    #       if valid; return eat = True: else; return False
    # if it is neither: return False
    else:
        return False


def check_game_state(board, turn):
    # Anyone who reaches the other player's respective square first,
    # or takes out all of the opponent's pieces,
    # or makes the other player unable to make any valid moves in their turn is the winner
    if turn == 'i':
        if 'i' in board[2]:
            return 'i'
        elif get_pos(board, piece='i') is None:
            return 'i'
        elif get_possible_moves(current_board=board, current_turn=turn) is None:
            return 'stalemate'
    elif turn == 'O':
        if 'O' in board[0]:
            return 'O'
        elif get_pos(board, piece='O') is None:
            return 'O'
    else:
        print("should not happen.")


def move_player(orgin, destination):
    orgin = get_position(orgin)
    destination = get_position(destination)
    # replace orgin with empty space
    board[orgin[0]][orgin[1]] = ' '
    # replace destination with O
    board[destination[0]][destination[1]] = 'O'
    print_board()


def roll(board=board):
    try:
        for key, value in game_states.items():
            if board == value:
                state = key
    except UnboundLocalError:
        return
    # returns None if state = "state0"
    moves = ai_moves.get(state)
    weights = []
    coordinates = []
    for move in moves:
        weight = move[2]
        weights.append(weight)
        bead = move
        bead_orgin = bead[0]
        bead_destination = bead[1]
        coordinate = bead_orgin, bead_destination
        coordinates.append(coordinate)
    chosen_choices = choices(population=coordinates, weights=weights, k=1)
    _from = chosen_choices[0][0]
    to = chosen_choices[0][1]
    return state, _from, to


def ai_move():
    state, _from, to = roll()
    board[_from[0]][_from[1]] = ' '
    board[to[0]][to[1]] = 'i'
    print_board()
    # records the move into a list. Used later to change the weights next game.
    used_moves.append([state, _from, to])


def change_weights(game_outcome, weight_change_lose=-1, weight_change_win=0):
    # if player (O) won, it activates.
    # By default, it changes the weight by -1 if it loses. In matchbox terms, it removes the bead.
    # By default, it changes the weight by 0 if it wins.
    if game_outcome == 'O':
        for used_move in used_moves:
            used_state = used_move[0]
            # print(used_state)
            used_from = used_move[1]
            used_to = used_move[2]
            moves = ai_moves.get(used_state)
            #print("BEFORE", ai_moves.get(used_state))
            for index, move in enumerate(moves):
                if move[0] == used_from and move[1] == used_to:
                    new_weight = move[2] + weight_change_lose
                    ai_moves[used_state][index] = [
                        used_from, used_to, new_weight]
            #print("AFTER", ai_moves.get(used_state))
    # same thing, but this is for when the AI wins.
    elif game_outcome == 'i':
        for used_move in used_moves:
            used_state = used_move[0]
            # print(used_state)
            used_from = used_move[1]
            used_to = used_move[2]
            moves = ai_moves.get(used_state)
            #print("BEFORE", ai_moves.get(used_state))
            for index, move in enumerate(moves):
                if move[0] == used_from and move[1] == used_to:
                    new_weight = move[2] + weight_change_win
                    ai_moves[used_state][index] = [
                        used_from, used_to, new_weight]
            #print("AFTER", ai_moves.get(used_state))
    else:
        return


recorded_matches = []


def record_win(winner):
    if winner == 'i':
        recorded_matches.append('i')
    elif winner == 'O':
        recorded_matches.append('O')


def instructions():
    print('The goal of each player is to advance one of their pawns to the opposite end of the board,\n or to prevent the other player from moving')
    print("""
Format is:
    Letter-Number
    Example, A3 

    The board looks like this.

            A   B   C
        1   i   i   i
        2
        3   O   O   O

    YOU ARE 'O'
""")


#format is letter, number


def main_loop(running=True):
    instructions()
    print("type \'exit\' to leave the game.")
    while running:
        print('It is your turn')
        piece = input('Example - A3\nChoose a piece: ')
        if piece == 'exit':
            break
        target = input('Example - A2\nto where: ')
        if target == 'exit':
            break
        if validity(targ_pos=get_position(target), piece_pos=get_position(piece)) == True:
            move_player(target, piece)
            check_if_player_won = check_game_state(board=board, turn='O')
            if check_if_player_won == 'O':
                print('you won!')
                change_weights(game_outcome='O')
                # do something to reset the board and do a show_wins()
                record_win('O')
                continue
            ai_move()
            check_if_ai_won = check_game_state(board=board, turn='i')
            if check_if_ai_won == 'i':
                print('ai won!')
                change_weights(game_outcome='i')
                # do something to reset the board and do a show_wins()
                record_win('i')


main_loop()
