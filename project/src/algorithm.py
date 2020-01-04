from src.solution import Solution
from src.parameters import Parameters   
from src.population import Population
import subalgorithm

def algorithm(parameters: Parameters, parent: Population = None, stop: float = 0.00001):
    counter = 0         #licznik iteracji
    for i in range(5):
        result = 1
        while result > stop:
            if parent == None:
                parent = Population(parameters)
            else:
                parent = offspring
            offspring = Population(parameters, subalgorithm.offspring(parent))
            result = subalgorithm.stop(parent, offspring, parameters)   #wynik warunku stopu
            counter += 1

    offspring.main_list.sort(key=lambda obj: obj.adaptation(offspring.parameters), reverse=True)
    print(counter)
    return offspring.main_list[0]
