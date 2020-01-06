from src.parameters import Parameters
from src.population import Population
from src.solution import Solution

# W tym pliku są funkcje do wczytywania danych, tj. parametrów i populacji początkowej z plików tekstowych


def line2list(strin: str) -> list:  # zamienia linijkę parametru na listę
    temp_str = strin
    temp_str = temp_str.rstrip()
    temp_list = temp_str.split(' ')
    for i in range(len(temp_list)):
        if temp_list[i].find('.') == -1:
            temp_list[i] = int(temp_list[i])
        else:
            temp_list[i] = float(temp_list[i])
    return temp_list


def load_parametry(alpha: int = 4) -> Parameters:
    temp_employee_number = 0
    rating = []
    skills_matrix = []
    employee_time = []
    company_time = []
    population_size = 0
    f = open("parametry.txt", "r")
    f_lines = f.readlines()
    for i in range(len(f_lines)):
        if f_lines[i] == 'EMPLOYEE_NUMBER' + '\n':
            temp_employee_number = int(f_lines[i+1])
        if f_lines[i] == 'POPULATION_NUMBER' + '\n':
            population_size = int(f_lines[i+1])
        if f_lines[i] == 'RATING' + '\n':
            rating = line2list(f_lines[i+1])
        if f_lines[i] == 'SKILLS_MATRIX' + '\n':
            for j in range(temp_employee_number):
                skills_matrix.append(line2list(f_lines[i+1+j]))
        if f_lines[i] == 'EMPLOYEE_TIME' + '\n':
            employee_time = line2list(f_lines[i+1])
        if f_lines[i] == 'COMPANY_TIME' + '\n':
            company_time = line2list(f_lines[i+1])
    f.close()
    return Parameters(rating, skills_matrix, employee_time, company_time, alpha=alpha,
                      population_count=population_size)


def load_populacja(params: Parameters) -> Population:
    temp_employee_number = 0
    temp_company_number = 0
    population_size = 0
    solutions = []
    f = open("populacja.txt", "r")
    f_lines = f.readlines()
    for i in range(len(f_lines)):
        if f_lines[i] == 'EMPLOYEE_NUMBER' + '\n':
            temp_employee_number = int(f_lines[i+1])
        if f_lines[i] == 'COMPANY_NUMBER' + '\n':
            temp_company_number = int(f_lines[i+1])
        if f_lines[i] == 'POPULATION_NUMBER' + '\n':
            population_size = int(f_lines[i+1])
        if f_lines[i] == 'POPULATION_MEMBERS' + '\n':
            for j in range(population_size):
                solutions.append(line2list(f_lines[i+1+j]))
    f.close()
    solution_list = []
    for j in range(population_size):
        solution_list.append(Solution(temp_employee_number, temp_company_number, premade_list=solutions[j]))
    return Population(params, solution_list)
