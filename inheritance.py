# Base Class
class Animal:
  def __init__(self, name):
    self.name = name

  def sound(self):
    print( f"{self.name} makes a sound")
  

# dog = Animal("Dog")
# dog.sound()


# Derived Class
class Dog(Animal):
  def sound(self):
    print(f"{self.name} barks")

dog = Dog("Oscar")
dog.sound()