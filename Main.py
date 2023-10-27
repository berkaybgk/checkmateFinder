
board_file = input()
opponent_file = input()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

board_inp = board_file
opponent_inp = opponent_file
fp_board = open(f"{board_inp}", "r")
fp_opp = open(f"{opponent_inp}", "r")

my_color = fp_board.readline().rstrip()
my_color_abrv = "W" if my_color == "white" else "B"
color_opp = "W" if my_color == "black" else "B"

opponent_moves_text = fp_opp.readlines()
for line_count in range(len(opponent_moves_text)):
    if opponent_moves_text[line_count] == "\n":
        opponent_moves_text.pop(line_count)
    else:
        opponent_moves_text[line_count] = opponent_moves_text[line_count].strip("\n")

opponent_moves_list = []
for line in opponent_moves_text:
    curr_line_list = line.split(",")
    opponent_moves_list.append(curr_line_list)
opponent_moves_list.append([])

board_cord = {"a1": "1 1", "a2": "1 2", "a3": "1 3", "a4": "1 4", "a5": "1 5", "a6": "1 6", "a7": "1 7", "a8": "1 8",
             "b1": "2 1", "b2": "2 2", "b3": "2 3", "b4": "2 4", "b5": "2 5", "b6": "2 6", "b7": "2 7", "b8": "2 8",
             "c1": "3 1", "c2": "3 2", "c3": "3 3", "c4": "3 4", "c5": "3 5", "c6": "3 6", "c7": "3 7", "c8": "3 8",
             "d1": "4 1", "d2": "4 2", "d3": "4 3", "d4": "4 4", "d5": "4 5", "d6": "4 6", "d7": "4 7", "d8": "4 8",
             "e1": "5 1", "e2": "5 2", "e3": "5 3", "e4": "5 4", "e5": "5 5", "e6": "5 6", "e7": "5 7", "e8": "5 8",
             "f1": "6 1", "f2": "6 2", "f3": "6 3", "f4": "6 4", "f5": "6 5", "f6": "6 6", "f7": "6 7", "f8": "6 8",
             "g1": "7 1", "g2": "7 2", "g3": "7 3", "g4": "7 4", "g5": "7 5", "g6": "7 6", "g7": "7 7", "g8": "7 8",
             "h1": "8 1", "h2": "8 2", "h3": "8 3", "h4": "8 4", "h5": "8 5", "h6": "8 6", "h7": "8 7", "h8": "8 8",
             }
board_cord_inv ={'1 1': 'a1', '1 2': 'a2', '1 3': 'a3', '1 4': 'a4', '1 5': 'a5', '1 6': 'a6', '1 7': 'a7', '1 8': 'a8',
                '2 1': 'b1', '2 2': 'b2', '2 3': 'b3', '2 4': 'b4', '2 5': 'b5', '2 6': 'b6', '2 7': 'b7', '2 8': 'b8',
                '3 1': 'c1', '3 2': 'c2', '3 3': 'c3', '3 4': 'c4', '3 5': 'c5', '3 6': 'c6', '3 7': 'c7', '3 8': 'c8',
                '4 1': 'd1', '4 2': 'd2', '4 3': 'd3', '4 4': 'd4', '4 5': 'd5', '4 6': 'd6', '4 7': 'd7', '4 8': 'd8',
                '5 1': 'e1', '5 2': 'e2', '5 3': 'e3', '5 4': 'e4', '5 5': 'e5', '5 6': 'e6', '5 7': 'e7', '5 8': 'e8',
                '6 1': 'f1', '6 2': 'f2', '6 3': 'f3', '6 4': 'f4', '6 5': 'f5', '6 6': 'f6', '6 7': 'f7', '6 8': 'f8',
                '7 1': 'g1', '7 2': 'g2', '7 3': 'g3', '7 4': 'g4', '7 5': 'g5', '7 6': 'g6', '7 7': 'g7', '7 8': 'g8',
                '8 1': 'h1', '8 2': 'h2', '8 3': 'h3', '8 4': 'h4', '8 5': 'h5', '8 6': 'h6', '8 7': 'h7', '8 8': 'h8'
                  }
