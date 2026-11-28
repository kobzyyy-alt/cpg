class Auto:
    def __init__(self, zn, model, barva):
        self.znacka = zn
        self.model = model
        self.barva = barva

    def vrat_popis(self):
        return f"Auto: {self.znacka} {self.model} {self.barva}"


if __name__ == "__main__":
    a1 = Auto("Toyota", "Corola", "cervena")
    a2 = Auto("Ford", "Focus", "modra")
    a3 = Auto("Skoda", "Fabia", "bila")

    print(a1.barva)
    print(a1.vrat_popis())
    print(a2.vrat_popis())
    print(a3.vrat_popis())
    print(Auto.vrat_popis(a3))