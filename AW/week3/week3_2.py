def formattext(text):
    ls = text.split()
    bs = []
    for i in ls:
        if i[0] == "_":
            bs.append(i[1:-1].upper())
        elif i[0] == "#":
                bs.append(i[1:-1].lower())
        else:
            bs.append(i)
    return print(" ".join(bs))

formattext("Everyone _said_ that it would not work. Then someone came, #UNAWARE# of what everyone said, and just did it.")