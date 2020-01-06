from src.population import Population
from src.param_generate import string_mod
from datetime import datetime

# w tym pliku jest funkcja która dodaje nr iteracji, wartości funkcji celu i kary oraz postac rozwiązania najlepszego
# rozwiązania w danej iteracji. Przy pierwszej iteracji dodaje tez datę i czas. Plik jest modyfikowany w trybie append,
# wiec po ponownym uruchomieniu algorytmu nie wyczyści się.


def get_data(iterate_num: int, population: Population):
    # podawac iteracje od 0 (czyli wprost zmienną iteracyjną), +1 odbywa się w pliku
    best_solution = max(population.main_list, key=lambda q: q.adaptation(population.parameters))
    target_value = best_solution.f_target(population.parameters.rating, population.parameters.skills_matrix)
    penalty_value = best_solution.f_penalty(population.parameters.employee_time, population.parameters.company_time,
                                            population.parameters.alpha)
    best_solution_string = string_mod(str(best_solution.company_employee_list))

    current_time = datetime.now()
    current_time = current_time.strftime("%H:%M:%S %d/%m/%Y")
    f = open("dane_z_algorytmu.txt", "a+")
    if iterate_num == 0:
        f.write(f'DANE Z ALGORYTMU, {current_time}\n')
        f.write('NR_ITERACJI , FUNKCJA_CELU , FUNKCJA_KARY , POSTAC_ROZWIAZANIA\n')
    f.write(f'{iterate_num} , {target_value} , {penalty_value} , {best_solution_string}\n')
    f.close()
