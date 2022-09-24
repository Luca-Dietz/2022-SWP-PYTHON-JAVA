import random

gewinnerzahlen = []
statistik = {}

def create_dict():
    for a in range(1, 46):
        statistik[a] = 0

def lottoziehung():
    lottozahlen = [*range(1, 46, 1)]
    gewinnerzahlen.clear()
    for i in range(6):
        randnumb = random.choice(lottozahlen)
        gewinnerzahlen.append(randnumb)
        lottozahlen.remove(randnumb)
    return gewinnerzahlen

def statistik1000():
    for x in range(1000):
        zahlen = lottoziehung()
        for f in range(6):
            for key, value in statistik.items():
                if zahlen[f] == key:
                    statistik[key] += 1
    return statistik

create_dict()
print("Lottoziehung: " + str(lottoziehung()))
print("Statistik bei 1000: " + str(statistik1000()))

