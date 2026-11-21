def jaccard(monzina1, monzina2):
    monzina1 = set(monzina1)
    monzina2 = set(monzina2)

    prunik = monzina1.intersection(monzina2)
    sjednoceni = monzina1.union(monzina2)

    jindex = len(prunik) / len(sjednoceni)
    jdistance = 1 - jindex
    return jdistance


if __name__ == "__main__":
    mnozina1 = [1,2,2,3,3,3]
    mnozina2 = [3,4,5,5]

    d = jaccard(mnozina1, mnozina2)
    print(d)