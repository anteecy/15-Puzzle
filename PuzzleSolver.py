class PuzzleSolver:
    # TODO Add documentation for history of problems in the project and their solutions??

    def __init__(self, p):
        """
        Takes in a Puzzle object to solve and logs all moves made by the solver.

        :param p: Instance of puzzle class to be solved.
        """

        self.p = p

    @staticmethod
    def reconstruct_path(came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)
        return total_path

    def a_star(self):
        open_set = {self.p}
        closed_set = set()
        came_from = dict()
        g_score = {self.p: 0}
        f_score = {self.p: self.p.heuristic}

        while len(open_set) > 0:
            # current = utils.a_star_helper(open_set, f_score)
            current = min(open_set, key=lambda puzzle: puzzle.heuristic)
            if current.heuristic == 0:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            closed_set.add(current)

            for neighbor in current.neighbors():
                if neighbor in closed_set:
                    continue

                tmp_g_score = g_score[current] + 1

                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif tmp_g_score >= g_score[neighbor]:
                    continue

                came_from[neighbor] = current
                g_score[neighbor] = tmp_g_score
                f_score[neighbor] = g_score[neighbor] + neighbor.heuristic
