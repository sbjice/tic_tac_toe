def print_game_field(field):
    for row in field:
        [print(row[i], end=' | ') if i < 2 else print(row[i]) for i in range(len(row))]
        print(f'---------')


def get_empty_field():
    return [[' ' for __ in range(3)] for _ in range(3)]


def get_coordinates():
    x = 0
    while x not in range(1, 4):
        x = int(input("Enter row number (from 1 to 3)"))
    y = 0
    while y not in range(1, 4):
        y = int(input("Enter column number (from 1 to 3)"))
    x -= 1
    y -= 1

    print(f"row: {x}, column: {y}")
    return x, y


def point_can_be_filled(field, row, col):
    return field[row][col] == ' '


def column_is_filled_with_given_choice(field, col=0, choice='x'):
    for row in field:
        if row[col] != choice:
            return False
    return True


def row_is_filled_with_given_choice(field, row=0, choice='x'):
    for col in range(len(field)):
        if field[row][col] != choice:
            return False
    return True


# row_val, col_val = get_coordinates()
# while not point_can_be_filled(test_field, row_val, col_val):
#     print('The given point is not free, enter new point!')
#     row_val, col_val = get_coordinates()


def winning_on_rows_with_given_choice(field, choice='x'):
    for i in range(len(field)):
        if row_is_filled_with_given_choice(field, i, choice):
            return True
    return False


def winning_on_columns_with_given_choice(field, choice='x'):
    for i in range(len(field)):
        if column_is_filled_with_given_choice(field, i, choice):
            return True
    return False


def winning_on_main_diagonal_with_given_choice(field, choice='x'):
    for i in range(len(field)):
        if field[i][i] != choice:
            return False
    return True


def winning_on_side_diagonal_with_given_choice(field, choice='x'):
    for i in range(len(field)):
        if field[len(field)-1-i][i] != choice:
            return False
    return True


def winning_for_given_choice(field, choice='x'):
    if winning_on_main_diagonal_with_given_choice(field, choice):
        return True
    if winning_on_side_diagonal_with_given_choice(field, choice):
        return True
    if winning_on_columns_with_given_choice(field, choice):
        return True
    if winning_on_rows_with_given_choice(field, choice):
        return True
    return False



# TODO 1: Move to classes
# TODO 2: Create field autofill consistent with current player change
# TODO 3: Create AI for playing with PC
# TODO 4: Create main loop with game reset
