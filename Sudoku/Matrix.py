from Sudoku.Cell import Cell


class Matrix:
    def __init__(self):
        self.cells = [[Cell(), Cell(), Cell()],
                      [Cell(), Cell(), Cell()],
                      [Cell(), Cell(), Cell()]]

    def __getitem__(self, index):
        i0, i1 = index  # Assume an x and y index
        return self.cells[i0][i1]  # Returns: a Cell value

    def __setitem__(self, index, value):
        i0, i1 = index  # Assume an x and y index
        self.cells[i0][i1] = value

    def __str__(self):
        # Output String
        os = ""
        for row in self.cells:
            os += "[ "
            for item in row:
                os += str(item) + " "
            os += "]\n"
        return os

    def __repr__(self):
        return str(self)

    def get_row(self, row):
        return [value for value in self.cells[row]]

    def get_col(self, col):
        return [value[col] for value in self.cells]

    def set_value(self, row, col, val):
        self[row][col].set_value(val)

    def check_matrix(self):
        # Check if any duplicates exist
        for i in range(1, 10):
            # print("="*30)
            # print(f"Testing {i}")
            output = sum(cell == i for cells in self.cells for cell in cells)
            # print(f"Output: {output}")

            # Check if there is only one of each number in the matrix
            if output == 0:
                # If a value isn't found in the matrix
                return False
            elif output > 1:
                # If more than one value is found in the row
                return False
        return True
