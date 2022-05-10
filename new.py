def decode_morse(morse_code):
    prev = None
    ls = [x for x in morse_code]
    bs = "".join(ls)
    ls = []
    ls = bs.split(" ")
    for x,i in enumerate(ls):
        if i == "" and prev == "":
            ls.pop(x)
        prev = i

    bs = []
    for i in ls:
        if i == "":
            bs.append(" ")
        else:
            bs.append(MORSE_CODE[i])
    return "".join(bs)

decode_morse('...   ---   ...')