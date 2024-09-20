class test:

    def __init__(self, name):
        self.__name = name


p1 = test("m")
# if p1 != None:
#     raise ValueError("bereits vergeben")
# else:
#     print("ja")'

class prüfen:
    def __init__(self):
        self.__zupruefendesObjekt = None

    def prüfen(self, objekt):
        if objekt is not isinstance(objekt, test):
            print ("nein")
        else:
            print("ja")

prüfen.prüfen("p1")