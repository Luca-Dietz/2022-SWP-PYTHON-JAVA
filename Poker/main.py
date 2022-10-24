import random

yourhandsymbols = []
yourhandvalue = []
yourhand = []
lastcard = []


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


def getcards(mind, maxi, cardsquanitity):
    cards = []
    for g in range(mind, maxi + 1):
        cards.append(g)
    for j in range(cardsquanitity):
        zufallsindex = random.randrange(0, maxi - mind + 1)
        lastPosition = len(cards) - 1 - j
        cards[zufallsindex], cards[lastPosition] = cards[lastPosition], cards[zufallsindex]
    return cards[-cardsquanitity:]


def getrealvalue(value):
    realvalue = value + 2
    if realvalue == 11:
        return "J"
    if realvalue == 12:
        return "Q"
    if realvalue == 13:
        return "K"
    if realvalue == 14:
        return "Ass"
    return realvalue


def checkforpairs(values):
    duplicates = [number for number in values if values.count(number) > 1]
    unique_duplicates = list(set(duplicates))
    return len(duplicates), unique_duplicates


def checkfororders(symbols, values):
    orders = False
    if symbols.count(symbols[0]) == len(symbols):
        symbols.sort()
        if values[0] == values[-1] - 4 and values[-1] == 12:
            print("Royal Flush")
            orders = True
        elif values[0] == values[-1] - 4:
            print("Straight Flush")
            orders = True
        elif not orders:
            print("Flush")
    if checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) == 1:
        print("Vierling")
        orders = True
    elif checkforpairs(values)[0] == 5 and len(checkforpairs(values)[1]) >= 2:
        print("Full House")
        orders = True
    elif checkforpairs(values)[0] == 3:
        print("Drilling")
        orders = True
    elif checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) >= 2:
        print("Zwei Paare")
        orders = True
    elif checkforpairs(values)[0] == 2:
        print("Paar")
        orders = True
    if not orders:
        print("Highest Card: " + getrealvalue(max(values)))


if __name__ == "__main__":
    yourCards = getcards(1, 52, 5)
    for i in yourCards:
        yourhandvalue.append(getcardnumber(i))
        yourhandsymbols.append(getsymbolofnumber(i))
        yourhand.append([getrealvalue(getcardnumber(i)), getsymbolofnumber(i)])
    checkfororders(yourhandsymbols, yourhandvalue)
    # yourhand = sorted(yourhand, key=lambda l: l[0])
    print(yourhand)
    yourhandvalue = []
    yourhandsymbols = []
