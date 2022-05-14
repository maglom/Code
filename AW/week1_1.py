import random

health = 100
attack1 = random.randint(20,30)
attack2 = random.randint(20,30)
healthpotion = 10 + random.randint(10,15)

output = health - attack1 - attack2 + healthpotion

print(output)

