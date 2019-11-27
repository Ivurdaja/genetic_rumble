from src.solution import Solution
from src.parameters import Parameters


class Population:
    """Klasa będąca populacją, posiadająca operatory"""
    def __init__(self, parameters: Parameters):
        # Population posiada pola: lista główna osobników tj. rozwiązań, tu trafia lista po inicjalizacji i po danym
        # etapie algorytmu, lista tymczasowa, uzywana w operatorach do przechowania potomków przed zmergowaniem z listą
        # główną.
        self.main_list = [Solution(employee_number=len(parameters.skills_matrix),
                                   company_number=len(parameters.skills_matrix[0]))]
        self.temporary_list = None

    # TODO:  dodać operatory selekcji/krzyżowania/mutacji/złączenia list, ew. otestować
