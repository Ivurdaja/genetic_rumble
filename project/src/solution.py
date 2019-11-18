from random import randint
from typing import List


class Solution:
    def __init__(self, rows: int = 0, cols: int = 0,
                 employee_number: int = 0, premade_list: List = None):  # rows/cols - algorytm, number/list - test
        # Solution posiada pola: lista indeksów, max indeks pracowników
        if employee_number != 0 and premade_list is not None:
            self.list = premade_list
            self.number_of_employees = employee_number
        else:
            self.list = []
            self.number_of_employees = rows
            for k in range(cols):
                self.list.append(randint(0, rows-1))

    def print(self):
        print(str(self.list))

    def f_target(self, rating: List, matrix_skills: List[List]) -> float:  # funkcja celu
        result = 0
        for m in range(len(self.list)):
            for n in range(self.number_of_employees):
                if self.list[m] == n:
                    result += rating[m] * matrix_skills[n][m]
        return result

    def f_penalty(self, employee_time: List, company_time: List, alpha: int = 4) -> float:  # funkcja kary, zwraca >0
        result = 0
        company_time_sum = [0 for i in range(self.number_of_employees)]
        for n in range(self.number_of_employees):
            for m in range(len(self.list)):
                if self.list[m] == n:
                    company_time_sum[n] += company_time[m]
            if company_time_sum[n] > employee_time[n]:
                result += alpha*(company_time_sum[n]-employee_time[n])
        return result
