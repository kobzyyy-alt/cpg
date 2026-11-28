class ZapornaCastka(Exception):
    pass

class NedostatecnyZustatek(Exception):
    pass

class Ucet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je {self.__zustatek}"

    def vloz(self, castka):
        if castka < 0:
            raise ZapornaCastka("Nelze vlozit zapornou castku")
        self.__zustatek += castka

    def vyber(self, castka):
        if castka < 0:
            raise ZapornaCastka("Nelze vybrat zapornou castku")
        if castka > self.__zustatek:
            raise NedostatecnyZustatek("Nelze vybrat vice nez je zustatek")
        self.__zustatek -= castka

if __name__ == "__main__":
    u1 = Ucet("Osobni")
    while True:
        try:
            prikaz = input("Zadej prikaz: ")
            if prikaz == "vloz":
                castka = int(input("Zadej castku: "))
                u1.vloz(castka)
            elif prikaz == "vyber":
                castka = int(input("Zadej castku: "))
                u1.vyber(castka)
            elif prikaz == "konec":
                break
            else:
                print("Neplatny prikaz!")
        except ZapornaCastka:
            print("Nelze pouzit zapornou castku!")
        except NedostatecnyZustatek:
            print("Nemate dost prostredku na ucte!")

