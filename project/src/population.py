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
        
    def crossover(self):
        pair_list = [(self.main_list[2*i], self.main_list[2*i + 1])
                     for i in range(len(self.main_list)//2)] # otrzymamy listę par rozwiązań
        self.temporary_list = []
        for i in range(len(pair_list)):
            crossing_point = randint(1, len(self.parameters.skills_matrix[0])-1) #wylosowanie punktu krzyżowania
            offspring_1 = pair_list[i][0].company_employee_list[:crossing_point] + pair_list[i][1].company_employee_list[crossing_point:]  # stworzenie pierwszego potomka
            offspring_2 = pair_list[i][1].company_employee_list[:crossing_point] + pair_list[i][0].company_employee_list[crossing_point:]
            self.temporary_list.append(offspring_1)
            self.temporary_list.append(offspring_2)

    def mutation(self, mut_prob: float = 0.1):
        "Mutacja z prawdopodbienstwem mut_prob"
        for i in range(len(self.temporary_list)):
            for j in range(len(self.temporary_list[i])):
                temp_gene = self.temporary_list[i][j]
                prob = random()
                if prob <= mut_prob:        #dla każdego genu losujemy liczbę z przedziału (0,1) i sprawdzamy, czy jest mniejsza od prawd. mutacji
                     while temp_gene == self.temporary_list[i][j]:
                        temp_gene = randint(0, len(self.parameters.skills_matrix) - 1)
                self.temporary_list[i][j] = temp_gene

    def merging(self) -> List:
        "Laczenie populacji rodzicielskiej z potomkami, sortowanie wg f.adaptacji oraz wyznaczenie nowej populacji z najlepszych osobnikow"
        self.temporary_list = [Solution(len(self.parameters.skills_matrix), len(self.parameters.skills_matrix[0]), self.temporary_list[i]) for i in range(len(self.temporary_list))]
        merged_list = self.main_list + self.temporary_list      #złączenie list rodziców i potomków
        merged_list.sort(key=lambda obj: obj.adaptation(self.parameters), reverse=True)     #posortowanie wszystkich osobników od najlepszego do najgorszego
        merged_list = merged_list[:len(self.main_list)]
        self.main_list = merged_list        #powstaje lista nowych rodziców 
    
    # TODO zrobić testy, zwłaszcza dla dotychczas napisanych
    #  pododawać błędy i ich obsługi
