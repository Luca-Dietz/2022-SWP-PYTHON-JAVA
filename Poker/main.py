import random

yourhandsymbols = []
yourhandvalue = []


def getsymbolofnumber(numbers):
    numbers %= 4
    if numbers == 0:
        return "Herz"
    if numbers == 1:
        return "Kreuz"
    if numbers == 2:
        return "Karo"
    if numbers == 3:
        return "Pik"


def getcardnumber(number):
    number %= 13
    return number


def getcards(min, max, cardsquanitity):
    cards = []
    for i in range(min, max + 1):
        cards.append(i)
    for j in range(cardsquanitity):
        zufallsindex = random.randrange(0, max - min + 1)
        lastPosition = len(cards) - 1 - j
        cards[zufallsindex], cards[lastPosition] = cards[lastPosition], cards[zufallsindex]
    return cards[-cardsquanitity:]


def sameinlist(list):
    firstelement = list[0]
    for i in list:
        if firstelement != i:
            return False
    return True


def checkforcard(list, values):
    if list == values:
        return True


def checkforstreet(list):
    list.sort()
    for i in range(8):
        for a in range(i, i + 5):
            if list == [a, a + 1, a + 2, a + 3, a + 4]:
                return True


def checkfororders(symbols, values):
    if sameinlist(symbols):
        if checkforcard(values, [8, 9, 10, 11, 12]):
            print("Royal Flush")
        elif checkforstreet(values):
            print("Straight Flush")


if __name__ == "__main__":
    yourCards = getcards(1, 52, 5)
    for i in yourCards:
        yourhandvalue.append(getcardnumber(i))
        yourhandsymbols.append(getsymbolofnumber(i))


checkfororders(yourhandsymbols, yourhandvalue)
