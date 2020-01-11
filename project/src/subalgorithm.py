from src.parameters import Parameters   
from src.population import Population


def stop(parent: Population, offspring: Population, parametres: Parameters) -> int:
    "Funkcja opisujaca warunek stopu. Algorytm wykonuje kolejne iteracje do momentu,"
    "gdy roznica procentowa miedzy populacjami bedzie mniejsza niż difference_par kilka razy pod rzad"
    #sum_parent = max(parent.main_list[i].adaptation(parametres) for i in range(len(parametres.skills_matrix[0])))
    #sum_offspring = sum(offspring.main_list[i].adaptation(parametres) for i in range(len(parametres.skills_matrix[0])))
    max_parent = max(parent.main_list, key=lambda q: q.adaptation(parent.parameters)).adaptation(parametres)
    max_offspring = max(offspring.main_list, key=lambda q: q.adaptation(offspring.parameters)).adaptation(parametres)
    return abs((max_parent-max_offspring)/max_parent)

def offspring(main_list: Population, mut_prob):
    "Funkcja generująca nowa populacje"
    main_list.selection()
    main_list.crossover()
    main_list.mutation(mut_prob)
    return main_list.merging()





