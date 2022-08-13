import random
q = True
count = 0
while q:
    count += 1
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    d = random.randint(1,6)
    e = random.randint(1,6)

    if a == b and b == c and c == d and d == e and e == a:
        print('Yathzee')
        print(count)
        q = False

