def print_cars():
    print("VEHICLE NUMBER - TYPE - NO. SEATS")
    for number, car in booked_cars.items(): 
        if car not in booked_cars:
            print(f"No. {number} - {car['type']} - {car['seats']} seats")


def book_car(car_number, customer_name, booked_cars):
    if car_number in car:
        booked_cars.append(car[car_number])
        print(f"{car[car_number]['type']} booked by {customer_name}")
    else:
        print("Invalid vehicle number.")


car_number = 0

while car_number != 9:
    print("-----------------------------------------------------------------------")
    print("VEHICLE NUMBER - TYPE - NO. SEATS")
    print("-----------------------------------------------------------------------")
    print("No. 1 - Suzuki Van - 2 seats - NOTE: Not have enough seats")
    print("No. 2 - Toyota Corolla - 4 seats")
    print("No. 3 - Honda CRV - 4 seats")
    print("No. 4 - Suzuki Swift - 4 seats")
    print("No. 5 - Mitsubishi Airtrek - 4 seats")
    print("No. 6 - Nissan DC Ute - 4 seats")
    print("No. 7 - Toyota Previa - 7 seats")
    print("No. 8 - Toyota Hi Ace - 12 seats")
    print("No. 9 - Toyota Hi Ace - 12 seats")
    print()

car_number = int(input("Enter a number to book: "))
customer_name = input("Enter your name: ")
print(f"{customer_name} booked by")


while True:
    print("Please enter the number of seats required (Type -1 to quit):")
    seats_required = int(input())

    if seats_required == -1:
    print(cars)
    print("Enter a number to book:")
    car_number = int(input())
    print("Enter your name:")
    customer_name = input()
    book_car(car_number, customer_name)
    print("VEHICLES BOOKED TODAY")
    for car in booked_cars:
        for number, car_details in cars.items():
            if car_details == car:
                print(f"No. {number} - {car_details['type']} - Booked by: {customer_name}")
