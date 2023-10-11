
def main():
    add = 0
    add += positive("I feel that I am a person of worth, at least on an equal plane with others. ")
    add += positive("I feel that I have a number of good qualities. ")
    add += negative("All in all, I am inclined to feel that I am a failure. ")
    add += positive("I am able to do things as well as most other people. ")
    add += negative("I feel I do not have much to be proud of. ")
    add += positive("I take a positive attitude toward myself. ")
    add += positive("On the whole, I am satisfied with myself. ")
    add += negative("I wish I could have more respect for myself. ")
    add += negative("I certainly feel useless at times. ")
    add += negative("At times I think I am no good at all. ")

    if add > 15:
        print(f"Your score is: {add} thus you have high self-esteem.")
    elif add <= 15:
        print(f"Your score is: {add} thus you have low self-esteem.")

def positive(question):

    print(question)
    reply = input("Enter D, d, a, or A: ")
    print()
    add = 0
    if reply == "D":
        add = 0
    elif reply == "d":
        add = 1
    elif reply == "a":
        add = 2
    else:
        add = 3
    
    return add


def negative(question):

    print(question)
    reply = input("Enter D, d, a, or A: ")
    print()
    add = 0
    if reply == "D":
        add = 3
    elif reply == "d":
        add = 2
    elif reply == "a":
        add = 1
    else:
        add = 0
    
    return add


if __name__ == "__main__":
    main()