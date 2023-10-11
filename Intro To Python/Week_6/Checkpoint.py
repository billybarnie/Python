with open("books.txt") as mormon:
    for line in mormon:
        line = line.strip()
        name = line
        print(name)