import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SchereSteinPapier"
)

mycursor = mydb.cursor()

gameselection = ['Stein', 'Schere', 'Papier', 'Echse', 'Spock']
w = 0
l = 0
s = 0


def game(yourpick):
    if yourpick == 'Stein':
        return 'Echse', 'Schere'
    if yourpick == 'Schere':
        return 'Papier', 'Echse'
    if yourpick == 'Papier':
        return 'Stein', 'Spock'
    if yourpick == 'Echse':
        return 'Spock', 'Papier'
    if yourpick == 'Spock':
        return 'Schere', 'Schere'


def validateinput(answ):
    if answ not in gameselection:
        return False
    else:
        return True

def getdata():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from playerdata")
    myresult = mycursor.fetchall()
    mycursor.execute("SELECT * from pcdata")
    myresult2 = mycursor.fetchall()
    return myresult, myresult2

def showdata():
    pass

def maingame(w, l, s):
    print("Stein Schere Papier Echse Spock")
    answer = input("Enter your selection: ")
    if not validateinput(answer):
        print("Wrong input")
        maingame(w, l, s)
    generated = random.choice(gameselection)
    print("Computer has chosen: " + generated)
    if generated in game(answer):
        print("You won")
        w = w + 1
        print(w)

        sql = "INSERT INTO playerdata(outcome, pick) VALUES (%s, %s)"
        val = ("win", answer)

        sql2 = "INSERT INTO pcdata(outcome, pick) VALUES (%s, %s)"
        val2 = ("lose", generated)
    elif generated == answer:
        print("same")
        s = s + 1
        print(s)

        sql = "INSERT INTO playerdata(outcome, pick) VALUES (%s, %s)"
        val = ("same", answer)

        sql2 = "INSERT INTO pcdata(outcome, pick) VALUES (%s, %s)"
        val2 = ("same", generated)
    else:
        print("You lost")
        l = l + 1
        print(l)

        sql = "INSERT INTO playerdata(outcome, pick) VALUES (%s, %s)"
        val = ("lose", answer)

        sql2 = "INSERT INTO pcdata(outcome, pick) VALUES (%s, %s)"
        val2 = ("win", generated)
    mycursor.execute(sql, val)
    mycursor.execute(sql2, val2)

    mydb.commit()
    maingame(w, l, s)


if __name__ == "__main__":
    #maingame(w, l, s)
    print(getdata()[0][0][0])
