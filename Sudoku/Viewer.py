import sys
import curses
from curses.textpad import rectangle
from Sudoku import Puzzle, Pointer




class Viewer:
    def __init__(self):
        """
        Initialize the viewer class. Creates a screen, pointer, and a puzzle. Set some parameters for curses
        """
        self.screen = curses.initscr()
        self.pointer = Pointer.Pointer()
        self.puzzle = Puzzle.Puzzle()

        self.input = ""

        self.x_offset = 5
        self.y_offset = 5

        self.navigation = {curses.KEY_UP: 1, curses.KEY_DOWN: 0, curses.KEY_LEFT: 2, curses.KEY_RIGHT: 3}
        self.quit = [ord('q'), 27]
        curses.noecho()  # Turn off automatic key echoing to screen
        curses.cbreak()  # App will need to reach to keys without needing to hit enter first
        self.screen.keypad(True)  # Use special keys as special keys

    def __del__(self):
        """
        Makes sure that curses restores the settings as not to mess up terminal
        """
        curses.nocbreak()  # Disable cbreak
        curses.echo()      # Re-enable terminal echoing
        self.screen.keypad(False)  # Don't use special keys when returning to tty

        curses.endwin()  # Kill the window


    def display_puzzle(self):
        """
        Display the puzzle by adding lines of the puzzle as well as the status to the output screen
        :return:
        """
        self.screen.addstr(0, 0, "Sudoku Puzzle", curses.A_BOLD)

        # TODO: Sophisticated Line Formatting
        rectangle(self.screen, 4, 4, 9+5, 9+5)
        # For each row in the puzzle, get the items in a row, and display them.

        for row in range(0, 9):
            elements = [item for sublist in self.puzzle.get_row(row) for item in sublist]
            for col in range(0, 9):
                self.screen.addstr(self.y_offset + row, self.x_offset + col, str(elements[col]))
        # Check if puzzle is solved
        reason = self.puzzle.check_puzzle()
        if reason:
            result = 'solved!'
        else:
            result = f'unsolved.\n{reason}'

        # Current status of puzzle
        self.screen.addstr(5, 20, f'Puzzle is {result}')

    def display_last_key(self):
        self.screen.addstr(0, 20, f'You last pressed: {chr(self.input)}, {self.input}, {curses.KEY_DL}')

    def handle_input(self):
        if self.input in self.navigation:
            self.pointer.move(self.navigation[self.input])  # Navigation button was pressed, respond appropriately
        elif self.input in self.quit:
            return False
        elif self.input == 127:
            self.puzzle.set_value(self.pointer.y, self.pointer.x, " ")  # Clear the value
        elif int(chr(self.input)) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.puzzle.set_value(self.pointer.y, self.pointer.x, int(chr(self.input)))  # Add the value
        return True

    def loop(self):
        self.input = None
        while True:
            if self.input is not None:
                ret = self.handle_input()
                if not ret:
                    return False
                self.screen.erase()

                self.display_last_key()

            self.display_puzzle()

            # TODO: I don't like to do this here, but I think it is the best spot
            self.screen.addstr(1, 20, f'Current Matrix Pointer: {self.pointer}')
            self.screen.move(self.y_offset + self.pointer.y, self.x_offset + self.pointer.x)

            self.screen.refresh()

            self.input = self.screen.getch()