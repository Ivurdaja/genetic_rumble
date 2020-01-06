from src.get_data import get_data
from src.loading_txt import load_parametry, load_populacja
from time import sleep

params = load_parametry()
# attr_params = vars(params)
# print('zmienne parametrów:\n')
# print('\n'.join(f'{i}' for i in attr_params.items()))
# sleep(0.2)
populacja = load_populacja(params)
# print('zmienne populacji:\n')
# print(str(len(populacja.main_list)))
# for i in populacja.main_list:
#     print(f'{i.company_employee_list}\n')
# sleep(0.2)
get_data(2, populacja)
