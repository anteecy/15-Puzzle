import unittest
from Puzzle import Puzzle
file1 = "board.txt"
file2 = "board2.txt"
file3 = "board3.txt"


class TestPuzzleMethods(unittest.TestCase):

    def test_is_solvable1(self):
        p = Puzzle(file1)
        self.assertEqual(True, p.is_solvable())

    def test_is_solvable2(self):
        p = Puzzle(file2)
        self.assertEqual(True, p.is_solvable())

    def test_is_solvable_false(self):
        p = Puzzle(file3)
        self.assertEqual(False, p.is_solvable())

    def test_number_of_inversions(self):
        p = Puzzle(file2)
        self.assertEqual(41, p.number_of_inversions())


if __name__ == '__main__':
    unittest.main()
# Test comment to see if changes were made.
