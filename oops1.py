# Initiating a class

class Employee:
  # Special Metohd/ Dunder Method - Constructor
  def __init__(self):
    self.id = 176
    self.salary = 30000
    self.designation = "ML Engineer"
  
  def travel(self, destination):
    print(f"Employee is travelling to {destination}")


# Creating an object
sam = Employee()
# print(sam.designation)
sam.travel("London")
