from collections import Counter
def anagrams(word, words):
    bs = []
    x = Counter(word)
    for w in words:
        c = Counter(w)
        status = True
        for letter in w:
            if c[letter] != x[letter]:
                status = False
        if status == True:
            bs.append(w)
    return bs


anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])