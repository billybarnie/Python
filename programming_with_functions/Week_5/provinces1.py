import csv

def main():

    province = list_of_provinces("provinces.txt")


    print(province)

    # Removes the first item in the list
    province.pop(0)

    # Removes the last item in the list
    province.pop()

    # Replaces all occurrences of "AB" with "Alberta"
    for i in range(len(province)):
        if province[i] == "AB":
            province[i] = "Alberta"

    add = province.count("Alberta")

    print()
    print(f"Alberta occurs {add} times")

def list_of_provinces(filename):

    # Empty list
    provinces = []

    # Opens the text file for reading and applies a reference named "text_file"
    with open(filename, "rt") as text_file:

        # Reads the contents of the file one line after the next
        for line in text_file:
            
            # Removes any white space
            strip = line.strip()

            # Adds the strip line to the end of the list
            provinces.append(strip)

    return provinces


if __name__ == "__main__":
    main()