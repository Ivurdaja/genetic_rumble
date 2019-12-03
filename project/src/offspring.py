from random import random
from random import randint
from population import *

def crossover(population: Population):
    pair_list = [(Population.main_list[i], Population.main_list[i + 1])
                 for i in range(len(Population.main_list) - 1)]  # otrzymamy listę par roziązań
    temporary_list = []

    for i in range(len((pair_list + 1) / 2)):
        crossing_point = randint(1,len(Population.main_list[0]) - 1)  # wylosowanie punktu krzyżowania #poprawić na ilość firm-1
        if i == 0:
            offspring_1 = pair_list[0][0][:crossing_point] + pair_list[0][1][
                                                             crossing_point:]  # stworzenie pierwszego potomka
            offspring_2 = pair_list[0][1][:crossing_point] + pair_list[0][0][crossing_point:]
            temporary_list.append(offspring_1)
            temporary_list.append(offspring_2)
        else:
            offspring_1 = pair_list[2 * i][0][:crossing_point] + pair_list[2 * i][1][crossing_point:]  # stworzenie pierwszego potomka
            offspring_2 = pair_list[2 * i][1][:crossing_point] + pair_list[2 * i][0][crossing_point:]
            temporary_list.append(offspring_1)
            temporary_list.append(offspring_2)

    Population.main_list = temporary_list


def mutation(population: Population, mut_pam: float = 0.01):
    for i in range(len(Population.main_list)):
        for j in range(len(Population.main_list[i])):
            temp_gene = Population.main_list[i][j]
            prob = random()
            if prob <= mut_pam:
                if temp_gene == 1:
                    temp_gene = 2
                else:
                    temp_gene -= 1
            Population.main_list[i][j] = temp_gene