board_dic = {"a1": "empty", "a2": "empty", "a3": "empty", "a4": "empty", "a5": "empty", "a6": "empty", "a7": "empty", "a8": "empty",
             "b1": "empty", "b2": "empty", "b3": "empty", "b4": "empty", "b5": "empty", "b6": "empty", "b7": "empty", "b8": "empty",
             "c1": "empty", "c2": "empty", "c3": "empty", "c4": "empty", "c5": "empty", "c6": "empty", "c7": "empty", "c8": "empty",
             "d1": "empty", "d2": "empty", "d3": "empty", "d4": "empty", "d5": "empty", "d6": "empty", "d7": "empty", "d8": "empty",
             "e1": "empty", "e2": "empty", "e3": "empty", "e4": "empty", "e5": "empty", "e6": "empty", "e7": "empty", "e8": "empty",
             "f1": "empty", "f2": "empty", "f3": "empty", "f4": "empty", "f5": "empty", "f6": "empty", "f7": "empty", "f8": "empty",
             "g1": "empty", "g2": "empty", "g3": "empty", "g4": "empty", "g5": "empty", "g6": "empty", "g7": "empty", "g8": "empty",
             "h1": "empty", "h2": "empty", "h3": "empty", "h4": "empty", "h5": "empty", "h6": "empty", "h7": "empty", "h8": "empty",
             }

board_rest = fp_board.readlines()
for line_num in range(len(board_rest)):
    board_rest[line_num] = board_rest[line_num].strip()

for piece in board_rest:
    location = piece.split()[1]
    board_dic[location] = piece.split()[0]


def board_print(dic_of_board):
    print()
    print("    A    B    C    D    E    F    G    H  |")
    for y in range(8):
        print(f"{8-y} | ", end="")
        for key, value in dic_of_board.items():
            if key.endswith(str(8-y)):
                if value == "empty":
                    print(f"-- | ", end="")
                else:
                    print(f"{value} | ", end="")
        print()
        print("------------------------------------------|")
    print()


def make_move(dic_board, coords_alpha):

    main_board = dic_board.copy()
    coord_list = coords_alpha.split()
    temp_piece = main_board[coord_list[0]]
    main_board[coord_list[0]] = "empty"
    main_board[coord_list[-1]] = temp_piece
    return main_board


def does_opp_check(current_board_dic, turn_color):
    global board_cord
    global board_cord_inv
    global board_dic

    opposite_turn_color = "B" if turn_color == "W" else "W"
    kings_loc = "unknown"

    for place, piece in current_board_dic.items():
        if piece == f"{turn_color}" + f"K":
            kings_loc = place
            break
    for elements in piece_moves(current_board_dic, opposite_turn_color, "control"):
        if elements[-2:] == kings_loc:
            return True
    return False


