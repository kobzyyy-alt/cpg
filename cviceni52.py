if __name__ == "__main__":

    try:
        filename = input("Zadej jmeno souboru: ")
        fp = open(filename, "r")
        try:
            content = fp.read()
            print(content)
        except Exception:
            print("Chyba cteni")
        finally:
            fp.close()
    except FileNotFoundError:
        print("Soubor neexistuje")
    except Exception as e:
        print(type(e))
