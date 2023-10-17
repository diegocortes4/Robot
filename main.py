import random

class Robot:
    def __init__(self, name, energy_consumption):
        self.name = name
        self.energy_consumption = energy_consumption
        self.energy = 100  # Initialize energy to 100%
        self.inventory = []  # Robot's inventory for holding parts
        self.xp = 0
        self.level = 1

    def display_info(self):
        print(f"Robot Name: {self.name}")
        print(f"Energy Consumption: {self.energy_consumption}")
        print(f"Energy: {self.energy}%")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}")

    def change_energy_consumption(self, new_energy_consumption):
        self.energy_consumption = new_energy_consumption

    def attack(self, part):
        if self.energy >= 10:
            print(f"{self.name} attacks {part.name} with energy consumption of {self.energy_consumption}.")
            self.energy -= 10
            part.reduce_defense()
            self.gain_xp(10)  # Gain XP for successful attack
        else:
            print(f"{self.name} does not have enough energy to attack.")

    def add_to_inventory(self, part):
        self.inventory.append(part)
        print(f"{part.name} has been added to {self.name}'s inventory.")

    def remove_from_inventory(self, part_name):
        for part in self.inventory:
            if part.name == part_name:
                self.inventory.remove(part)
                print(f"{part_name} has been removed from {self.name}'s inventory.")
                break
        else:
            print(f"{self.name} does not have {part_name} in their inventory.")

    def recharge_energy(self, amount):
        self.energy = min(100, self.energy + amount)
        print(f"{self.name} recharges energy. Energy is now {self.energy}%.")

    def display_inventory(self):
        print(f"{self.name}'s Inventory:")
        for part in self.inventory:
            print(part.name)

    def gain_xp(self, xp_amount):
        self.xp += xp_amount
        if self.xp >= 100:
            self.xp -= 100
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")

    def random_event(self):
        event = random.choice(["Energy Drain", "Lucky Find"])
        if event == "Energy Drain":
            energy_loss = random.randint(10, 30)
            self.energy -= energy_loss
            print(f"{self.name} experienced an energy drain event and lost {energy_loss}% energy.")
        elif event == "Lucky Find":
            found_part = Part("Mystery Part", random.randint(50, 100), random.randint(50, 100), "Low")
            self.add_to_inventory(found_part)
            print(f"{self.name} found a mysterious part in a lucky event and added it to the inventory.")

    def use_special_ability(self, part):
        # Add special abilities here
        pass

    def part_upgrade(self, part_name):
        for part in self.inventory:
            if part.name == part_name and self.xp >= 50:
                self.xp -= 50
                part.attack_level += 10
                part.defense_level += 10
                print(f"{self.name} spent 50 XP to upgrade {part_name}.")
                return
        print(f"{self.name} cannot upgrade {part_name} or does not have enough XP.")

    def is_game_over(self):
        return self.energy <= 0

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

# The main part of the code remains unchanged.

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
    cam.add_to_inventory(Part("Laser Gun", 80, 0, "High"))

    cam.display_inventory()
    print()

    while not cam.is_game_over():
        cam.random_event()
        cam.attack(cam_part)
        cam.display_info()
        cam_part.display_info()
        print()

    print(f"{cam.name} has run out of energy. Game over!")
