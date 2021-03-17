from main import *

test_field = get_empty_field()
test_field[2][0] = 'x'
test_field[2][1] = '0'
test_field[2][2] = 'x'
print_game_field(test_field)

print(winning_on_rows_with_given_choice(test_field, 'x'))
print('winning on rows')

test_field = get_empty_field()
test_field[0][2] = 'x'
test_field[1][2] = '0'
test_field[2][2] = 'x'
print_game_field(test_field)

print(winning_on_columns_with_given_choice(test_field, 'x'))
print('winning on cols')


test_field = get_empty_field()
test_field[0][0] = 'x'
test_field[1][1] = 'x'
test_field[2][2] = 'x'
print_game_field(test_field)

print(winning_on_main_diagonal_with_given_choice(test_field, 'x'))
print('winning on main diagonal')

test_field = get_empty_field()
test_field[0][2] = 'x'
test_field[1][1] = ' '
test_field[2][0] = 'x'
print_game_field(test_field)

print(winning_on_side_diagonal_with_given_choice(test_field, 'x'))
print('winning on side diagonal')


test_field = get_empty_field()
test_field[0][2] = 'x'
test_field[1][1] = 'x'
test_field[2][0] = 'x'
test_field[0][1] = 'o'
test_field[1][0] = 'o'
test_field[2][1] = 'o'
test_field[1][2] = 'o'
print_game_field(test_field)
print(winning_for_given_choice(test_field, 'x'))
print('winning')