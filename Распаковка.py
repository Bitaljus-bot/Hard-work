def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1.23, 'roma', False]
values_dict = {'a':1.53, 'b': 'go', 'c': len}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'roma']
print_params(*values_list_2, 42)