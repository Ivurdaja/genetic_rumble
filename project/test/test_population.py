import unittest
from src.solution import Solution
from src.parameters import Parameters
from src.population import Population, MeasuresError


class PopulationTestCase(unittest.TestCase):
    def test_population_init(self):
        rating1 = [1, 2, 3.5, 4, 5]  # 5 firm
        skill1 = [[2, 2, 1, 3, 2], [1, 1, 1, 2, 1], [2, 3, 2, 1, 1]]  # 3 pracowników
        emp_time1 = [1.8, 2, 0.7]
        comp_time1 = [1, 2, 2.5, 1.5, 0.8]
        params = Parameters(rating=rating1, skills_matrix=skill1, employee_time=emp_time1, company_time=comp_time1)
        current_population = Population(parameters=params)
        self.assertEqual(len(current_population.main_list), 10)
        custom_list = [Solution(employee_number=len(params.skills_matrix),
                                company_number=len(params.skills_matrix[0]))
                       for i in range(5)]
        with self.assertRaises(MeasuresError):
            Population(parameters=params, test_list=custom_list)

    def test_population_selection(self):
        pass
    # TODO: dokończyć test selekcji + zmockować RNG, ew. rozbudować test init


if __name__ == '__main__':
    unittest.main()
