class Speeder:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        if self.speed <= 10:
            return 30
        elif self.speed <= 14:
            return 80
        elif self.speed <= 19:
            return 120
        elif self.speed <= 24:
            return 170
        elif self.speed <= 29:
            return 230
        elif self.speed <= 34:
            return 300
        elif self.speed <= 39:
            return 400
        elif self.speed <= 44:
            return 510
        else:
            return 630

    def str_(self):
        return f"Name: {self.name}, Speed: {self.speed}"


wanted_list = ["James Wilson", "Helga Norman", "Zachary Conroy"]
speeders = []
total_fines = 0

while True:
    name = input("Enter the driver's name: ")
    if name in wanted_list:
        print(f"{name} - WARRANT FOR ARREST!")
        continue
    elif name == "stop":
        break
    speed = int(input("Enter the driver's speed: "))
    speeder = Speeder(name, speed)
    speeders.append(speeder)
    total_fines += speeder.fine
    print(f"{speeder.name} will be ${speeder.fine}")

print("\nSummary of the day:")
print(f"Total violations: {len(speeders)}")
for idx, speeder in enumerate(speeders, start=1):
    print(f"{idx}. {speeder}")
print(f"Total fines collected: ${total_fines}")