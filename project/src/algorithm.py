
from src.population import Population
from src.loading_txt import load_parametry,load_populacja
from src.subalgorithm import stop,offspring
from src.get_data import get_data


def algorithm(parent_population: Population = None, difference: float = 0.2):
    parameters = load_parametry()
    population = load_populacja(parameters)
    counter = 0         #licznik iteracji
    result = 1
    while result > difference:
        if counter >3000:
            break
        else:
            if parent_population == None:
                parent_population = Population(parameters)
            else:
                parent_population = population
            offspring_population = Population(parameters, offspring(parent_population))
            result = stop(parent_population, offspring_population, parameters)   #wynik warunku stopu
            counter += 1
            get_data(counter, offspring_population)

    print(counter)


algorithm()