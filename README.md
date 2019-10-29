# Sudoku 

I've been playing quite a bit of Sudoku recently and became interested in figuring out what that would look like to 
as program. It's all Pure Python, with curses for a UI to learn it. If you want to run it, clone this project, and 
just run main in a Terminal window.

`python3 main.py`

`./main.py`

There's a few problems with it. It can't generate puzzles. Because all of the values are pre-populated (as such that a
real game wouldn't let you edit the initial hints), none of the values are editable without changing the source code. 
`(Cell.py, Line 13)` The UI is terrible because I wanted to be fancy but Mac OS doesn't have the extended ASCII table
and I'm not that clever.