def piece_moves(dic_board, color_side, command):
    global board_cord
    global board_cord_inv
    opp_color_abrv = "B" if color_side == "W" else "W"
    moves_list = []

    for place, piece in dic_board.items():
        ################################################################################################################
        if piece.startswith(color_side) and piece.endswith("R"):  # if the piece is a rook and has the turn
            pos_numeric_initial = board_cord[place]
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) > 7):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    if command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"
                    if int(pos_numeric_varies[0]) + 1 > 8:
                        break
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    if command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"
                    if int(pos_numeric_varies[0]) - 1 == 0:
                        break
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[-1]) > 7):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    if command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"
                    if int(pos_numeric_varies[-1]) + 1 > 8:
                        break
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[-1]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    if command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"
                    if int(pos_numeric_varies[-1]) - 1 == 0:
                        break
        ################################################################################################################
        elif piece.startswith(color_side) and piece.endswith("N"):  # if the piece is a knight and has the turn
            pos_numeric = board_cord[place]
            altered_board = board_dic.copy()
            if (1 <= int(pos_numeric[0]) + 1 <= 8) and (1 <= int(pos_numeric[-1]) - 2 <= 8):
                temp_pos = f"{int(pos_numeric[0]) + 1} " + f"{int(pos_numeric[-1]) - 2}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) + 1} " + f"{int(pos_numeric[-1]) - 2}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) + 2 <= 8) and (1 <= int(pos_numeric[-1]) - 1 <= 8):
                temp_pos = f"{int(pos_numeric[0]) + 2} " + f"{int(pos_numeric[-1]) - 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) + 2} " + f"{int(pos_numeric[-1]) - 1}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) + 2 <= 8) and (1 <= int(pos_numeric[-1]) + 1 <= 8):
                temp_pos = f"{int(pos_numeric[0]) + 2} " + f"{int(pos_numeric[-1]) + 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) + 2} " + f"{int(pos_numeric[-1]) + 1}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) + 1 <= 8) and (1 <= int(pos_numeric[-1]) + 2 <= 8):
                temp_pos = f"{int(pos_numeric[0]) + 1} " + f"{int(pos_numeric[-1]) + 2}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) + 1} " + f"{int(pos_numeric[-1]) + 2}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) - 1 <= 8) and (1 <= int(pos_numeric[-1]) - 2 <= 8):
                temp_pos = f"{int(pos_numeric[0]) - 1} " + f"{int(pos_numeric[-1]) - 2}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) - 1} " + f"{int(pos_numeric[-1]) - 2}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) - 2 <= 8) and (1 <= int(pos_numeric[-1]) - 1 <= 8):
                temp_pos = f"{int(pos_numeric[0]) - 2} " + f"{int(pos_numeric[-1]) - 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) - 2} " + f"{int(pos_numeric[-1]) - 1}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) - 2 <= 8) and (1 <= int(pos_numeric[-1]) + 1 <= 8):
                temp_pos = f"{int(pos_numeric[0]) - 2} " + f"{int(pos_numeric[-1]) + 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) - 2} " + f"{int(pos_numeric[-1]) + 1}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
            temp_pos = pos_numeric
            altered_board = dic_board.copy()
            if (1 <= int(pos_numeric[0]) - 1 <= 8) and (1 <= int(pos_numeric[-1]) + 2 <= 8):
                temp_pos = f"{int(pos_numeric[0]) - 1} " + f"{int(pos_numeric[-1]) + 2}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                temp_move_alpha = board_cord_inv[str(pos_numeric)] + " " + temp_pos_alpha
                altered_board = make_move(dic_board, temp_move_alpha)
                if dic_board[temp_pos_alpha] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric[0]) - 1} " + f"{int(pos_numeric[-1]) + 2}"]].startswith(opp_color_abrv):
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
        ################################################################################################################
        elif piece.startswith(color_side) and piece.endswith("B"):  # if the piece is a bishop and has the turn
            pos_numeric_initial = board_cord[place]
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 8) and not (int(pos_numeric_initial[-1]) == 8):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"
                    if (int(pos_numeric_varies[0]) == 8) or (int(pos_numeric_varies[-1]) == 8):
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 1) and not (int(pos_numeric_initial[-1]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"
                    if (int(pos_numeric_varies[0]) == 1) or (int(pos_numeric_varies[-1]) == 1):
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 1) and not (int(pos_numeric_initial[-1]) == 8):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"
                    if (int(pos_numeric_varies[0]) == 1) or (int(pos_numeric_varies[-1]) == 8):
                        break
            altered_board = dic_board.copy()
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 8) and not (int(pos_numeric_initial[-1]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"
                    if (int(pos_numeric_varies[0]) == 8) or (int(pos_numeric_varies[-1]) == 1):
                        break
        ################################################################################################################
        elif piece.startswith(color_side) and piece.endswith("Q"):  # if the piece is a queen and has the turn
            pos_numeric_initial = board_cord[place]
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) >= 8):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"
                    if int(pos_numeric_varies[0]) + 1 > 7:
                        break
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) == 1):
                while (dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"]] == "empty") or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"
                    if int(pos_numeric_varies[0]) - 1 == 0:
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[-1]) > 7):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"
                    if int(pos_numeric_varies[-1]) + 1 > 7:
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[-1]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"
                    if int(pos_numeric_varies[-1]) - 1 == 0:
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 8) and not (int(pos_numeric_initial[-1]) == 8):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"
                    if (int(pos_numeric_varies[0]) == 8) or (int(pos_numeric_varies[-1]) == 8):
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 1) and not (int(pos_numeric_initial[-1]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"
                    if (int(pos_numeric_varies[0]) == 1) or (int(pos_numeric_varies[-1]) == 1):
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 1) and not (int(pos_numeric_initial[-1]) == 8):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"
                    if (int(pos_numeric_varies[0]) == 1) or (int(pos_numeric_varies[-1]) == 8):
                        break
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 8) and not (int(pos_numeric_initial[-1]) == 1):
                while dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"]] == "empty" or dic_board[board_cord_inv[f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"]].startswith(opp_color_abrv):
                    temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"
                    temp_pos_alpha = board_cord_inv[temp_pos]
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if command == "main":
                        if not does_opp_check(altered_board, color_side):
                            moves_list.append(temp_move_alpha)
                    elif command == "control":
                        moves_list.append(temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                        break
                    pos_numeric_varies = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"
                    if (int(pos_numeric_varies[0]) == 8) or (int(pos_numeric_varies[-1]) == 1):
                        break
        ################################################################################################################
        elif piece.startswith(color_side) and piece.endswith("P"):  # if the piece is a pawn and has the turn
            pos_numeric_initial = board_cord[place]
            pos_numeric_varies = pos_numeric_initial
            if piece.startswith("W"):
                if not (int(pos_numeric_initial[-1]) == 8):
                    if place.endswith("2"):
                        temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 2}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha] == "empty":
                            if dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"]] == "empty":
                                if command == "main":
                                    if not does_opp_check(altered_board, color_side):
                                        moves_list.append(temp_move_alpha)
                                if command == "control":
                                    moves_list.append(temp_move_alpha)
                    pos_numeric_varies = pos_numeric_initial
                    altered_board = dic_board.copy()
                    if int(pos_numeric_varies[-1]) <= 7:
                        temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha] == "empty":
                            if command == "main":
                                if not does_opp_check(altered_board, color_side):
                                    moves_list.append(temp_move_alpha)
                            if command == "control":
                                moves_list.append(temp_move_alpha)
                    pos_numeric_varies = pos_numeric_initial
                    altered_board = dic_board.copy()
                    if int(pos_numeric_varies[0]) <= 7 and int(pos_numeric_varies[-1]) <= 7:
                        temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                            if command == "main":
                                if not does_opp_check(altered_board, color_side):
                                    moves_list.append(temp_move_alpha)
                        if command == "control":
                            moves_list.append(temp_move_alpha)
                    pos_numeric_varies = pos_numeric_initial
                    altered_board = dic_board.copy()
                    if (int(pos_numeric_varies[0]) > 1) and (int(pos_numeric_varies[-1]) <= 7):
                        temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                            if command == "main":
                                if not does_opp_check(altered_board, color_side):
                                    moves_list.append(temp_move_alpha)
                        if command == "control":
                            moves_list.append(temp_move_alpha)
            altered_board = dic_board.copy()
            if piece.startswith("B"):
                if not (int(pos_numeric_initial[-1]) == 1):
                    if place.endswith("7"):
                        temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 2}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha] == "empty" or dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                            if dic_board[board_cord_inv[f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"]] == "empty":
                                if command == "main":
                                    if not does_opp_check(altered_board, color_side):
                                        moves_list.append(temp_move_alpha)
                                if command == "control":
                                    moves_list.append(temp_move_alpha)
                    pos_numeric_varies = pos_numeric_initial
                    altered_board = dic_board.copy()
                    if int(pos_numeric_varies[-1]) <= 7:
                        temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha] == "empty":
                            if command == "main":
                                if not does_opp_check(altered_board, color_side):
                                    moves_list.append(temp_move_alpha)
                                if command == "control":
                                    moves_list.append(temp_move_alpha)
                    pos_numeric_varies = pos_numeric_initial
                    altered_board = dic_board.copy()
                    if int(pos_numeric_varies[0]) >= 2 and int(pos_numeric_varies[-1]) >= 2:
                        temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                            if command == "main":
                                if not does_opp_check(altered_board, color_side):
                                    moves_list.append(temp_move_alpha)
                        if command == "control":
                            moves_list.append(temp_move_alpha)
                    pos_numeric_varies = pos_numeric_initial
                    altered_board = dic_board.copy()
                    if (int(pos_numeric_varies[0]) <= 7) and (int(pos_numeric_varies[-1]) >= 1):
                        temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"
                        temp_pos_alpha = board_cord_inv[temp_pos]
                        temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                        altered_board = make_move(dic_board, temp_move_alpha)
                        if dic_board[temp_pos_alpha].startswith(opp_color_abrv):
                            if command == "main":
                                if not does_opp_check(altered_board, color_side):
                                    moves_list.append(temp_move_alpha)
                        if command == "control":
                            moves_list.append(temp_move_alpha)
        ################################################################################################################
        elif piece.startswith(color_side) and piece.endswith("K"):  # If the piece is king and has the turn
            pos_numeric_initial = board_cord[place]
            pos_numeric_varies = pos_numeric_initial
            if not (int(pos_numeric_initial[0]) == 8):
                temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1])}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[temp_pos_alpha].startswith(my_color_abrv):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) == 1):
                temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1])}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[-1]) == 8):
                temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) + 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[-1]) == 1):
                temp_pos = f"{int(pos_numeric_varies[0])} {int(pos_numeric_varies[-1]) - 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) < 2) and not (int(pos_numeric_initial[-1]) < 2):
                temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) - 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) > 7) and not (int(pos_numeric_initial[-1]) > 7):
                temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) + 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) < 2) and not (int(pos_numeric_initial[-1]) > 7):
                temp_pos = f"{int(pos_numeric_varies[0]) - 1} {int(pos_numeric_varies[-1]) + 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()
            if not (int(pos_numeric_initial[0]) > 7) and not (int(pos_numeric_initial[-1]) < 2):
                temp_pos = f"{int(pos_numeric_varies[0]) + 1} {int(pos_numeric_varies[-1]) - 1}"
                temp_pos_alpha = board_cord_inv[temp_pos]
                if not dic_board[board_cord_inv[temp_pos]].startswith(color_side):
                    temp_move_alpha = board_cord_inv[str(pos_numeric_initial)] + " " + temp_pos_alpha
                    altered_board = make_move(dic_board, temp_move_alpha)
                    if dic_board[temp_pos_alpha].startswith(opp_color_abrv) or dic_board[temp_pos_alpha] == "empty":
                        if command == "main":
                            if not does_opp_check(altered_board, color_side):
                                moves_list.append(temp_move_alpha)
                        elif command == "control":
                            moves_list.append(temp_move_alpha)
            pos_numeric_varies = pos_numeric_initial
            altered_board = dic_board.copy()

    return moves_list

