# Single Inheritance (Единично наследяване):
# В случай на единично наследяване, един клас наследява от друг един клас.
# Този вид наследяване е най-простият и ефективен начин за повторно използване на код.
# В следния пример ще използваме два класа, Person и Employee, като Employee наследява от Person:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")

# Създаваме инстанция на класа Employee
employee = Employee("Alice", 30, "E1234")
employee.display_info()  # Метод от родителския клас
employee.display_employee_info()  # Метод от наследения клас


# Multiple Inheritance (Множествено наследяване):
# В случай на множествено наследяване, един клас наследява от повече от един клас.
# В следния пример имаме три класа, Person, Address, и Contact,
# като Contact наследява както от Person, така и от Address:

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def display_address_info(self):
        print(f"Address: {self.street}, {self.city}")

class Contact(Person2, Address):
    def __init__(self, name, age, street, city, phone):
        Person2.__init__(self, name, age)
        Address.__init__(self, street, city)
        self.phone = phone

    def display_contact_info(self):
        self.display_person_info()
        self.display_address_info()
        print(f"Phone: {self.phone}")

# Създаваме инстанция на класа Contact
contact = Contact("Alice", 30, "123 Main St", "City", "555-1234")
contact.display_contact_info()


# Multilevel Inheritance (Многостепенно наследяване):
# В случай на многостепенно наследяване, един клас наследява от друг, който в свой ред наследява от трети клас.
# В следния пример имаме три класа, Vehicle, Car, и ElectricCar,
# като Car наследява от Vehicle, а ElectricCar наследява от Car:

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def display_car_info(self):
        self.display_info()
        print(f"Fuel Type: {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model, "Electric")
        self.battery_capacity = battery_capacity

    def display_electric_car_info(self):
        self.display_car_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Създаваме инстанция на класа ElectricCar
electric_car = ElectricCar("Tesla", "Model S", 100)
electric_car.display_electric_car_info()

