import queue


class PuzzleSolver:
    # TODO Add documentation for history of problems in the project and their solutions??

    def __init__(self, puzzle, logs):
        """
        Takes in a Puzzle object to solve and logs all moves made by the solver.

        :param puzzle: Instance of puzzle class to be solved.
        :param logs: Text file in which the steps to solve puzzle are kept track in.
        """

        self.puzzle = puzzle
        self.logs = logs

        self.file = open(self.logs, "a")
        self.update_logs()

    @staticmethod
    def opposite_direction(direction):
        """
        :param direction: String in {"left", "right", "up", "down"}.
        :return: The opposite direction of the parameter.
        """
        if direction == 'left':
            s = 'right'
        elif direction == 'right':
            s = 'left'
        elif direction == 'up':
            s = 'down'
        else:
            s = 'up'
        return s

    def update_logs(self):
        """
        Prints to self.file information on what the solver is doing.
        :return: VOID
        """
        self.file.write(str(self.puzzle))
        self.file.write("\n\n")

    def optimal_move(self):
        """
        :return: The next most optimal move to solve the puzzle.
        """
        # TODO Add feature that doesn't allow moves to be repeated
        # Priority queue of tuples (heuristic, move).
        # Highest priority is the minimum heuristic, or the min first element of each tuple.
        q = queue.PriorityQueue()
        for direction in self.puzzle.available_moves():
            self.puzzle.update_board(direction)
            q.put((self.puzzle.heuristic, direction))
            self.puzzle.update_board(self.opposite_direction(direction))

        return q.get()[1]

    def solve(self):
        """
        Solves the 15 Puzzle configuration.
        :return: VOID
        """
        # TODO Implementation where puzzle doesn't need to update to find optimal move (efficiency)
        if self.puzzle.is_solvable():
            steps = 0
            while self.puzzle.heuristic > 0:
                self.puzzle.update_board(self.optimal_move())
                steps += 1
                self.update_logs()

            self.file.write("\n")
            self.file.write("Puzzle solved with " + str(steps) + " steps.")
        else:
            self.file.write("Puzzle is not solvable.")
            print("Puzzle configuration cannot be solved.")

        self.file.close()
