def generate_hashtag(s):
    if not s:
        return False
    ls = s.split(' ')
    for c,i in enumerate(ls):
        ls[c] = list(i)
        ls[c][0] = ls[c][0].upper()
    for c,i in enumerate(ls):
        ls[c] = ''.join(i)
    ls.insert(0,'#')
    return ''.join(ls)

generate_hashtag('codewars is nice')