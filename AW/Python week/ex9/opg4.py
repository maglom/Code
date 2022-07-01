def set_by_path(input_dict, path, value):
    if path[0] not in input_dict:
        for key in path:
            input_dict[key] = value
    return input_dict



    print(input_dict)

set_by_path({'a':1}, ['b'], 2) #-> {'a':1, 'b':2}
print(set_by_path({'a':1}, ['a','b'], 2)) #-> {'a':{'b':2}}
set_by_path({'a':1}, ['b','c','d'], 2) #-> {'a':1, 'b':{'c':{'d'2}}}