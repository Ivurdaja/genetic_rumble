from src.solution import Solution
from src.parameters import Parameters
from typing import List
from random import random


class MeasuresError(Exception):
    pass


class Population:
    """Klasa będąca populacją, posiadająca operatory"""
    def __init__(self, parameters: Parameters, test_list: List[Solution] = None):
        # Population posiada pola: lista główna osobników tj. rozwiązań, tu trafia lista po inicjalizacji i po danym
        # etapie algorytmu, lista tymczasowa, uzywana w operatorach do przechowania potomków przed zmergowaniem z listą
        # główną (elitaryzm?), parametry algorytmu.
        if not test_list:
            self.main_list = [Solution(employee_number=len(parameters.skills_matrix),
                                       company_number=len(parameters.skills_matrix[0]))
                              for i in range(parameters.population_count)]
        elif len(test_list) != parameters.population_count:
            raise MeasuresError
        else:
            self.main_list = test_list
        self.temporary_list = None
        self.parameters = parameters

    def selection(self, ni_max: float = 1.5):  # ni_max od 1 do 2, ze wzoru
        """Selekcja rankingowa, sortowanie malejące"""
        self.main_list.sort(key=lambda obj: obj.adaptation(self.parameters), reverse=True)
        lam = len(self.main_list)
        probability_table = [1/lam*(ni_max - (2*ni_max - 2)*(i - 1)/(lam - 1))  # wzór na prawdopodobienstwo wyboru rozw
                             for i in range(1, lam+1)]  # suma tej listy zawsze bedzię równa 1
        temp_list = []
        for j in range(lam):  # dla zrobionej listy prawdopodobienstw robimy ruletkę do kazdego elementu listy rodziców
            random_number = random()  # losowanie z przedziału [0,1)
            probability_sum = 0
            for k in range(len(probability_table)):
                probability_sum += probability_table[k]
                if random_number <= probability_sum:
                    temp_list.append(self.main_list[k])
                    break
        self.main_list = temp_list
    # TODO: dodać operatory krzyżowania/mutacji/złączenia list, zrobić testy, zwłaszcza dla dotychczas napisanych
    #  funkcjonalości Population, ew. pododawać błędy i ich obsługi
