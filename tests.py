from main import TicTacToe

t = TicTacToe()
t.field[2][0] = 'x'
t.field[2][1] = 'o'
t.field[2][2] = 'x'
t.print_game_field()

print('winning on rows')
print(t.winning_on_rows_with_given_choice('x'))

t = TicTacToe()
t.field[0][2] = '0'
t.field[1][2] = '0'
t.field[2][2] = '0'
t.print_game_field()

print('winning on cols')
print(t.winning_on_columns_with_given_choice('x'))

t = TicTacToe()
t.field[0][0] = 'x'
t.field[1][1] = 'x'
t.field[2][2] = 'x'
t.print_game_field()

print(t.winning_on_main_diagonal_with_given_choice('x'))
print('winning on main diagonal')

t = TicTacToe()
t.field[0][2] = 'x'
t.field[1][1] = 'x'
t.field[2][0] = 'x'
t.print_game_field()

print(t.winning_on_side_diagonal_with_given_choice('x'))
print('winning on side diagonal')


t = TicTacToe()
t.field[0][2] = 'x'
t.field[1][1] = 'x'
t.field[2][0] = 'x'
t.field[0][1] = 'o'
t.field[1][0] = 'o'
t.field[2][1] = 'o'
t.field[1][2] = 'o'
t.print_game_field()
print(t.winning_for_given_choice('x'))
print('winning')

full_field = t.get_full_field()
empty_field = t.get_empty_field()

print('check full_field is full')
print(t.field_given_filled(full_field))
print('check empty_field is full')
print(t.field_given_filled(empty_field))
empty_field = t.get_empty_field()

# fill_field_until_win_or_draw(empty_field)


