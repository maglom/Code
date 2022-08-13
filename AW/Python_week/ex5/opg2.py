import random

count = 0


while True:
    count += 1
    dice = [1,2,3,4,5,6]
    n_dices = 5
    rand_dices = random.choices(dice, k=n_dices)
    print('Min = ', min(sorted(rand_dices)),'Max = ', max(sorted(rand_dices)), sorted(rand_dices))


    if rand_dices.count(rand_dices[0]) == len(rand_dices):
        print('Yathzee')
        print(count)
        count = 0
        break


