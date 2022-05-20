# Coding Challenge 3 - Dictonaries and key-value inputs

dic = {}

while True:
    ls = input("If you want to print the dictonary enter PRINT NOW \nEnter a key-value pair: ")
    ls = ls.split()
    if len(ls) != 2:
        print("Only two words are accepted")
    elif ls[0] == "PRINT" and ls[1] == "NOW":
        print(dic)
        print("To end the program press ctrl+c")
    elif ls[0] not in dic:
        dic[ls[0]] = [ls[1]]
    else:
        dic[ls[0]] = dic[ls[0]] + [ls[1]]
        