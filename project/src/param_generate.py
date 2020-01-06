from random import randint, uniform
from typing import List

# Skrypt do generacji pliku z losowymi parametrami na podstawie wymiarów problemu (tj. ilość osób i firm)
# Nie trzeba koniecznie robic od zera, mozna modyfikowac recznie ale trzeba pilnować rozmiarów, jak problem tego samego
# rozmiaru to raczej trudno sie pomylić, ale jakby nowe wymiary to chyba lepiej wygenerowac losowo i ew. wtedy ręcznie.


def string_mod(temp_string: str) -> str:  # wyrzuca pewne znaki ze stringa
    temp_string = temp_string.replace('[', '')
    temp_string = temp_string.replace(']', '')
    temp_string = temp_string.replace(',', '')
    return temp_string


def get_random_param_row(cols_number: int, random_range: List[int],  is_float: bool = True) -> str:
    # zwraca stringa tj. losowy wiersz jakiegoś parametru na podstawie zadanej długości, granic funkcji RNG i typu
    # generowanych liczb
    temporary_list = []
    rounding_number = None
    if is_float:
        func = uniform
        rounding_number = 1
    else:
        func = randint
    for k in range(cols_number):
        temporary_list.append(round(func(random_range[0], random_range[1]), rounding_number))
        # liczby rzeczywiste zaokrąglone do 1 miejsca po przecinku, całkowite zaokrąglone do samych siebie
    return string_mod(str(temporary_list))


def main():
    row = input('Ilość osób?: ')
    col = input('Ilość firm?: ')
    population_size = input("Jaki rozmiar populacji?: ")

    f = open("parametry.txt", "w+")
    param_types = ['EMPLOYEE_NUMBER', 'COMPANY_NUMBER', 'POPULATION_NUMBER', 'RATING', 'SKILLS_MATRIX',
                   'EMPLOYEE_TIME', 'COMPANY_TIME']

    for i in param_types:  # xxx_boundaries = [x, y] to granice losowania dla liczb w parametrach
        if i == 'EMPLOYEE_NUMBER':
            f.write(i + '\n')
            f.write(row + '\n')
        if i == 'COMPANY_NUMBER':
            f.write(i + '\n')
            f.write(col + '\n')
        if i == 'POPULATION_NUMBER':
            f.write(i + '\n')
            f.write(population_size + '\n')
        if i == 'RATING':
            f.write(i + '\n')
            rating_boundaries = [1, 3]
            list_str = get_random_param_row(int(col), rating_boundaries, is_float=False)
            f.write(list_str + '\n')
        if i == 'SKILLS_MATRIX':
            f.write(i + '\n')
            skills_boundaries = [1, 5]
            for j in range(int(row)):
                list_str = get_random_param_row(int(col), skills_boundaries)
                f.write(list_str + '\n')
        if i == 'EMPLOYEE_TIME':
            f.write(i + '\n')
            emp_boundaries = [4, 8]
            list_str = get_random_param_row(int(row), emp_boundaries)
            f.write(list_str + '\n')
        if i == 'COMPANY_TIME':
            f.write(i + '\n')
            comp_boundaries = [1, 3]
            list_str = get_random_param_row(int(col), comp_boundaries)
            f.write(list_str + '\n')
    f.close()


if __name__ == "__main__":
    main()
