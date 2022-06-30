from collections import defaultdict

def my_counter(x):
    dic = defaultdict(int)
    for i in x:
        dic[i] = dic[i] + 1
    return print(dic)

my_counter([1, 2, 1, 3])