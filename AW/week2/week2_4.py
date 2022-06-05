from collections import defaultdict

dic = defaultdict(list)

print("If you want to print the dictonary enter PRINT NOW")

while True:
    ls = input("Enter a key-value pair: ")
    print("To end the program press ctrl+c")
    ls = ls.split()
    if len(ls) != 2:
        print("Only two words are accepted")
    elif ls[0] == "PRINT" and ls[1] == "NOW":
        print(dic)  
    else:
        dic[ls[0]] = dic[ls[0]] + [ls[1]]
        