# zad 1

[] and {} or 3
# 3

[1] and None or []
# []

not (0 and None or 3)
# False


# zad 2

# miesiace = {'luty': 28, 'maj': 31, 'lipiec': 31, 'wrzesien': 55, 'listopad': 20}

# a)

[k for k in miesiace]
# ['luty', 'wrzesien', 'maj' itd.] kolejnosc jest przypadkowa

" and ".join(["%s in %s" % (v,k) for k,v in miesiace.items()])
# 28 in luty and 55 in wrzesien itd.

reduce(lambda x, y: x+y, miesiace.values())
# sumuje wartosci miesiecy
