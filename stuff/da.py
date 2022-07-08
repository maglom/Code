def order(sentence):
    ls = sentence.split()
    ls.sort(key=comp)
    return ' '.join(ls)

def comp(o):
    for i in o:
        if i in '123456789':
            return int(i)

order("is2 Thi1s T4est 3a")