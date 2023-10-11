import csv

def main():
    
    user = input("What is your user I-Number? ")

    students = read_dictionary("students.csv")

    user = user.replace("-", "")

    if not user.isdigit():
        print("Invalid I-Number")
    else:
        if len(user) < 9:
            print("Invalid I-Number")
        elif len(user) > 9:
            print("Invalid I-Number")
        else:
            if user not in students:
                print("Student doesn't exist")
            else:
                key = students[user]
                name = key[1]

                print(f"Welcome: {name}")

    print(students)


def read_dictionary(filename):

    dictionary = {}

    with open(filename, "rt") as studentfile:

        student = csv.reader(studentfile)

        next(student)

        for line in student:

            key = line[0]

            dictionary[key] = line[1]
            
    return dictionary

if __name__ == "__main__":
    main()