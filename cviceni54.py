import sys
import csv

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} file_name")
        sys.exit(1)

    filename = sys.argv[1]
    base, ext = filename.split('.')
    newfile = f"{base}2.{ext}"

    with open(newfile, "w") as fw:
        writer = csv.writer(fw)
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                price = float(line[2])
                price *= 1.1
                line[2] = round(price, 2)
                writer.writerow(line)