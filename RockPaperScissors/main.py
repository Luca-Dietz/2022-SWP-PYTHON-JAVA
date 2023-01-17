import json
import random

import requests

gameselection = ['Stein', 'Echse', 'Spock', 'Schere', 'Papier']
playeroutcomes = []
pcoutcomes = []
playerpicks = []
pcpicks = []
difficultmode = False

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
    if int(answ) in [1, 2, 3, 4, 5]:
        return True
    else:
        return False


def playgame(difficultmode):
    print("1 | Stein\n2 | Echse\n3 | Spock\n4 | Schere\n5 | Papier")
    answer = input("Enter your selection: ")
    if not validateinput(answer):
        print("Wrong input")
        playgame(difficultmode)
    if difficultmode:
        fnlist = []
        locallist = []
        weight = []
        data = requests.get("http://localhost:5000/").content
        json_data = json.loads(data)
        fnlist.append(json_data["Stein"])
        fnlist.append(json_data["Echse"])
        fnlist.append(json_data["Spock"])
        fnlist.append(json_data["Schere"])
        fnlist.append(json_data["Papier"])
        for a in fnlist:
            locallist.append(a / sum(fnlist) * 100)
        for i in range(len(fnlist)):
            weight.append((locallist[(i + 1) % 5]) + (locallist[(i + 3) % 5]))
        print("Difficult mode activated")
        generated = random.choices(gameselection, weights=weight)[0]
    else:
        generated = random.choice(gameselection)
    print("Computer has chosen: " + str(generated))
    player = int(answer)-1
    if gameselection[(player + 1) % 5] == generated or gameselection[(player + 3) % 5] == generated:
        print("You won")

        playeroutcomes.append("win")
        pcoutcomes.append("lose")
    elif generated == answer:
        print("same")

        playeroutcomes.append("same")
        pcoutcomes.append("same")
    else:
        print("You lost")
        playeroutcomes.append("lose")
        pcoutcomes.append("win")
    playerpicks.append(answer)
    pcpicks.append(generated)
    playagain = input("Do you want to play again: (y/n)")
    if playagain == "y":
        playgame(difficultmode)
    else:
        maingame(difficultmode)


def choosedifficultmode():
    ans = input("Do you want to play difficultmodemode? (y/n): ")
    if ans == "y":
        difficultmode = True
        playgame(difficultmode)
    else:
        difficultmode = False
        playgame(difficultmode)


def maingame(difficultmode):
    print_menu()
    option = int(input('Enter your choice: '))
    if option == 1:
        choosedifficultmode()
    elif option == 2:
        data = requests.get("http://localhost:5000/").content
        json_data = json.loads(data)
        print("\nWin\tLose\tStein\tSchere\tPapier\tEchse\tSpock\t")
        print(str(json_data["win"]) + "\t" + str(json_data["lose"]) + "\t\t" + str(json_data["Stein"]) +
              "\t\t" + str(json_data["Schere"]) + "\t\t" + str(json_data["Papier"]) + "\t\t" + str(json_data["Echse"]) +
              "\t\t" + str(json_data["Spock"]) + "\n")
        maingame(difficultmode)
    elif option == 3:
        result = requests.post("http://localhost:5000/", data=json.dumps({"playerpicks": playerpicks,
                                                                          "pcpicks": pcpicks,
                                                                          "playeroutcomes": playeroutcomes,
                                                                          "pcoutcomes": pcoutcomes}))
        if result.status_code == 200:
            print("\nData sent Succesfully\n")
        else:
            print("\nFailed\n")
        maingame(difficultmode)
    elif option == 4:
        print('Thanks for playing')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')


if __name__ == "__main__":
    maingame(difficultmode)
