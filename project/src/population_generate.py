from src.param_generate import get_random_param_row

# skrypt do generacji pliku z losową populacją na podstawie rozmiaru populacji, a rozmiar problemu jest wczytany z
# parametry.txt
# Co do modyfikacji gotowego pliku .txt to tak jak w param_generate zostało opisane


def main():
    f_param = open("parametry.txt", "r")
    f_param_lines = f_param.readlines()
    num_of_employees = 0
    num_of_companies = 0
    population_num = 0
    for i in range(len(f_param_lines)):
        if f_param_lines[i] == 'EMPLOYEE_NUMBER' + '\n':
            num_of_employees = int(f_param_lines[i+1])
        if f_param_lines[i] == 'COMPANY_NUMBER' + '\n':
            num_of_companies = int(f_param_lines[i+1])
        if f_param_lines[i] == 'POPULATION_NUMBER' + '\n':
            population_num = int(f_param_lines[i+1])
        if num_of_employees and num_of_companies and population_num:
            break
    f_param.close()

    f_pop = open("populacja.txt", "w+")
    for k in range(6):
        f_pop.write(f_param_lines[k])
    f_pop.write('POPULATION_MEMBERS' + '\n')
    for j in range(int(population_num)):
        temp_str = get_random_param_row(num_of_companies, [0, num_of_employees-1], is_float=False)
        f_pop.write(temp_str + '\n')
    f_pop.close()


if __name__ == "__main__":
    main()
