def number_check(Q):
    error = "Sorry, please enter an number"
    number = ""
    while not number:
        try:
            number = int(input(Q))
            return number
        except ValueError:
            print(error)


name = input("What is the driver's name?\n")
minute = 0
while minute != 0:
if minute <= 0:
    minute = float(input("How many minutes to enter a new trip"))
    print(f"This trip cost ${10 + 2 * minute}")
    elif 0 <= minute:
    print("")




