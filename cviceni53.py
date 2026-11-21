if __name__ == "__main__":

    while True:
        filename = input("Zadej jmeno souboru: ")
        #text = input("Zadej text: ")
        try:
            with open(filename, "r") as fp:
                for line in fp:
                    print("Radek: " + line)
            break
        except FileNotFoundError:
            print("Soubor neexistuje")