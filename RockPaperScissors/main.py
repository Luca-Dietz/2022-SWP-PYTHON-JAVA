import random

from server import getdata, uploaddata, mydb

gameselection = ['Stein', 'Echse', 'Spock', 'Schere', 'Papier']
playeroutcomes = []
pcoutcomes = []
playerpicks = []
pcpicks = []
sorted = []
weight = []
locallist = []
w = 0
l = 0
s = 0
hard = False

menu_options = {
    1: 'Play Game',
    2: 'Get Data',
    3: 'Upload Data',
    4: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def validateinput(answ):
    if answ not in gameselection:
        return False
    else:
        return True


def playgame(w, l, s, hard):
    print("Stein Echse Spock Schere Papier")
    answer = input("Enter your selection: ")
    if not validateinput(answer):
        print("Wrong input")
        playgame(w, l, s, hard)
    if hard:
        sorted = []
        locallist = []
        weight = []
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from playerdata")
        myresult = mycursor.fetchall()
        for i in gameselection:
            sorted.append([el[2] for el in myresult].count(i))
        for a in sorted:
            locallist.append(a / sum(sorted) * 100)
        for i in range(len(sorted)):
            weight.append((locallist[(i + 1) % 5]) + (locallist[(i + 3) % 5]))
        print("Hardmode activated")
        generated = random.choices(gameselection, weights=weight)[0]
    else:
        generated = random.choice(gameselection)
    print("Computer has chosen: " + str(generated))
    player = gameselection.index(answer)
    if gameselection[(player + 1) % 5] == generated or gameselection[(player + 3) % 5] == generated:
        print("You won")
        w = w + 1
        print(w)
        playeroutcomes.append("win")
        pcoutcomes.append("lose")
    elif generated == answer:
        print("same")
        s = s + 1
        print(s)
        playeroutcomes.append("same")
        pcoutcomes.append("same")
    else:
        print("You lost")
        l = l + 1
        print(l)
        playeroutcomes.append("lose")
        pcoutcomes.append("win")
    playerpicks.append(answer)
    pcpicks.append(generated)
    playagain = input("Do you want to play again: (y/n)")
    if playagain == "y":
        playgame(w, l, s, hard)
    else:
        maingame(w, l, s, hard)


def choosedifficulty(w, l, s, hard):
    ans = input("Do you want to play easy or hard? (y/n): ")
    if ans == "y":
        hard = True
        playgame(w, l, s, hard)
    else:
        hard = False
        playgame(w, l, s, hard)


def maingame(w, l, s, hard):
    print_menu()
    option = int(input('Enter your choice: '))
    if option == 1:
        choosedifficulty(w, l, s, hard)
    elif option == 2:
        getdata(gameselection)
    elif option == 3:
        uploaddata(playerpicks, playeroutcomes, pcpicks, pcoutcomes)
    elif option == 4:
        print('Thanks for playing')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')


if __name__ == "__main__":
    maingame(w, l, s, hard)
