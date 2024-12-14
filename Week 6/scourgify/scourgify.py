import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Invalide arg length")
    else:
        with open(sys.argv[1]) as first_file:
            reader = csv.DictReader(first_file)

            with open(sys.argv[2], "w") as second_file:
                writer = csv.DictWriter(second_file, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
main()
