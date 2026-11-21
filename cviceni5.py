def conversion(value):
    try:
        value = int(value)
    except ValueError:
        value = 0
    return value


def division(a, b):
    a = conversion(a)
    b = conversion(b)
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    return c


if __name__ == "__main__":

    try:

        data = ["10", "5", "A", "0", "3"]
        numbers = []

        for value in data:
            try:
                number = division(10, value)
            except ValueError:
                print(f"Nelze zkonvertovat textovou hodnotu '{value}' na cislo")
                continue
            except ZeroDivisionError:
                print(f"Nelze delit nulou")
                continue
            numbers.append(number)

        print(numbers)

    except Exception as e:
        print(f"Nastala neocekavana chyba {e}")