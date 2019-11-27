import unittest
from src.solution import Solution
from src.parameters import Parameters


class MyTestCase(unittest.TestCase):
    def test_solution_functions(self):
        rating1 = [3, 2, 1, 3]
        skill1 = [[1, 1, 2, 2], [2, 1, 1, 2], [1, 1, 2, 1]]
        sol1 = [2, 2, 0, 0]
        solution1 = Solution(employee_number=3, premade_list=sol1)
        self.assertEqual(solution1.f_target(rating1, skill1), 13)
        emp_time = [1.5, 2, 1]
        comp_time = [1, 1, 0.5, 0.5]
        parameters = Parameters(rating1, skill1, emp_time, comp_time)
        self.assertEqual(solution1.f_penalty(emp_time, comp_time), 4)
        self.assertEqual(solution1.adaptation(parameters), 9)


if __name__ == '__main__':
    unittest.main()
