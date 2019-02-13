from Puzzle import Puzzle
from PuzzleSolver import PuzzleSolver
import utils

file = "data/board2.txt"
p = Puzzle(utils.board_from_file(file))
logs = open("data/test.txt", "a")
solver = PuzzleSolver(p)
print(p)

y = input("Solve puzzle? (y/n): ")
if y == 'y' and p.is_solvable():
    solution = solver.a_star()
    for s in reversed(solution):
        logs.write(str(s))
        logs.write("\n\n")
    logs.write("Puzzle solved with " + str(len(solution)) + " steps.")
    print("Puzzle solved.")
elif y != 'y':
    print("Solver quit.")
else:
    print("Puzzle is not solvable.")
