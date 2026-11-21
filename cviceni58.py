import json


if __name__ == "__main__":

    data = {"jmeno": "Vlada", "vek": 44}

    print(data)
    print(type(data))

    json_data = json.dumps(data)
    print(json_data)
    print(type(json_data))

    with open("data.json", "w") as f:
        f.write(json_data)

    with open("data.json", "r") as f:
        read_data = f.read()

    print(read_data)
    print(type(read_data))

    new_data = json.loads(read_data)
    print(new_data)
    print(type(new_data))