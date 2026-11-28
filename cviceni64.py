class Ucet:
    def __init__(self, pocatecni_zustatek=0):
        self.__zustatek = pocatecni_zustatek

    @property
    def zustatek(self):
        return self.__zustatek

    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota > 0:
            self.__zustatek = hodnota


if __name__ == "__main__":

    u = Ucet(1000)
    print(u.zustatek)

    u.zustatek = 100
    print(u.zustatek)
    
    u.zustatek = -100
    print(u.zustatek)