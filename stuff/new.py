def generate_hashtag(s):
    if not s:
        return False
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

generate_hashtag('CodeWars is nice')