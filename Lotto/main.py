import random

lottozahlen = [*range(1, 46, 1)]
gewinnerzahlen = []


def lottoziehung():
    for i in range(6):
        randnumb = random.choice(lottozahlen)
        gewinnerzahlen.append(randnumb)
        lottozahlen.remove(randnumb)
    return gewinnerzahlen


print(lottoziehung())
