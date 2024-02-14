def dropOff():
    child_name = input("Enter the name of the child: ")
    print(f"{child_name} has been added in.")


def pickUp():
    child_name = input("Enter the name of the child: ")
    print(f"{child_name} has been added in.")


def calcCost():
    hour = float(input("How many hours will this child stay: "))
    rate_per_hour = 12
    total_cost = hour * rate_per_hour
    print(f"The total cost for {hour} hours is ${total_cost:.2f}.")


def printRoll():
    child_name = input("Enter the name of the child: ")
    print(f"Printing {child_name}...")


choice = 0

while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()

    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()
    elif choice == 2:
        pickUp()
    elif choice == 3:
        calcCost()
    elif choice == 4:
        printRoll()
        print("Goodbye")
    else:
        print("Please write the numbers within 1 to 5")
