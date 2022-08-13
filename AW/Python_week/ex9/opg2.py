dic = {}

while True:
    keyvalue = input('Input key;value')

    if keyvalue == 'revert':
        print(dic)
        dicc = {}
        for i in dic:
            dicc[dic[i]] = i
        print(dicc)
        break

    ls = keyvalue.split(';')

    dic[ls[0]] = ls[1]

