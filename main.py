import random
import time

class Robot:
    def __init__(self, name, energy_consumption):
        self.name = name
        self.energy_consumption = energy_consumption
        self.energy = 100  # Initialize energy to 100%
        self.inventory = []  # Robot's inventory for holding parts
        self.xp = 0
        self.level = 1
        self.overclocked = False  # Flag to indicate if the robot is overclocked
        self.overclock_duration = 10  # Duration of overclock in seconds

        # New attributes for the shield
        self.shield = 0
        self.max_shield = 50  # Maximum shield capacity

    def display_info(self):
        print(f"Robot Name: {self.name}")
        print(f"Energy Consumption: {self.energy_consumption}")
        print(f"Energy: {self.energy}%")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}")
        if self.overclocked:
            print("Overclocked: Yes")
        print(f"Shield: {self.shield}%")

    def change_energy_consumption(self, new_energy_consumption):
        self.energy_consumption = new_energy_consumption

    def attack(self, part):
        if self.energy >= 10:
            attack_power = 20 if self.overclocked else 10  # Double attack power when overclocked
            if self.shield > 0:
                absorbed_damage = min(self.shield, attack_power)
                self.shield -= absorbed_damage
                attack_power -= absorbed_damage
                print(f"{self.name}'s shield absorbed {absorbed_damage} damage.")

            if attack_power > 0:
                print(f"{self.name} attacks {part.name} with energy consumption of {self.energy_consumption}.")
                self.energy -= 10
                part.reduce_defense(attack_power)
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

    def repair_part(self, part_name):
        for part in self.inventory:
            if part.name == part_name:
                if self.energy >= 20:  # Require 20 energy to perform a repair
                    self.energy -= 20
                    part.restore_defense()  # Call the method to restore defense
                    print(f"{self.name} repairs {part_name}, restoring some defense.")
                else:
                    print(f"{self.name} does not have enough energy to repair {part_name}.")
                return
        print(f"{self.name} does not have {part_name} in their inventory for repair.")

    def overclock(self):
        if not self.overclocked and self.energy >= 30:  # Require 30 energy to overclock
            self.energy -= 30
            self.overclocked = True
            print(f"{self.name} overclocks and gains double attack power for {self.overclock_duration} seconds.")
            start_time = time.time()
            while time.time() - start_time < self.overclock_duration:
                pass
            self.overclocked = False
            print(f"{self.name} returns to normal operation after overclocking.")
        elif self.overclocked:
            print(f"{self.name} is already overclocked.")
        else:
            print(f"{self.name} does not have enough energy to overclock.")

    # New method to recharge the shield
    def recharge_shield(self, amount):
        self.shield = min(self.max_shield, self.shield + amount)
        print(f"{self.name} recharges the shield. Shield is now {self.shield}%.")

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

    def reduce_defense(self, attack_power):
        print(f"{self.name}'s defense level reduced by {attack_power}.")
        self.defense_level -= attack_power

    def restore_defense(self):
        print(f"{self.name}'s defense is partially restored by 10.")
        self.defense_level += 10

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

    cam.repair_part("Cam Part")  # Perform a repair
    cam.display_info()
    cam_part.display_info()

    cam.overclock()  # Use the overclock feature
    cam.attack(cam_part)  # Try an attack while overclocked
    cam.display_info()
    cam_part.display_info()
