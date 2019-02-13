def board_from_file(file):
    """
    :param file: Path to CSV file of a 15-Puzzle configuration.
    :return: Matrix representation of the 15-Puzzle configuration in file.
    """
    # Read input from file to create a board configuration
    file_reader = open(file, 'r')
    board_rep = ""

    for line in file_reader:
        board_rep = line
    file_reader.close()

    board_rep = board_rep.split(', ')

    board = [[],
             [],
             [],
             []]

    for i in range(len(board)):
        for j in range(len(board)):
            board[i].append(int(board_rep.pop(0)))

    return board
