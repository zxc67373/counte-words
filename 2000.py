word = "abcdefd"
ch = "d"
def a(word,ch):
    if ch in word:
        pos = word.index(ch)
        l  = word[:pos+1]
        l2 = list(l)
        l3 = l2.reverse()
        return str(l) + word[pos:]
    else:
        return word
print(a(word,ch))