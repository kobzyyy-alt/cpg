import os
import sys

if __name__ == "__main__":

    filename = input("Zadej jmeno souboru: ")

    if not os.path.exists(filename):
        print("Soubor neexistuje")
        sys.exit()

    fp = open(filename, "r")

    content = fp.read()
    if not content:
        print("Soubor nic neobsahuje")

    print(content)
    
    fp.close()