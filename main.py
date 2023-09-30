class Robot:
    def __init__(self, name, energy_consumption):
        """
        Initialize a Robot with a name and energy consumption.

        Args:
            name (str): The name of the robot.
            energy_consumption (str): The energy consumption as a string.

        """
        self.name = name
        self.energy_consumption = energy_consumption

    def display_info(self):
        """Display information about the robot."""
        print(f"Robot Name: {self.name}")
        print(f"Energy Consumption: {self.energy_consumption}")

class Part:
    def __init__(self, name, attack_level, defense_level, energy_consumption):
        """
        Initialize a Part with name, attack level, defense level, and energy consumption.

        Args:
            name (str): The name of the part.
            attack_level (int): The attack level.
            defense_level (int): The defense level.
            energy_consumption (str): The energy consumption as a string.

        """
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def display_info(self):
        """Display information about the part."""
        print(f"Part Name: {self.name}")
        print(f"Attack Level: {self.attack_level}")
        print(f"Defense Level: {self.defense_level}")
        print(f"Energy Consumption: {self.energy_consumption}")

if __name__ == "__main__":
    cam = Robot("Cam", "0.5%")
    print("Robot Cam:")
    cam.display_info()

    julyx = Robot("Julyx", "2%")
    print("Robot Julyx:")
    julyx.display_info()

    cam_part = Part("Cam Part", 90, 100, "Yes")
    print("Part Cam:")
    cam_part.display_info()

    julyx_part = Part("Julyx Part", 95, 90, "Yes")
    print("Part Julyx:")
    julyx_part.display_info()

