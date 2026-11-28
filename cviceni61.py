from abc import ABC, abstractmethod

class Osoba(ABC):
    def __init__(self, jmeno, vek):
        self.jmeno = self.uprav_jmeno(jmeno)
        self.vek = vek

    def __str__(self):
        return f"Osoba {self.jmeno} ma {self.vek} let"

    def uprav_jmeno(self, jmeno):
        vysledne_jmeno = []
        for part in jmeno.split(" "):
            vysledne_jmeno.append(part.capitalize())
        return " ".join(vysledne_jmeno)

    def pridej_rok(self):
        self.vek += 1

    @abstractmethod
    def predstav_se(self):
        pass

class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f"Student {self.jmeno} ma {self.vek} let a je v {self.rocnik} rocniku"

    def __repr__(self):
        return f"Student<{self.jmeno}>"

    def pridej_rok(self):
        super().pridej_rok()
        if self.rocnik < 5:
            self.rocnik += 1

    def predstav_se(self):
        print(f"Jsem student {self.jmeno}")

class Ucitel(Osoba):
    def __init__(self, jmeno, vek, let_praxe):
        super().__init__(jmeno, vek)
        self.let_praxe = let_praxe

    def __str__(self):
        return f"Ucitel {self.jmeno} ma {self.vek} let a {self.let_praxe} let praxe"

    def __repr__(self):
        return f"Ucitel<{self.jmeno}>"

    def pridej_rok(self):
        super().pridej_rok()
        self.let_praxe += 1

    def predstav_se(self):
        print(f"Jsem ucitel {self.jmeno}")

if __name__ == "__main__":
    osoby = [
        Ucitel("karel", 50, 20),
        Student("Vlada", 44, 3),
        Student("Eva", 20, 1),
        Student("tomas novak", 18, 1),
    ]
    print(osoby)
    for osoba in osoby:
        osoba.pridej_rok()
        osoba.pridej_rok()
        osoba.pridej_rok()
        print(osoba)