from tabulate import tabulate
import sys
import csv

def main():
    if len(sys.argv) != 2:
        sys.exit("Command length not valid, must be 2")
    else:
        if sys.argv[1] != "regular.csv" and sys.argv[1] != "sicilian.csv":
            sys.exit("Filename invalid or does not exist")
        else:
            sys.argv[1] == "regular.csv"
            with open (sys.argv[1]) as file:
                reader = csv.reader(file)
                table = tabulate(reader, headers="firstrow", tablefmt="grid")
                print(table)

main()