moves_wbp = []

def main_func(dic_board, my_color, opponent_possible_moves):
    global board_cord
    global board_cord_inv
    global opponent_moves_list
    global moves_wbp
    opponents_color = "B" if my_color == "W" else "W"

    my_initial_moves = piece_moves(dic_board, my_color, "main")
    altered_board_pivot = dic_board

    if opponent_possible_moves[0] == []:  # if opponent has made his last move
        my_last_moves = piece_moves(dic_board, my_color, "main")
        last_altered = dic_board.copy()
        for last_move in my_last_moves:
            altered_board = make_move(last_altered, last_move)
            opponents_possiblities = piece_moves(altered_board, opponents_color, "main")
            if opponents_possiblities == []:
                if not last_move in moves_wbp:
                    moves_wbp.append(last_move)

    else:
        for my_move in my_initial_moves:
            altered_board = make_move(altered_board_pivot, my_move)
            opp_response = piece_moves(altered_board, opponents_color, "main")
            altered_board_pivot_two = altered_board
            if len(opp_response) == len(opponent_possible_moves[0]) and opponent_possible_moves[0][0] in opp_response:
                altered_board = make_move(altered_board_pivot_two, opponent_possible_moves[0][0])
                moves_wbp.append(my_move)
                main_func(altered_board, my_color, opponent_possible_moves[1:])


board_print(board_dic)

main_func(board_dic, my_color_abrv, opponent_moves_list)
for move in moves_wbp:
    print(move)

fp_board.close()
fp_opp.close()

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

