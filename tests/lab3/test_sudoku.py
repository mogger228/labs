import unittest
from pathlib import Path

from src.lab3 import sudoku


class SudokuTestCase(unittest.TestCase):
    def setUp(self):
        self.grid = [
            list('53..7....'),
            list('6..195...'),
            list('.98....6.'),
            list('8...6...3'),
            list('4..8.3..1'),
            list('7...2...6'),
            list('.6....28.'),
            list('...419..5'),
            list('....8..79'),
        ]

        self.solution = [
            list('534678912'),
            list('672195348'),
            list('198342567'),
            list('859761423'),
            list('426853791'),
            list('713924856'),
            list('961537284'),
            list('287419635'),
            list('345286179'),
        ]

    def test_group(self):
        result = sudoku.group([1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_group_incomplete(self):
        result = sudoku.group([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_group_empty(self):
        self.assertEqual(sudoku.group([], 3), [])

    def test_create_grid(self):
        puzzle = '123456789\n.........\n'
        expected = [list('123456789'), list('.........')]
        self.assertEqual(sudoku.create_grid(puzzle), expected)

    def test_read_sudoku(self):
        path = Path(sudoku.__file__).parent / 'puzzle1.txt'
        self.assertEqual(sudoku.read_sudoku(path), self.grid)

    def test_get_row(self):
        grid = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        self.assertEqual(sudoku.get_row(grid, (1, 2)), ['4', '.', '6'])

    def test_get_col(self):
        grid = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        self.assertEqual(sudoku.get_col(grid, (2, 1)), ['2', '.', '8'])

    def test_get_block(self):
        expected = ['5', '3', '.', '6', '.', '.', '.', '9', '8']
        self.assertEqual(sudoku.get_block(self.grid, (0, 1)), expected)

    def test_get_block_bottom_right(self):
        expected = ['2', '8', '.', '.', '.', '5', '.', '7', '9']
        self.assertEqual(sudoku.get_block(self.grid, (8, 8)), expected)

    def test_find_empty_positions(self):
        self.assertEqual(sudoku.find_empty_positions(self.grid), (0, 2))

    def test_find_empty_positions_full_grid(self):
        self.assertIsNone(sudoku.find_empty_positions(self.solution))

    def test_find_possible_values(self):
        result = sudoku.find_possible_values(self.grid, (0, 2))
        self.assertEqual(result, {'1', '2', '4'})

    def test_find_possible_values_empty(self):
        self.solution[0][0] = '.'
        self.solution[1][0] = '5'
        result = sudoku.find_possible_values(self.solution, (0, 0))
        self.assertEqual(result, set())

    def test_solve(self):
        self.assertEqual(sudoku.solve(self.grid), self.solution)

    def test_solve_full_grid(self):
        self.assertEqual(sudoku.solve(self.solution), self.solution)

    def test_solve_no_solution(self):
        grid = [
            list('.23456789'),
            list('1........'),
            list('.........'),
            list('.........'),
            list('.........'),
            list('.........'),
            list('.........'),
            list('.........'),
            list('.........'),
        ]
        self.assertIsNone(sudoku.solve(grid))
        self.assertEqual(grid[0][0], '.')

    def test_check_solution(self):
        self.assertTrue(sudoku.check_solution(self.solution))

    def test_check_solution_repeated_digit(self):
        self.solution[0][0] = self.solution[0][1]
        self.assertFalse(sudoku.check_solution(self.solution))

    def test_check_solution_empty_cell(self):
        self.solution[0][0] = '.'
        self.assertFalse(sudoku.check_solution(self.solution))

    def test_check_solution_wrong_size(self):
        self.assertFalse(sudoku.check_solution([['1', '2'], ['3', '4']]))

    def test_check_solution_wrong_columns(self):
        self.solution[1] = self.solution[0][:]
        self.assertFalse(sudoku.check_solution(self.solution))

    def test_check_solution_wrong_blocks(self):
        # Переставляем две строки из разных квадратов.
        # Строки и столбцы остаются правильными, но квадраты нарушаются.
        self.solution[0], self.solution[3] = self.solution[3], self.solution[0]
        self.assertFalse(sudoku.check_solution(self.solution))

    def test_generate_sudoku(self):
        grid = sudoku.generate_sudoku(40)
        self.assertEqual(len(grid), 9)

        filled = 0
        for row in grid:
            self.assertEqual(len(row), 9)
            for value in row:
                if value != '.':
                    filled += 1

        self.assertEqual(filled, 40)
        solution = sudoku.solve(grid)
        self.assertIsNotNone(solution)
        self.assertTrue(sudoku.check_solution(solution))

    def test_generate_sudoku_zero(self):
        grid = sudoku.generate_sudoku(0)
        self.assertEqual(len(grid), 9)
        for row in grid:
            self.assertEqual(row, ['.'] * 9)

    def test_generate_sudoku_large_number(self):
        grid = sudoku.generate_sudoku(1000)
        self.assertTrue(sudoku.check_solution(grid))

    def test_generate_sudoku_negative_number(self):
        grid = sudoku.generate_sudoku(-5)
        self.assertEqual(len(grid), 9)
        for row in grid:
            self.assertEqual(row, ['.'] * 9)


if __name__ == '__main__':
    unittest.main()
