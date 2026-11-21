import random

if __name__ == "__main__":

    symboly = ["+", "-", "*", "x"]
    while True:
        choice = []
        for x in range(3):
            choice.append(random.choice(symboly))
        print(choice)
        if len(set(choice)) == 1:
            print("Vyhral jsi")
            break