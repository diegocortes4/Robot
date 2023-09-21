class Robot:
  def __init__(self, name, energy_consumption):
    self.name = name
    self.energy_consumption = energy_consumption

    print("Hello world")

  def great(self):
    print("my name is:", self.name)

  def sprint_energy(self):
    print("My energy consumption is:", self.energy_consumption)  


cam = Robot("cam", "0.5%")
cam.great()
cam.sprint_energy()

julyx = Robot("julyx", "2%")
julyx.great()
julyx.sprint_energy()


class Part:
    def __init__(self, name, attack_level, defense_level, energy_consumption):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
        print("My name is:", self.name)

    def get_status_dict(self):
        print("Nivel de ataque es:", self.attack_level)

    def reduce_defense(self):
        print("Nivel de defensa:", self.defense_level)

    def is_available(self):
        print("disponible:", self.energy_consumption)
        


cam = Part("cam", 90, 100, "Yes")

cam.get_status_dict()
cam.reduce_defense()
cam.is_available()

julyx = Part("julyx", 95, 90, "Yes")
julyx.get_status_dict()
julyx.reduce_defense()
julyx.is_available()

