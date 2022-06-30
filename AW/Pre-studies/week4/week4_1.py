from collections import defaultdict

class MyCounter:
    
    def __init__(self, input):
        self.input = input

        self.dic = defaultdict(int)
        for i in self.input:
            self.dic[i] += 1    

    def get(self, key):
        if self.dic[key] == 0:
            return 'Key not found'
        else:
            return self.dic[key]
            
    def __str__(self):
        return 'Here is the count {}'.format(self.dic)


