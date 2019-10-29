#!/usr/local/bin/python3
import sys
from Sudoku import Viewer

class StdOutWrapper:
    def __init__(self):
        self.text = ""

    def write(self, txt):
        self.text += txt
        self.text = '\n'.join(self.text.split('\n')[-30:])

    def get_text(self, beg, end):
        return '\n'.join(self.text.split('\n')[beg:end])

if __name__ == "__main__":
    # Make puzzle
    mystdout = StdOutWrapper()
    sys.stdout = mystdout
    sys.stderr = mystdout

    viewer = Viewer.Viewer()

    while viewer.loop():
        pass
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    sys.stdout.write(mystdout.get_text())

