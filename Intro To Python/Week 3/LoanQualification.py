print("Please use a 1 - 10 rating for the following: ")
print()

large = int(input("How large is the loan size? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment = int(input("How large is your down payment? "))

if large >= 5:
    boo = True
    if credit >= 7 and income >=7:
        boo = True
        print("Decision: Yes")
    elif credit >=7 and income >= 5:
        boo = True
        print("Decision: Yes")
    else:
        boo = False
        print("Decision: No")
else:
    if credit < 4:
        boo = False
        print("Decision: No")
    elif credit >= 5:
        boo = True
        if income >= 7 and payment <= 7:
            boo = True
            print("Decision: Yes")
        elif income >= 4 and payment >= 4:
            boo = True
            print("Decision: Yes")
        else:
            boo = False
            print("Decision: No")     
    else:
        boo = False
        print("Decision: No")