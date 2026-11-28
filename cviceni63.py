import json

class Osoba:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def __str__(self):
        return f"Osoba {self.jmeno} {self.prijmeni} ma {self.vek} let"

    def __eq__(self, other):
        return self.jmeno == other.jmeno and self.prijmeni == other.prijmeni and self.vek == other.vek

    @classmethod
    def from_json(cls, data):
        try:
            data = json.loads(data)
            if 'jmeno' in data and 'prijmeni' in data and 'vek' in data:
                return cls(data['jmeno'], data['prijmeni'], data['vek'])
        except Exception:
            return None


if __name__ == "__main__":
    o1 = Osoba("Jan", "Novak", 20)
    o2 = Osoba("Jan", "Novak", 20)
    print(o1 == o2)
    # with open("osoby.json", "r") as f:
    #     for line in f:
    #         o = Osoba.from_json(line)
    #         print(o)
