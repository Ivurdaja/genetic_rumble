from random import randint
from typing import List
from src.parameters import Parameters


class Solution:
    """Klasa bedąca osobnikiem tj. rozwiązaniem zadania"""

    def __init__(self, employee_number: int, company_number: int, premade_list: List[int] = None):
        # Solution posiada pola: lista(indeksy listy = firmy) indeksów(osób), max indeks pracowników
        if premade_list:  # przypadek testowy
            self.company_employee_list = premade_list
            self.number_of_employees = employee_number
        else:
            self.company_employee_list = []
            self.number_of_employees = employee_number
            for k in range(company_number):  # 1 losowy pracownik dla każdej firmy
                self.company_employee_list.append(randint(0, employee_number - 1))

    def print(self):
        """Print do wypisywania rozwiązania"""
        print(str(self.company_employee_list))

    def f_target(self, rating: List[int], skills_matrix: List[List[float]]) -> float:
        """Funkcja celu"""
        "Rating traktowany jest jako kategoria, definiujaca kwote, " \
        "ktora uzyskamy w wyniku nawiazania wspolpracy z dana firma"
        result = 0
        for m in range(len(self.company_employee_list)):
            for n in range(self.number_of_employees):
                if self.company_employee_list[m] == n:
                    result += rating[m] * skills_matrix[n][m]*1000
        return round(result,2)

    def f_penalty(self, employee_time: List[float], company_time: List[float], skills_matrix: List[List[float]],
                  alpha: int = 4, overtime_allowance: float = 1.5) -> float:
        """Funkcja kary"""
        "Alpha stanowi tutaj hour rate, czyli podstawe do wyliczenia stawki godzinowej dla " \
        "kazdego pracownika na postawie skills_matrix"
        result = 0
        company_time_sum = [0 for i in range(self.number_of_employees)]
        employee_salary = [0 for i in range(self.number_of_employees)]
        hourly_rate = [(sum(skills_matrix[n]) * alpha)/len(self.company_employee_list)
                       for n in range(self.number_of_employees)]
        for n in range(self.number_of_employees):
            for m in range(len(self.company_employee_list)):
                if self.company_employee_list[m] == n:
                    company_time_sum[n] += company_time[m]
            overtime = company_time_sum[n] - employee_time[n]
            if overtime > 0:
                employee_salary[n] = employee_time[n]*hourly_rate[n]
                employee_salary[n] += overtime*hourly_rate[n]*overtime_allowance
            else:
                employee_salary[n] = company_time_sum[n]*hourly_rate[n]
            result += employee_salary[n]
        return round(result,2)

    def adaptation(self, parameters: Parameters) -> float:
        """Funkcja przystosowania"""
        # Do operacji na populacji po wartości tej funkcji dla danego osobnika
        return self.f_target(parameters.rating, parameters.skills_matrix) - self.f_penalty(
            parameters.employee_time, parameters.company_time, parameters.skills_matrix, parameters.alpha)
