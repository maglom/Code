# Coding Challange 2 - List of Names

ls = []
try:
    while True:
        userinput = input("Enter a name or enter PRINT to see saved names: ")
        if userinput == "PRINT":
            print(ls)
        else:
            ls.append(userinput)
            print("To end the program press ctrl+c")
except:
    print(f"\nHere are all the wonderful names you entered: {ls}")
