import unittest
from Puzzle import Puzzle
import utils
import copy

file1 = "data/board.txt"
file2 = "data/board2.txt"
file3 = "data/board3.txt"
file4 = "data/board4.txt"


class TestPuzzleMethods(unittest.TestCase):

    def test_is_solvable1(self):
        p = Puzzle(utils.board_from_file(file1))
        self.assertEqual(True, p.is_solvable())

    def test_is_solvable2(self):
        p = Puzzle(utils.board_from_file(file2))
        self.assertEqual(True, p.is_solvable())

    def test_is_solvable_false(self):
        p = Puzzle(utils.board_from_file(file3))
        self.assertEqual(False, p.is_solvable())

    def test_number_of_inversions(self):
        p = Puzzle(utils.board_from_file(file2))
        self.assertEqual(41, p.number_of_inversions())

    def test_get_updated_configuration(self):
        p = Puzzle(utils.board_from_file(file3))
        p_copy = copy.deepcopy(p)
        p2 = p.get_updated_configuration("up")
        p2_expected = Puzzle(utils.board_from_file(file4))

        self.assertEqual(p_copy, p)
        self.assertEqual(p2_expected, p2)


if __name__ == '__main__':
    unittest.main()
