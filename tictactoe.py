user_input = '         '
matrix = [[user_input[6], user_input[3], user_input[0]],
          [user_input[7], user_input[4], user_input[1]],
          [user_input[8], user_input[5], user_input[2]]]


def matrix_print():
    print("---------")
    print("|", (matrix[0][2]), (matrix[1][2]), (matrix[2][2]), "|")
    print("|", (matrix[0][1]), (matrix[1][1]), (matrix[2][1]), "|")
    print("|", (matrix[0][0]), (matrix[1][0]), (matrix[2][0]), "|")
    print("---------")


move_counter = 0
x_wins = 0
o_wins = 0
result_draw = 0
result_impossible = 0
game_not_finished = 0
amount_of_o = 0
amount_of_x = 0

matrix_print()

while True:
    column_input, row_input = input('Enter the coordinates: ').split()
    for element in matrix:
        if element == 'X':
            amount_of_x = int(amount_of_x) + 1
        elif element == 'O':
            amount_of_o = int(amount_of_o) + 1
    if column_input.isalpha() or row_input.isalpha() is True:
        print('You should enter numbers!')
        continue
    elif 3 < int(column_input) or int(row_input) < 1:
        print('Coordinates should be from 1 to 3!')
        continue
    elif matrix[int(column_input) - 1][int(row_input) - 1] == 'X' or matrix[int(column_input) - 1][int(row_input) - 1] == 'O':
        print('This cell is occupied! Choose another one!')
        continue
    else:
        move_counter += 1
        if move_counter % 2 != 0:
            matrix[int(column_input) - 1][int(row_input) - 1] = 'X'
            matrix_print()
            if ((matrix[0][2]) == 'X' and (matrix[1][2]) == 'X' and (matrix[2][2]) == 'X')\
               or ((matrix[0][1]) == 'X' and (matrix[1][1]) == 'X' and (matrix[2][1]) == 'X')\
               or ((matrix[0][0]) == 'X' and (matrix[1][0]) == 'X' and (matrix[2][0]) == 'X')\
               or ((matrix[0][2]) == 'X' and (matrix[0][1]) == 'X' and (matrix[0][0]) == 'X')\
               or ((matrix[1][2]) == 'X' and (matrix[1][1]) == 'X' and (matrix[1][0]) == 'X')\
               or ((matrix[2][2]) == 'X' and (matrix[2][1]) == 'X' and (matrix[2][0]) == 'X')\
               or ((matrix[0][2]) == 'X' and (matrix[1][1]) == 'X' and (matrix[2][0]) == 'X')\
               or ((matrix[2][2]) == 'X' and (matrix[1][1]) == 'X' and (matrix[0][0]) == 'X'):
                x_wins = 1
                pass
            elif ((matrix[0][2]) == 'O' and (matrix[1][2]) == 'O' and (matrix[2][2]) == 'O')\
                or ((matrix[0][1]) == 'O' and (matrix[1][1]) == 'O' and (matrix[2][1]) == 'O')\
                or ((matrix[0][0]) == 'O' and (matrix[1][0]) == 'O' and (matrix[2][0]) == 'O')\
                or ((matrix[0][2]) == 'O' and (matrix[0][1]) == 'O' and (matrix[0][0]) == 'O')\
                or ((matrix[1][2]) == 'O' and (matrix[1][1]) == 'O' and (matrix[1][0]) == 'O')\
                or ((matrix[2][2]) == 'O' and (matrix[2][1]) == 'O' and (matrix[2][0]) == 'O')\
                or ((matrix[0][2]) == 'O' and (matrix[1][1]) == 'O' and (matrix[2][0]) == 'O')\
                or ((matrix[2][2]) == 'O' and (matrix[1][1]) == 'O' and (matrix[0][0]) == 'O'):
                o_wins = 1
                pass
            elif (x_wins == 1 and o_wins == 1) or (abs(int(amount_of_o) - int(amount_of_x)) >= 2):
                result_impossible = 1
                pass
            elif (x_wins == 0) and (o_wins == 0) and move_counter == 9:
                result_draw = 1
                pass
            if result_impossible == 1:
                print('Impossible')
                continue
            elif result_draw == 1:
                print('Draw')
                break
            elif x_wins == 1:
                print('X wins')
                break
            elif o_wins == 1:
                print('O wins')
                break
            continue
        else:
            matrix[int(column_input) - 1][int(row_input) - 1] = 'O'
            matrix_print()
            if ((matrix[0][2]) == 'X' and (matrix[1][2]) == 'X' and (matrix[2][2]) == 'X')\
               or ((matrix[0][1]) == 'X' and (matrix[1][1]) == 'X' and (matrix[2][1]) == 'X')\
               or ((matrix[0][0]) == 'X' and (matrix[1][0]) == 'X' and (matrix[2][0]) == 'X')\
               or ((matrix[0][2]) == 'X' and (matrix[0][1]) == 'X' and (matrix[0][0]) == 'X')\
               or ((matrix[1][2]) == 'X' and (matrix[1][1]) == 'X' and (matrix[1][0]) == 'X')\
               or ((matrix[2][2]) == 'X' and (matrix[2][1]) == 'X' and (matrix[2][0]) == 'X')\
               or ((matrix[0][2]) == 'X' and (matrix[1][1]) == 'X' and (matrix[2][0]) == 'X')\
               or ((matrix[2][2]) == 'X' and (matrix[1][1]) == 'X' and (matrix[0][0]) == 'X'):
                x_wins = 1
                pass
            elif ((matrix[0][2]) == 'O' and (matrix[1][2]) == 'O' and (matrix[2][2]) == 'O')\
                or ((matrix[0][1]) == 'O' and (matrix[1][1]) == 'O' and (matrix[2][1]) == 'O')\
                or ((matrix[0][0]) == 'O' and (matrix[1][0]) == 'O' and (matrix[2][0]) == 'O')\
                or ((matrix[0][2]) == 'O' and (matrix[0][1]) == 'O' and (matrix[0][0]) == 'O')\
                or ((matrix[1][2]) == 'O' and (matrix[1][1]) == 'O' and (matrix[1][0]) == 'O')\
                or ((matrix[2][2]) == 'O' and (matrix[2][1]) == 'O' and (matrix[2][0]) == 'O')\
                or ((matrix[0][2]) == 'O' and (matrix[1][1]) == 'O' and (matrix[2][0]) == 'O')\
                or ((matrix[2][2]) == 'O' and (matrix[1][1]) == 'O' and (matrix[0][0]) == 'O'):
                o_wins = 1
                pass
            elif (x_wins == 1 and o_wins == 1) or (abs(int(amount_of_o) - int(amount_of_x)) >= 2):
                result_impossible = 1
                pass
            elif (x_wins == 0) and (o_wins == 0) and move_counter == 9:
                result_draw = 1
                pass
            if result_impossible == 1:
                print('Impossible')
                continue
            elif result_draw == 1:
                print('Draw')
                break
            elif x_wins == 1:
                print('X wins')
                break
            elif o_wins == 1:
                print('O wins')
                break
            continue
