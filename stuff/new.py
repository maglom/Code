def title_case(title, minor_words=''):
    ls = title.split()
    bs = []
    minor_words = minor_words.split()
    for c,i in enumerate(minor_words):
        minor_words[c] = i.lower()
    for i in ls:
        if i.lower() in minor_words[1:]:
            bs.append(i.lower())
        else:
            bs.append(i.capitalize())
    return ' '.join(bs)

title_case('THE WIND IN THE WILLOWS', 'The In')