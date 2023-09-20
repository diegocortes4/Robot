class Robot: 
   def __init__(self, name, color_code):
     self.name = name
     self.color_code = color_code
     self.energy = 100
     self.on = True
     
     print("Hello World")
     
   def great(self):
     print("My name is: ", self.name)
     print("My color is: ", self.color_code)
     print("My energy is: ", self.energy)
     print("My status is: ", self.on)


friday = Robot("Friday", "25")
friday.great()

jarvis = Robot("Jarvis", "65")
jarvis.great()
