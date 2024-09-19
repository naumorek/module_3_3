
#1

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(c = [1,2,3])

#2

values_list=['Хлопушки', [12,2,5,7],False]
values_dict={'a': 123, 'b':True, 'c': [1,4.24,5,7]}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2=['Фуникулер', [True,True,False]]
print_params(*values_list_2,33)