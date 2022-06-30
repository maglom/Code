def title_case(title, minor_words=''):
    ls = title.split()
    bs = []
    minor_words = minor_words.split()
    for i in ls:
        if i in minor_words[1:]:
            bs.append(i.lower())
        else:
            bs.append(i.capitalize())
    return ' '.join(bs)

title_case('THE WIND IN THE WILLOWS', 'The In')