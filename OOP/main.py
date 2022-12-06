class Person:
    def __init__(self, vorname, nachname, geschlecht):
        self.vorname = vorname
        self.nachname = nachname
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, geschlecht, firma):
        super().__init__(vorname, nachname, geschlecht)
        self.firma = firma


class Gruppenleiter(Mitarbeiter):
    def __init__(self, vorname, nachname, geschlecht, firma):
        super().__init__(vorname, nachname, geschlecht, firma)


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []

    def str(self):
        return f'Abteilung: {self.name}\n'


class Firma:
    def __init__(self, firmenname):
        self.firmenname = firmenname
        self.abteilungen = []
        self.mitarbeiter = []
        self.gruppenleiter = []

    def countmitarbeiter(self):
        count = 0
        for _ in self.mitarbeiter:
            count = count + 1
        return count

    def countgruppenleiter(self):
        count = 0
        for _ in self.gruppenleiter:
            count = count + 1
        return count

    def countabteilungen(self):
        count = 0
        for _ in self.abteilungen:
            count = count + 1
        return count

    def getstrength(self):
        last = self.abteilungen[0].mitarbeiter
        abteilungname = self.abteilungen[0].name
        for abteilung in self.abteilungen:
            if len(abteilung.mitarbeiter) > len(last):
                abteilungname = abteilung.name
        return abteilungname

    def getdifferencemanwoman(self):
        male = 0
        female = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht == "male":
                    male = male + 1
                else:
                    female = female + 1
        return {"male": male, "female": female}


f1 = Firma("Spacks und Pfusch GmbH & Co. KG")
a1 = Abteilung("Spackser")
a2 = Abteilung("Murkser")
m1 = Mitarbeiter("Mertos", "Certos", "male", f1)
m2 = Mitarbeiter("Leo", "Knurtschi", "female", f1)
m3 = Mitarbeiter("Kristof", "Furtzi", "female", f1)
g1 = Gruppenleiter("Dolm", "McDolm", "male", f1)
g2 = Gruppenleiter("Noah", "Stinki", "female", f1)

a1.mitarbeiter.append(m1)
a1.mitarbeiter.append(g1)
a2.mitarbeiter.append(m3)
a2.mitarbeiter.append(m2)
a2.mitarbeiter.append(g2)
f1.abteilungen.append(a1)
f1.abteilungen.append(a2)
f1.gruppenleiter.append(g1)
f1.gruppenleiter.append(g2)
f1.mitarbeiter.append(m1)
f1.mitarbeiter.append(m2)
f1.mitarbeiter.append(m3)

print(f1.firmenname)
print("Anzahl der Mitarbeiter: " + str(f1.countmitarbeiter()))
print("Anzahl der Gruppenleiter: " + str(f1.countgruppenleiter()))
print("Anzahl der Abteilungen: " + str(f1.countabteilungen()))
print("Mitarbeiterstärkste Abteilung: " + str(f1.getstrength()))
print("Prozentanteil Männer und Frauen: " + str(f1.getdifferencemanwoman()))
