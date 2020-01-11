
from src.population import Population
from src.loading_txt import load_parametry,load_populacja
from src.subalgorithm import stop,offspring
from src.get_data import get_data


def algorithm(parent_population: Population = None, difference: float = 0.0001, mut_probability: float=0.1, hour_rate: int=4):
    parameters = load_parametry(hour_rate)
    population = load_populacja(parameters)
    counter = 0         #licznik iteracji
    get_data(counter, population)
    result_difference = 1
    while result_difference > difference:
        if counter >1000:
            break
        else:
            if parent_population == None:
                parent_population = Population(parameters)
            else:
                parent_population = population
            offspring_population = Population(parameters, offspring(parent_population, mut_probability))
            result_difference = stop(parent_population, offspring_population, parameters)   #wynik warunku stopu
            counter += 1
            get_data(counter, offspring_population)

    print(counter)


#algorithm(hour_rate=50)
#algorithm(mut_probability=0.2)
algorithm()
