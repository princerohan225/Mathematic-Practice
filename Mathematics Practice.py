import random


def Addition():
    while True:

        min = 1
        max = 100

        A = random.randint(min, max)
        # print("A:",A)
        B = random.randint(min, max)
        # print("B:",B)

        Sum = A+B
        print("\n", A, "+", B, "= ?")

        try:

            i = int(input("Enter the number:"))

            if i == Sum:
                print("\nCorrect Answer. {}".format(Sum))

            else:
                print("\nWrong Answer. The Answer is {}".format(Sum))

        except ValueError:
            print("\nAccept only Integer Number. Enter Again...")


def Subtraction():
    while True:
        min = 1
        max = 100

        A = random.randint(min, max)
        #print("\nA:", A)
        B = random.randint(min, max)
        #print("B:", B)
        print("\n", A, '-', B, '= ?')

        try:
            if A > B:
                Sum = A-B
                # print(Sum)

                i = int(input("Enter the number:"))

                if i == Sum:
                    print("\nCorrect Answer. {}".format(Sum))

                else:
                    print("\nWrong Answer. The Answer is {}".format(Sum))

            elif B > A:

                Sum = B-A
                # print(Sum)

                i = int(input("Enter the value:"))

                if i == Sum:
                    print("\nCorrect Answer. {}".format(Sum))

                else:
                    print("\nWrong Answer. The Answer is {}".format(Sum))

        except ValueError:
            print("\nAccept only Integer Number. Enter Again...")


def Multiplication():
    while True:

        min = 1
        max = 50

        A = random.randint(min, max)
        #print("\nA:", A)
        B = random.randint(min, max)
        #print("B:", B)

        Sum = A*B
        print("\n", A, "*", B, "= ?")
        try:
            I = int(input("\nEnter the Number:"))

            if I == Sum:
                print("\nCorrect Answer. {}".format(Sum))

            else:
                print("\nWrong Answer. The Answer is {}".format(Sum))

        except ValueError:
            print("\nAccept only Integer Number. Enter Again...")


def Division():
    while True:

        min = 1
        max = 50

        A = random.randint(min, max)
        # print("\nA:",A)
        B = random.randint(min, max)
        # print("B:",B)

        Divisor = A/B
        Remainder = round(Divisor, 2)

        print("\n", A, "/", B, "= ?")

        # print("Remainder:",Remainder)
        try:

            I = float(input("Enter the value: "))

            if I == Remainder:
                print("Correct Answer. {}".format(Remainder))

            else:
                print("Wrong Answer. The Answer is {}".format(Remainder))

        except ValueError:
            print("\nAccept only floating Number. Enter Again...")


def Percentage():
    while True:
        min = 1
        max = 50
        #per = 100

        A = random.randint(min, max)
        #print("\nA:", A)

        B = random.randint(min, max)
        #print("B:", B)

        quotient = A/B
        per = quotient*100
        percentage = round(per, 2)

        print("\n",A,'/',B, "*100","= ?")

        #print('Answer {} %'.format(percentage))

        try:

            Y = float(input("Enter the value:"))

            if Y == percentage:
                print("Correct Answer. {} %".format(percentage))

            else:
                print("Wrong Answer. The Answer is {} %".format(percentage))

        except ValueError:
            print("\nAccept only Floating Number. Enter Again...")


#print("Enter your Choice:\n")
print("Enter 0 for Quit.\n")
print("Enter 1 for Addition.\n")
print("Enter 2 for Substraction.\n")
print("Enter 3 for Multiplication.\n")
print("Enter 4 for Division.\n")
print("Enter 5 for Percentage.\n")

choice = int(input("Enter your Choice:"))

if choice == 1:
    Addition()
elif choice == 2:
    Subtraction()
elif choice == 3:
    Multiplication()
elif choice == 4:
    Division()
elif choice == 5:
    Percentage()
elif choice == 0:
    exit
