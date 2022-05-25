import itertools
from random import choices
import contextlib
import itertools
print('hello world!')

# TODO add more game states. investigate and fix the issue on why when Player does c3 c2, then the ai does a3 a2 every single time.
# Hard coded possible states.
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
    "state24": [[' ', 'i', ' '], [' ', 'i', 'O'], [' ', ' ', ' ']],
    "state25": [['i', 'i', 'i'], [' ', ' ', 'O'], ['O', 'O', ' ']],
    "state26": [['i', ' ', 'i'], [' ', 'O', 'O'], ['O', ' ', ' ']],
    "state27": [['i', ' ', 'i'], ['O', ' ', 'i'], [' ', 'O', ' ']],
    "state28": [['i', ' ', 'i'], [' ', 'O', 'i'], ['O', ' ', ' ']],
    "state29": [['i', ' ', 'i'], [' ', 'O', 'i'], ['O', ' ', ' ']],
    "state30": [['i', ' ', 'i'], ['O', 'i', 'i'], [' ', ' ', ' ']],
    "state31": [[' ', 'i', 'i'], ['i', ' ', 'O'], ['O', ' ', ' ']],
    "state32": [[' ', ' ', 'i'], ['O', 'O', 'O'], [' ', ' ', ' ']],
    "state33": [['i', ' ', 'i'], [' ', ' ', 'O'], ['O', ' ', ' ']],
    "state34": [['i', ' ', ' '], [' ', 'O', 'i'], [' ', ' ', ' ']],
    "state35": [['i', ' ', ' '], ['O', 'i', 'i'], [' ', ' ', ' ']],
    "state36": [[' ', 'i', 'i'], ['O', ' ', 'O'], ['O', ' ', ' ']],
    "state37": [['i', ' ', 'i'], [' ', 'O', 'O'], [' ', 'O', ' ']],
    "state38": [[' ', ' ', 'i'], ['O', 'O', 'O'], [' ', ' ', ' ']],

}
ai_moves = {
    # [[[orgin_row, orgin_column], [target_row, target_column], weight],[another move], ...]
    "state1": [[[0, 1], [1, 0], 1], [[0, 1], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state2": [[[0, 0], [1, 0], 1], [[0, 0], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state3": [[[0, 1], [1, 2], 1], [[0, 2], [1, 1], 1]],
    "state4": [[[0, 1], [1, 2], 1], [[1, 1], [2, 0], 1], [[1, 1], [2, 1], 1]],
    "state5": [[[0, 1], [1, 0], 1], [[0, 1], [1, 1], 1], [[0, 1], [1, 2], 1]],
    "state6": [[[0, 2], [1, 2], 1]],
    "state7": [[[0, 0], [1, 1], 1], [[0, 1], [1, 0], 1]],
    "state8": [[[0, 0], [1, 1], 1], [[0, 2], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state9": [[[0, 1], [1, 0], 1], [[1, 1], [2, 1], 1], [[1, 1], [2, 2], 1], [[0, 2], [1, 2], 1]],
    "state10": [[[0, 2], [1, 1], 1], [[0, 2], [1, 2], 1]],
    "state11": [[[0, 0], [1, 1], 1], [[0, 2], [1, 2], 1], [[1, 0], [2, 0], 1], [[0, 2], [1, 2], 1]],
    "state12": [[[1, 0], [2, 0], 1], [[1, 0], [2, 1], 1]],
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
    "state24": [[[0, 1], [1, 2], 1], [[1, 1], [2, 1], 1]],
    "state25": [[[0, 0], [1, 0], 1], [[0, 1], [1, 1], 1], [[0, 1], [1, 2], 1]],
    "state26": [[[0, 0], [1, 0], 1], [[0, 0], [1, 1], 1], [[0, 2], [1, 1], 1]],
    "state27": [[[1, 2], [2, 2], 1], [[1, 2], [2, 1], 1]],
    "state28": [[[0, 0], [1, 0], 1]],
    "state29": [[[0, 0], [1, 0], 1], [[0, 2], [1, 1], 1], [[1, 2], [2, 2], 1]],
    "state30": [[[1, 1], [2, 1], 1], [[1, 2], [2, 2], 1]],
    "state31": [[[0, 1], [1, 1], 1], [[0, 1], [1, 2], 1], [[0, 1], [1, 0], 1]],
    "state32": [[[0, 2], [1, 1], 1]],
    "state33": [[[0, 0], [1, 0], 1]],
    "state34": [[[0, 0], [1, 0], 1], [[1, 2], [2, 2], 1]],
    "state35": [[[1, 1], [2, 1], 1], [[1, 2], [2, 2], 1]],
    "state36": [[[0, 1], [1, 1], 1], [[0, 1], [1, 0], 1], [[0, 1], [1, 2], 1]],
    "state37": [[[0, 0], [1, 0], 1], [[0, 0], [1, 1], 1], [[0, 2], [1, 1], 1]],
    "state38": [[[0, 2], [1, 1], 1]],
}

# what the board looks like currently.
board = [['i', 'i', 'i'], [' ', ' ', ' '], ['O', 'O', 'O']]
# stored used moves. state      from       to
# example           ['state4', [0, 1], [1, 2]]
used_moves = []


def get_pos(board, piece):
    return [[i, j] for i, j in itertools.product(range(3), range(3)) if board[i][j] == piece]


def get_possible_moves(current_board, current_turn):
    # get the opposite.
    opposite = 'O' if current_turn == 'i' else 'i'
    # forward of Ai and forward of player is different.
    forward_offset = -1 if current_turn == 'O' else 1
    possible_moves = []
    # for every piece of the current turn/player, check if it can
    # A go forward; if it can, add it to possible_moves
    for piece in get_pos(board=current_board, piece=current_turn):
        piece[0] = piece[0] + forward_offset
        with contextlib.suppress(IndexError):
            if current_board[piece[0]][piece[1]] == ' ':
                possible_moves.append(piece)
    #print("forward", possible_moves)
    # B go left diagonally; if it can, add it to possible_moves
    for piece in get_pos(board=current_board, piece=current_turn):
        piece[0] += forward_offset
        piece[1] -= 1
        with contextlib.suppress(IndexError):
            if piece[1] < 0 or piece[0] < 0:
                continue
            if current_board[piece[0]][piece[1]] == opposite:
                possible_moves.append(piece)
    #print("left", possible_moves)
    # C go right diagonally; if it can, add it to possible_moves
    for piece in get_pos(board=current_board, piece=current_turn):
        piece[0] += forward_offset
        piece[1] += 1
        with contextlib.suppress(IndexError):
            if current_board[piece[0]][piece[1]] == opposite:
                possible_moves.append(piece)
    #print("right", possible_moves)
    return possible_moves


def print_board():
    print('\n')
    for i, k in itertools.product(range(1), board):
        print(*k, sep='  ')
    print('\n')


def reset_board():
    global board
    board = [['i', 'i', 'i'], [' ', ' ', ' '], ['O', 'O', 'O']]
#   pos[row, column]


def clear_used_moves():
    global used_moves
    used_moves = []


def get_position(target):
    if target.lower().startswith('a'):
        if target.endswith('1'):
            return [0, 0]
        elif target.endswith('2'):
            return [1, 0]
        else:
            return [2, 0]

    elif target.lower().startswith('b'):
        if target.endswith('1'):
            return [0, 1]
        elif target.endswith('2'):
            return [1, 1]
        else:
            return [2, 1]

    elif target.lower().startswith('c'):
        if target.endswith('1'):
            return [0, 2]
        elif target.endswith('2'):
            return [1, 2]
        else:
            return [2, 2]
    else:
        return False


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


def is_the_piece_there(piece_pos):
    return board[piece_pos[0]][piece_pos[1]] == 'O'


def validity(targ_pos, piece_pos):
    # check if it is a forward movement
    if is_it_forward(targ_pos, piece_pos) and is_it_same_column(
        targ_pos, piece_pos
    ) and is_the_piece_there(piece_pos):
        return what_is_on_it(targ_pos) == ' '

    # check if it is a diagonal movement
    elif is_it_forward(targ_pos, piece_pos) and not is_it_same_column(
        targ_pos, piece_pos
    ) and is_it_next_column(targ_pos, piece_pos) and is_the_piece_there(piece_pos):
        return what_is_on_it(targ_pos) == 'i'

    else:
        return False


def check_game_state(turn=None):
    # Anyone who reaches the other player's respective square first,
    # or takes out all of the opponent's pieces,
    # or makes the other player unable to make any valid moves in their turn is the winner\
    check = 'i' if turn == 'O' else 'O'
    stalemate = get_possible_moves(current_board=board, current_turn=check)
    if 'i' in board[2]:
        return 'i'
    elif 'O' in board[0]:
        return 'O'
    elif get_pos(board, 'O') == []:
        return 'i'
    elif get_pos(board, 'i') == []:
        return 'O'
    elif stalemate == []:
        return 'stalemate'
    else:
        return


def move_player(orgin=None, destination=None):
    orgin = get_position(orgin)
    destination = get_position(destination)
    # replace orgin with empty space
    board[orgin[0]][orgin[1]] = ' '
    # replace destination with O
    board[destination[0]][destination[1]] = 'O'


def roll():
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
    # records the move into a list. Used later to change the weights next game.
    used_moves.append([state, _from, to])


def change_weights(game_outcome, weight_change_lose=0, weight_change_win=1):
    # By default, it changes the weight by -1 if it loses. In matchbox terms, it removes the bead.
    # By default, it changes the weight by 0 if it wins.
    last_move = used_moves[-1]
    if game_outcome == 'O':
        moves = ai_moves.get(last_move[0])
        for index, move in enumerate(moves):
            if move[0] == last_move[1] and move[1] == last_move[2]:
                # print('moves before', moves)
                if move[2] < 0:
                    try:
                        previous_move = used_moves[-2]
                    except IndexError:
                        continue
                    previous_moves = ai_moves.get(previous_move[0])
                    for ind, pm in enumerate(previous_moves):
                        if pm[0] == previous_move[1] and pm[1] == previous_move[2]:
                            nw = pm[2] + weight_change_lose
                            ai_moves[previous_move[0]][ind] = [
                                previous_move[1], previous_move[2], nw]
                    return
                new_weight = move[2] + weight_change_lose
                ai_moves[last_move[0]][index] = [
                    last_move[1], last_move[2], new_weight]
                # print('moves after', moves)
    # same thing, but this is for when the AI wins.
    elif game_outcome == 'i':
        moves = ai_moves.get(last_move[0])
        for index, move in enumerate(moves):
            if move[0] == last_move[1] and move[1] == last_move[2]:
                new_weight = move[2] + weight_change_win
                ai_moves[last_move[0]][index] = [
                    last_move[1], last_move[2], new_weight]
    else:
        return


recorded_matches = []


def record_win(winner):
    if winner == 'i':
        recorded_matches.append('i')
    elif winner == 'O':
        recorded_matches.append('O')


def show_score():
    total_matches = len(recorded_matches)
    player_wins = 0
    ai_wins = 0
    for match in recorded_matches:
        if match == 'O':
            player_wins += 1
        else:
            ai_wins += 1
    try:
        player_ratio = (player_wins / total_matches) * 100
        ai_ratio = (ai_wins / total_matches) * 100
    except ZeroDivisionError:
        print('there are no scores yet!')
        return
    print("\n\nMatches played : ", total_matches, "\nPlayer wins:",
          player_wins, "\nAI wins: ", ai_wins, "\n Win ratio \n Player :", round(player_ratio), "%\n AI :", round(ai_ratio), "%\n\n")


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

    YOU ARE O

    type \'exit\' to leave the game
    type \'score\' to show the score so far
    type \'help\' to show the intructions again
""")


# game loop
def main_loop():
    turn = 0
    instructions()
    while True:
        print('Example - A3\nChoose a piece: ')
        piece = input()
        if piece == 'exit':
            break
        elif piece == 'score':
            show_score()
            continue
        elif piece == 'help':
            instructions()
            continue
        elif piece.startswith(('a', 'b', 'c', 'A', 'B', 'C')) is False:
            continue
        print('Example - A2\nto where: ')
        target = input()
        if target == 'exit':
            break
        elif target == 'score':
            show_score()
            continue
        elif target == 'help':
            instructions()
            continue
        elif target.startswith(('a', 'b', 'c', 'A', 'B', 'C')) is False:
            continue
        if piece == target:
            print('invalid input')
            continue
        elif len(piece) > 2 or len(target) > 2:
            print('invalid input')
            continue
        elif len(piece) == 0 or len(target) == 0:
            print('invalid input')
            continue
        elif not target or not piece:
            print("invalid input")
            continue
        else:
            if validity(targ_pos=get_position(target), piece_pos=get_position(piece)) != True:
                continue
            move_player(orgin=piece, destination=target)
            print_board()
            check_player = check_game_state(turn='O')
            if check_player == 'O' or check_player != 'O' and check_player == 'stalemate':
                print('\nYOU WON!\n')
                change_weights(game_outcome='O')
                reset_board()
                clear_used_moves()
                record_win('O')
                print_board()
                turn = 0
                continue
            ai_move()
            print_board()
            check_ai = check_game_state(turn='i')
            if check_ai == 'i' or check_ai != 'O' and check_ai == 'stalemate':
                print('\nAI won!\n')
                change_weights(game_outcome='i')
                reset_board()
                clear_used_moves()
                record_win('i')
                print_board()
                turn = 0
                continue
            turn += 1


main_loop()
