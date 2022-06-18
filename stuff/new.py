from collections import Counter
class MyCounter:
    def __init__ (self, string=''):
        dictionary = {}
        for i in string:
            keys = dictionary.keys()
            if i in keys:
                dictionary[i] +=1
            else:
                dictionary[i] =1
        self.dictionary= dictionary
    def get (self,key):
        return self.dictionary [key]
my_counter = MyCounter(string =input("Skriv et ord: "))
print (my_counter.dictionary)
key = input("Skriv en bokstav: ")
if key in my_counter.dictionary:
    print (my_counter.dictionary[key])
else:
    print ("Denne bokstaven er ikke der")

x = MyCounter([1, 2, 3, 3])

x.get(1)