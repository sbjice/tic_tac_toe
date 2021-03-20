class TicTacToe:
    # counter = 0

    def __init__(self):
        # TicTacToe.counter += 1
        # if TicTacToe.counter > 1:
        #     return None
        self.field = []
        self.current_choice = ' '
        self.field = self.get_empty_field()
        self.main_loop()

    def print_game_field(self):
        for row in self.field:
            [print(row[i], end=' | ') if i < 2 else print(row[i]) for i in range(len(row))]
            print(f'---------')

    @staticmethod
    def get_empty_field():
        return [[' ' for __ in range(3)] for _ in range(3)]

    @staticmethod
    def get_full_field():
        return [['x' for __ in range(3)] for _ in range(3)]

    @staticmethod
    def get_coordinates():
        x = 0
        while x not in range(1, 4):
            try:
                x = int(input("Enter row number (from 1 to 3): "))
            except Exception as e:
                print(e)
        y = 0
        while y not in range(1, 4):
            try:
                y = int(input("Enter column number (from 1 to 3): "))
            except Exception as e:
                print(e)
        x -= 1
        y -= 1

        print(f"row: {x}, column: {y}")
        return x, y

    def point_can_be_filled(self, row, col):
        return self.field[row][col] == ' '

    def column_is_filled_with_given_choice(self, col=0, choice='x'):
        for row in self.field:
            if row[col] != choice:
                return False
        return True

    def row_is_filled_with_given_choice(self, row=0, choice='x'):
        for col in range(len(self.field)):
            if self.field[row][col] != choice:
                return False
        return True

    def winning_on_rows_with_given_choice(self, choice='x'):
        for i in range(len(self.field)):
            if self.row_is_filled_with_given_choice(i, choice):
                return True
        return False

    def winning_on_columns_with_given_choice(self, choice='x'):
        for i in range(len(self.field)):
            if self.column_is_filled_with_given_choice(i, choice):
                return True
        return False

    def winning_on_main_diagonal_with_given_choice(self, choice='x'):
        for i in range(len(self.field)):
            if self.field[i][i] != choice:
                return False
        return True

    def winning_on_side_diagonal_with_given_choice(self, choice='x'):
        for i in range(len(self.field)):
            if self.field[len(self.field)-1-i][i] != choice:
                return False
        return True

    def winning_for_given_choice(self, choice='x'):
        if self.winning_on_main_diagonal_with_given_choice(choice):
            return True
        if self.winning_on_side_diagonal_with_given_choice(choice):
            return True
        if self.winning_on_columns_with_given_choice(choice):
            return True
        if self.winning_on_rows_with_given_choice(choice):
            return True
        return False

    def field_filled(self):
        for row in self.field:
            for val in row:
                if val == ' ':
                    return False
        return True

    @staticmethod
    def field_given_filled(field):
        for row in field:
            for val in row:
                if val == ' ':
                    return False
        return True

    def fill_field_until_win_or_draw(self):
        self.current_choice = 'x'
        while True:
            print(f"Player with {self.current_choice} should put his figure: ")
            row_val, col_val = self.get_coordinates()
            while not self.point_can_be_filled(row_val, col_val):
                print('The given point is not free, enter new point!')
                row_val, col_val = self.get_coordinates()
            self.field[row_val][col_val] = self.current_choice
            self.print_game_field()

            if self.winning_for_given_choice(self.current_choice):
                print(f"The player with {self.current_choice} wins!")
                return
            if self.field_filled():
                print("The Draw!")
                return
            if self.current_choice == 'x':
                self.current_choice = 'o'
            else:
                self.current_choice = 'x'

    def main_loop(self):
        keep_playing = None
        while keep_playing != 'n':
            keep_playing = input("Do you want to play TicTacToe? (y or n): ")
            if keep_playing == 'y':
                self.fill_field_until_win_or_draw()


# TODO: Create AI for playing with PC


if __name__ == "__main__":
    t1 = TicTacToe()



