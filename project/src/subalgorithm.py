from src.parameters import Parameters   
from src.population import Population


def stop(parent: Population, offspring: Population, parametres: Parameters, difference_par: int = 0.00001) -> int:
    "Funkcja opisujaca warunek stopu. Algorytm wykonuje kolejne iteracje do momentu,"
    "gdy roznica procentowa miedzy populacjami bedzie mniejsza niż difference_par kilka razy pod rzad"
    sum_parent = sum(parent.main_list[i].adaptation(parametres) for i in range(len(parametres.skills_matrix[0])))
    sum_offspring = sum(offspring.main_list[i].adaptation(parametres) for i in range(len(parametres.skills_matrix[0])))
    return abs((sum_offspring-sum_parent)/sum_parent)

def offspring(main_list: Population):
    "Funkcja generująca nowa populacje"
    main_list.selection()
    main_list.crossover()
    main_list.mutation()
    return main_list.merging()





