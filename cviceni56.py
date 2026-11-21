from knihovna import jaccard


if __name__ == "__main__":

    data1 = ["aaa", "bbb", "ccc"]
    data2 = ["bbb", "ccc", "ddd"]
    data3 = ["ccc", "ddd", "eee"]

    print(jaccard(data1, data2))
    print(jaccard(data2, data3))
    print(jaccard(data1, data3))