from typing import List


class Parameters:
    """De facto struktura mająca zawierać parametru algorytmu"""
    def __init__(self, rating: List[int], skills_matrix: List[List[float]],
                 employee_time: List[float], company_time: List[float], alpha: int = 4,
                 population_count: int = 10):
        self.rating = rating
        self.skills_matrix = skills_matrix
        self.employee_time = employee_time  # lista okresów, które pracownicy wypracowują, czyli limit
        self.company_time = company_time  # lista okresów, które są spożytkowane na daną firmę
        self.alpha = alpha  # współczynnik mnożony przez "overtime" w funkcji kary, ew. do rozwinięcią
        self.population_count = population_count
