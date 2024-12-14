import sys

def main():
    line_count = 0
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            for row in file:
                strip_row = row.strip()
                if not strip_row or strip_row.lstrip().startswith("#"):
                    continue
                line_count+=1
    except FileNotFoundError:
        sys.exit("File not found")

    print(line_count)

main()
