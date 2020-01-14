from src.population import Population
from src.loading_txt import load_parametry,load_populacja
from src.subalgorithm import stop,offspring
from src.get_data import get_data


def algorithm(parent_population: Population = None, difference: float = 0.001, mut_probability: float=0.1, hour_rate: int=4):
    parameters = load_parametry(hour_rate)
    population = load_populacja(parameters)
    counter = 0         #licznik iteracji
    get_data(counter, population)
    result_difference = 1
    result = 0
    while result < 3:
        if result_difference< difference:
            result += 1
        else:
            if result > 0:
                result = 0
        if counter > 1000:
            break
        else:
            if counter == 0:
                parent_population = population
            else:
                parent_population = offspring_population
            offspring_population = offspring(parent_population, mut_probability)
            result_difference = stop(parent_population, offspring_population, parameters)   #wynik warunku stopu
            print("result=")
            print(result_difference)
            counter += 1
            get_data(counter, offspring_population)

    print(counter)


#algorithm(hour_rate=50)
#algorithm(mut_probability=0.2)
algorithm()
