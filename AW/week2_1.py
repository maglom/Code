# Coding Challenge 1 - Legal Driling Age

while True:
    name = input("What is your name?: ").strip()
    if len(name.split()) == 2:
        break
    else:
        print("Name must consist of two words")
year = int(input("What year are you born?: ").strip())
place = input("Where do you live?: ").strip().lower()

def legalage(name, year, place):
    if place == "norway":
        if year > 2004:
            print(f"{name} is too young to drink")
        else:
            print(f"{name} is old enough to drink")
    else:
        if year > 2001:
            print(f"{name} is too young to drink")
        else:
            print(f"{name} is old enough to drink")

legalage(name, year, place)


