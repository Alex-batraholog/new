def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [5, ['a', 'b', 'c'], 'Home']
values_dict = {'a': 3, 'b': 'dict', 'c': 3.14}
values_list_2 = [False, 17]
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)



