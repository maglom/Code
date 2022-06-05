from collections import defaultdict

from collections import defaultdict

class MyCounter:
    
    

    def __init__(self, input):
        self.input = input
        dic = defaultdict(lambda: 'Key not found')
        for i in input:
            dic[i] = dic[i] + 1

    def get(self, key):
        print(dic[key])

    def __str__(self):
        print(dic)

x = MyCounter([1, 2, 1, 3])

x.get(1)