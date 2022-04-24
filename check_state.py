import contextlib
import itertools


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
        if current_board[piece[0]][piece[1]] == ' ':
            possible_moves.append(piece)
    print("forward", possible_moves)
    # B go left diagonally; if it can, add it to possible_moves
    for piece in get_pos(board=current_board, piece=current_turn):
        piece[0] += forward_offset
        piece[1] -= 1
        if piece[1] < 0 or piece[0] < 0:
            continue
        if current_board[piece[0]][piece[1]] == opposite:
            possible_moves.append(piece)
    print("left", possible_moves)
    # C go right diagonally; if it can, add it to possible_moves
    for piece in get_pos(board=current_board, piece=current_turn):
        piece[0] += forward_offset
        piece[1] += 1
        with contextlib.suppress(IndexError):
            if current_board[piece[0]][piece[1]] == opposite:
                possible_moves.append(piece)
    print("right", possible_moves)
