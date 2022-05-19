# Coding Challenge 3 - Dictonaries and key-value inputs

dic = {}

while True:
    userinput = input("If you want to print the dictonary enter PRINT NOW \nEnter a key-value pair: ")
    if len(userinput.split()) != 2:
        print("Only two words are accepted")
    elif userinput == "PRINT NOW":
        print(dic)
    elif userinput[0] not in dic:
        dic[userinput[0]] = list(userinput[1])
    else:
        dic[userinput[0]] = dic[userinput[0]].append(userinput[1])
    