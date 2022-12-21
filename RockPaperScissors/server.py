import json

import flask
import mysql.connector
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SchereSteinPapier"
)

mycursor = mydb.cursor()


def getdata(gameselection):
    playerpicks = []
    pcpicks = []
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from playerdata")
    myresult = mycursor.fetchall()
    mycursor.execute("SELECT * from pcdata")
    myresult2 = mycursor.fetchall()
    length = len(myresult)
    playeroutcomes = [el[1] for el in myresult].count("win")
    for i in gameselection:
        playerpicks.append(i + " : " + str([el[2] for el in myresult].count(i)))
        pcpicks.append(i + " : " + str([el[2] for el in myresult2].count(i)))
    pcoutcomes = [el[1] for el in myresult2].count("win")
    print("\n STATISTICS \n")
    print("Games played: " + str(length) + "\n")
    print("(PLAYER) Win chance: " + str((playeroutcomes / length * 100).__floor__()) + "% | " + str(playerpicks) + "\n")
    print("(PC) Win chance: " + str((pcoutcomes / length * 100).__floor__()) + "% | " + str(pcpicks) + "\n")


def uploaddata(playerpicks, playeroutcomes, pcpicks, pcoutcomes):
    if len(playerpicks) == 0:
        print("\n NO DATA TO UPLOAD! \n")
    else:
        for i in range(len(playerpicks)):
            val = (playeroutcomes[i], playerpicks[i])
            val2 = (pcoutcomes[i], pcpicks[i])
            sql = "INSERT INTO playerdata(outcome, pick) VALUES (%s, %s)"
            sql2 = "INSERT INTO pcdata(outcome, pick) VALUES (%s, %s)"
            mycursor.execute(sql, val)
            mycursor.execute(sql2, val2)
            mydb.commit()
        print("\n DATA UPLOADED SUCCESSFULLY! \n")


def show_all_data():
    mycursor.execute("SELECT * FROM playerdata")
    result = mycursor.fetchall()
    tmplist = []
    dict = {
        "win": 0,
        "lose": 0,
        "Stein": 0,
        "Schere": 0,
        "Papier": 0,
        "Echse": 0,
        "Spock": 0
    }
    for row in result:
        t = (row[0], row[1], row[2])
        tmplist.append(t)
    for i in tmplist:
        if i[1] == "win":
            dict["win"] += 1
        else:
            dict["lose"] += 1
        if i[2] == "Stein":
            dict["Stein"] += 1
        elif i[2] == "Schere":
            dict["Schere"] += 1
        elif i[2] == "Papier":
            dict["Papier"] += 1
        elif i[2] == "Echse":
            dict["Echse"] += 1
        elif i[2] == "Spock":
            dict["Spock"] += 1
    j = json.dumps(dict)
    return j


class ssp(Resource):
    def get(self):
        dic = show_all_data()
        return "Player data: " + dic


api.add_resource(ssp, '/')

if __name__ == '__main__':
    app.run()