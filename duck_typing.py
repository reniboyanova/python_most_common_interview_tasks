class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
duck = Duck()

make_animal_speak(dog)  # Outputs: Woof!
make_animal_speak(cat)  # Outputs: Meow!
make_animal_speak(duck)  # Outputs: Quack!
