from Puzzle import Puzzle
from PuzzleSolver import PuzzleSolver

p = Puzzle("board.txt")
logs = "test.txt"
solver = PuzzleSolver(p, logs)
print(p)
print(p.heuristic)

y = input("Solve puzzle? (y/n): ")
if y == 'y':
    solver.solve()