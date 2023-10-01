class Robot:
    def __init__(self, name, energy_consumption):
        self.name = name
        self.energy_consumption = energy_consumption
        self.energy = 100  # Initialize energy to 100%
        self.inventory = []  # Robot's inventory for holding parts

    def display_info(self):
        print(f"Robot Name: {self.name}")
        print(f"Energy Consumption: {self.energy_consumption}")
        print(f"Energy: {self.energy}%")

    def change_energy_consumption(self, new_energy_consumption):
        self.energy_consumption = new_energy_consumption

    def attack(self, part):
        if self.energy >= 10:  # Require at least 10% energy to perform an attack
            print(f"{self.name} attacks {part.name} with energy consumption of {self.energy_consumption}.")
            self.energy -= 10
            part.reduce_defense()
        else:
            print(f"{self.name} does not have enough energy to attack.")

    def add_to_inventory(self, part):
        self.inventory.append(part)
        print(f"{part.name} has been added to {self.name}'s inventory.")

class Part:
    def __init__(self, name, attack_level, defense_level, energy_consumption):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def display_info(self):
        print(f"Part Name: {self.name}")
        print(f"Attack Level: {self.attack_level}")
        print(f"Defense Level: {self.defense_level}")
        print(f"Energy Consumption: {self.energy_consumption}")

    def reduce_defense(self):
        print(f"{self.name}'s defense level reduced by 10.")
        self.defense_level -= 10

if __name__ == "__main__":
    cam = Robot("Cam", "0.5%")
    cam_part = Part("Cam Part", 90, 100, "Yes")

    print("Robot Cam:")
    cam.display_info()
    print()

    print("Part Cam:")
    cam_part.display_info()
    print()

    cam.add_to_inventory(cam_part)

    print("Robot Cam's Inventory:")
    for item in cam.inventory:
        item.display_info()

    print()
    cam.attack(cam_part)
    cam.display_info()
    cam_part.display_info()

