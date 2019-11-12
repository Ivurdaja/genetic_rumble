from random import randint


class Solution:
    def __init__(self, rows: int, cols: int):  # generacja losowej binarnej macierzy rows x cols (1 jedynka/kolumna)
        self.rows: int = rows
        self.cols: int = cols
        self.matrix = []
        for i in range(rows):  # tworzenie macierzy rows x cols wypełnioną zerami
            self.matrix.append([])
            for j in range(cols):
                self.matrix[i].append(0)
        for k in range(cols):  # losowanie, w danej kolumnie, indeksu wiersza w którym ma znaleźć się 1 (1 osoba/firma)
            rand_value_row = randint(0, rows - 1)
            self.matrix[rand_value_row][k] = 1

    def printm(self):
        for i in range(len(self.matrix)):
            print("[", end=" ")
            print(*self.matrix[i], sep=" ", end=" ")
            print("]")


def add(rating, matrix_skills, solutions: Solution) -> float:
    result = 0
    for n in range(solutions.rows):
        for m in range(solutions.cols):
            result += rating[n] * matrix_skills[n][m] * solutions[n][m]
    return result
