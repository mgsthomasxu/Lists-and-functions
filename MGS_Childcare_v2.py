roll = []


def dropOff():
    child_name = input("Enter the name of the child: ")
    roll.append(child_name)
    print(f"{child_name} has been added in.")


def pickUp():
    child_name_2 = input("Enter the name of the child: ")
    if child_name_2 in roll:
        roll.remove(child_name_2)
        print(f"{child_name_2} has been removed in.")
    else:
        str(input(f"These is no name called {child_name_2}. Please enter it again"))


def calcCost():
    rate = 12
    total_cost = hour * rate * 12
    return total_cost


def printRoll():
    child_name = input("Enter the name of the child: ")
    print(f"Printing {child_name}...")
    for item in roll:
        print(f"\t{item}")
    print()


choice = 0
def menu():
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
    menu()

    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()
    elif choice == 2:
        pickUp()
    elif choice == 3:
        calcCost()
        hour = float(input("How many days will this child stay: "))
        print(f"The total cost for {hour} hours is ${total_cost:.2f}.")
    elif choice == 4:
        printRoll()
    else:
        print("Goodbye")
