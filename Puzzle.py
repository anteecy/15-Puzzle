class Puzzle:

    def __init__(self, file):
        """
        Creates a representation of a 15-puzzle off of file
        """
        self.file = file
        file_reader = open(self.file, 'r')
        board_rep = ""

        for line in file_reader:
            board_rep = line
        file_reader.close()

        self.tiles = board_rep.split(", ")
        for i in range(len(self.tiles)):
            self.tiles[i] = int(self.tiles[i])

        # Initialize board representation
        self.board = [
                        [],
                        [],
                        [],
                        []
                        ]

        index_counter = 0
        for j in range(len(self.board)):
            for i in range(len(self.board)):
                # Change to something that doesnt change self.tiles for inversion
                tile = self.tiles[index_counter]
                if not tile:
                    self.zeroCord = [j, i]
                self.board[j].append(tile)
                index_counter += 1

        self.heuristic = self.distance_heuristic()

    def __eq__(self, obj):
        return isinstance(obj, Puzzle) and obj.board == self.board

    def __str__(self):
        """
        Displays 15-Puzzle in a tabular format of a 4x4 board
        """
        # Rows
        i = 0
        puzzle = ""
        while i < len(self.board):
            # Columns
            j = 0
            while j < 4:
                tile = self.board[i][j]

                # If the tile is 0 (the representation of empty tile)
                # Make sure that empty string is printed rather than 0
                if tile:
                    puzzle += str(tile) + "\t"
                else:
                    puzzle += " " + "\t"
                j += 1
            puzzle += "\n"
            i += 1

        return puzzle

    def number_of_inversions(self):
        """
        Returns the number of inversions in self.board

        An inversion is a pair of tiles (a,b) such that a appears before b, but a > b.
        """
        inversions = 0

        # Can't check last index because no index after it.
        for i in range(len(self.tiles) - 1):
            for j in range(i + 1, len(self.tiles)):
                if self.tiles[i] and self.tiles[j] and self.tiles[i] > self.tiles[j]:
                    inversions += 1
        return inversions

    def is_solvable(self):
        """
        Determines whether the given board configuration can be solved based
        on the puzzle requirements

        https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
        """

        # To count rows bottom up do 4 - row index
        return (self.number_of_inversions() % 2) != ((4 - self.zeroCord[0]) % 2)

    def distance_heuristic(self):
        """
        https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
        """

        manhattan_distance = 0
        hamming_distance = 0
        for row in range(4):
            for column in range(4):
                tile = self.board[row][column]
                if tile and tile != (1 + (4 * row + column)):
                    hamming_distance += 1
                    expected_row = (tile - 1) // 4
                    expected_column = (tile - 1) % 4
                    manhattan_distance += abs(row - expected_row) + abs(column - expected_column)
                elif not tile and (row != 3 and column != 3):
                    hamming_distance += 1

        return manhattan_distance + hamming_distance

    def update_board(self, direction):
        """
        Moves empty tile in direction dir
        Requires dir in availableMoves
        """

        i = self.zeroCord[0]
        j = self.zeroCord[1]

        if direction == "up":
            self.board[i][j], self.board[i-1][j] = self.board[i-1][j], self.board[i][j]
            self.zeroCord[0] -= 1
        elif direction == "down":
            self.board[i][j], self.board[i+1][j] = self.board[i+1][j], self.board[i][j]
            self.zeroCord[0] += 1
        elif direction == "left":
            self.board[i][j], self.board[i][j-1] = self.board[i][j-1], self.board[i][j]
            self.zeroCord[1] -= 1
        elif direction == "right":
            self.board[i][j], self.board[i][j+1] = self.board[i][j+1], self.board[i][j]
            self.zeroCord[1] += 1

        self.heuristic = self.distance_heuristic()

    def available_moves(self):
        """
        Determines which directions the empty tile may be moved.
        """
        moves = ["left", "right", "up", "down"]
        zero_row = self.zeroCord[0]
        zero_column = self.zeroCord[1]

        if zero_row == 0:
            moves.remove("up")
        elif zero_row == 3:
            moves.remove("down")

        if zero_column == 0:
            moves.remove("left")
        elif zero_column == 3:
            moves.remove("right")
        return moves
