from typing import MutableMapping

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

dic = dic1 | dic2 | dic3

def flatten_dict(dic):
    output = {}
    for key, value in dic.items():
        for subkey, subvalue in value.items():
            newkey = key + subkey 
            output[newkey] = subvalue
    return output

input_dict = { 
'a':{'d':1, 'e':2}, 
'b':{'f':3}, 
'c':{'g':4, 'h':5} 
} 

print(flatten_dict(input_dict))