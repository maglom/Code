def set_by_path(input_dict, path, value):
    if path[0] in input_dict:
        for i in path[1:]:
            input_dict[path[0]] = 





    print(input_dict)

set_by_path({'a':1}, ['b'], 2) #-> {'a':1, 'b':2}
print(set_by_path({'a':1}, ['a','b'], 2)) #-> {'a':{'b':2}}
set_by_path({'a':1}, ['b','c','d'], 2) #-> {'a':1, 'b':{'c':{'d'2}}}