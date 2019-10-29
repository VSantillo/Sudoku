from Sudoku.Matrix import Matrix


class Puzzle:
    def __init__(self):
        self.puzzle = [[Matrix(), Matrix(), Matrix()],
                       [Matrix(), Matrix(), Matrix()],
                       [Matrix(), Matrix(), Matrix()]]
        self.populate_puzzle()

    def __getitem__(self, index):
        i0, i1 = index
        return self.puzzle[i0][i1]  # Returns: a Matrix

    def __str__(self):
        # Output String (os)
        os = ""

        # Iterate over "global rows"
        for row in range(0, 9):
            # Separate matrices horizontally
            if row % 3 == 0:
                os += "=" * 31 + "\n"

            # Iterate over the row of the matrices within the puzzle
            for index, item in enumerate(self.get_row(row)):
                os += "‖[ "  # Want to look pretty

                # Add each element to the output string
                for element in item:
                    os += str(element) + " "
                os += "]"

                if index == 2:
                    os += "‖\n"
        os += "=" * 31 + "\n"
        return os

    def populate_puzzle(self):
        # Just a start template, look into populating algorithms?
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  7, 8, 9, 1, 2, 3, 4, 5, 6,
                  2, 1, 4, 3, 6, 5, 8, 9, 7,
                  3, 6, 5, 8, 9, 7, 2, 1, 4,
                  8, 9, 7, 2, 1, 4, 3, 6, 5,
                  5, 3, 1, 6, 4, 2, 9, 7, 8,
                  6, 4, 2, 9, 7, 8, 5, 3, 1,
                  9, 7, 8, 5, 3, 1, 6, 4, 2]
        values.reverse()

        for m_row in range(0, 3):
            for row in range(0, 3):
                for m_col in range(0, 3):
                    for col in range(0, 3):
                        self[m_row, m_col][row, col].populate_value(values.pop())

    @staticmethod
    def find_matrices(dim):
        # Identify which dimension (row/col) of matrices we're interested in based on the dimension value provided
        if dim <= 2:
            return 0
        elif 3 <= dim <= 5:
            return 1
        elif 6 <= dim <= 8:
            return 2
        else:
            return -1

    def set_value(self, row, col, val):
        # Determine the location of the matrix being operated on
        m_row = self.find_matrices(row)
        m_col = self.find_matrices(col)
        row = row % 3
        col = col % 3

        self[m_row, m_col][row, col].set_value(val)

    def get_row(self, row):
        return [matrix.get_row(row % 3) for matrix in self.puzzle[self.find_matrices(row)]]

    def get_col(self, col):
        return [self[m_row, self.find_matrices(col)].get_col(col % 3) for m_row in range(0, 3)]

    def check_row(self, row):
        # Unpack all of the items into a single flat list
        cur_row = [item for row in self.get_row(row) for item in row]

        # Iterate over the numbers of Sudoku
        for i in range(1, 10):
            output = sum(item == i for item in cur_row)  # Add up each instance of each number

            if output == 0:
                # If a value isn't found in the row
                return False
            elif output > 1:
                # If more than one value is found in the row
                return False
        return True

    def check_col(self, col):
        # Unpack all of the items into a single flat list
        cur_col = [item for col in self.get_col(col) for item in col]

        # Iterate over the numbers of Sudoku
        for i in range(1, 10):
            output = sum(item == i for item in cur_col)  # Add up each instance of each number

            if output == 0:
                # If a value isn't found in the column
                return False
            elif output > 1:
                # If more than one value is found in the column
                return False
        return True

    def check_puzzle(self):
        # Matrix Checking
        for m_row in range(0, 3):
            for m_col in range(0, 3):
                matrix_flag = self[m_row, m_col].check_matrix()
                if not matrix_flag:
                    return f"Matrix [{m_col}, {m_row}] is bad."

        # Row Checking
        for row in range(0, 9):
            row_flag = self.check_row(row)
            if not row_flag:
                return f"Row {row} is unsolved."

        # Column Checking
        for col in range(0, 9):
            col_flag = self.check_col(col)
            if not col_flag:
                return f"Col {col} is unsolved."

        return True
