def generate_hashtag(s):
    if not s:
        return False
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> windows
    bs = []
    ls = s.split(' ')
    for c,i in enumerate(ls):
        print(c,i)
        if i:
            bs.append(list(i))
    for idx,word in enumerate(bs):
        bs[idx] = ''.join(word).capitalize()
    bs.insert(0, '#')
    return ''.join(bs)

<<<<<<< HEAD
generate_hashtag('CodeWars is nice')
=======
    ls = s.split(' ')
    for c,i in enumerate(ls):
        ls[c] = list(i)
        ls[c][0] = ls[c][0].upper()
    for c,i in enumerate(ls):
        ls[c] = ''.join(i)
    ls.insert(0,'#')
    return ''.join(ls)

generate_hashtag('codewars is nice')
>>>>>>> 7f697ec4332dbfd30665455ce8aaf6b77e6f50dc
=======
generate_hashtag('CodeWars is nice')
>>>>>>> windows
