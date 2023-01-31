class listenlement:
    def __init__(self, obj):
        # Initialisieren eines Listenelements mit einem Objekt
        self.obj = obj
        self.nextelem = None

    def setnextelem(self, nextelem):
        # Setzen des nächsten Listenelements
        self.nextelem = nextelem

    def getnextelem(self):
        # Rückgabe des nächsten Listenelements
        return self.nextelem

    def getobj(self):
        # Rückgabe des Objekts
        return self.obj


class VListe:
    def __init__(self):
        # Initialisieren der einfach verketteten Liste mit einem "Kopf"-Element
        self.startElem = listenlement("Kopf")

    def addlast(self, o):
        # Neues Element wird erstellt
        newElem = listenlement(o)
        # Das letzte Element in der Liste wird ermittelt
        lastElem = self.getlastelem()
        # Das neue Element wird als nächstes Element des letzten Elements in der Liste gesetzt
        lastElem.setnextelem(newElem)

    # Methode insertAfter, fügt ein neues Element nach einem bestimmten Element ein
    def insertafter(self, previtem, newitem):
        # Neues Element wird erstellt
        newElem = listenlement(newitem)
        # Pointer auf das aktuelle Element
        pointerElem = self.startElem.getnextelem()
        # Solange das nächste Element nicht None ist UND das aktuelle Element nicht dem gesuchten entspricht
        while pointerElem is not None and pointerElem.getobj() != previtem:
            # Pointer wird auf das nächste Element gesetzt
            pointerElem = pointerElem.getnextelem()
        # Nächstes Element nach dem gefundenen
        nextElem = pointerElem.getnextelem()
        # Neues Element wird als nächstes Element des gefundenen gesetzt
        pointerElem.setnextelem(newElem)
        # Das nächste Element des neuen Elements wird auf das alte nä
        newElem.setnextelem(nextElem)

    def delete(self, o):
        # Löschen eines bestimmten Elements aus der Liste
        le = self.startElem
        # Durchlaufen der Liste
        while le.getnextelem() is not None and le.getobj() != o:
            if le.getnextelem().getobj() == o:
                if le.getnextelem().getnextelem() is not None:
                    # Setzen des Verweises des vorherigen Elements auf das nächste Element nach dem zu löschenden
                    le.setnextelem(le.getnextelem().getnextelem())
                else:
                    le.setnextelem(None)
                    break
            le = le.getnextelem()

    def find(self, o):
        # Suchen eines bestimmten Elements in der Liste
        le = self.startElem
        # Durchlaufen der Liste
        while le is not None:
            if le.getobj() == o:
                return True
            le = le.nextelem
        return False

    def getfirstelem(self):
        # Rückgabe des ersten Listenelements
        return self.startElem

    def getlastelem(self):
        # Rückgabe des letzten Listenelements
        le = self.startElem
        while le.getnextelem() is not None:
            le = le.getnextelem()
        return le

    def writelist(self):
        # Ausgabe des Listenobjekts
        le = self.startElem
        while le is not None:
            print(le.getobj())
            le = le.getnextelem()


if __name__ == "__main__":
    vlist = VListe()
    vlist.addlast("1")
    vlist.addlast("2")
    vlist.addlast("3")
    vlist.addlast("4")
    vlist.addlast("5")
    vlist.insertafter("2", "neu")
    vlist.delete("2")
    vlist.writelist()
    print("erstes Element: " + vlist.getfirstelem().getobj())
    print("ist '3' enthalten? " + str(vlist.find("3")))


