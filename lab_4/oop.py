from Office_module import Office
from Employee_modul import Employee
from Car_module import Car
from Person_module import Person

car = Car("Toyota", 100, 80)
person = Person("Ali", 500, "happy", 90)
employee = Employee("Ahmed", 1000, "tired", 80, id=1, car=car, email="ahmed@example.com", salary=1200, distance_to_work=20)
office = Office(name="TechCorp")

person.sleep(6)
print(f"Person Mood after sleeping: {person.mood}")

person.eat(2)
print(f"Person Health Rate after eating: {person.healthRate}")

person.buy(3)
print(f"Person Money after buying items: {person.money}")

employee.work(9)
print(f"Employee Mood after working: {employee.mood}")

employee.drive(15)
employee.refuel(20)
print(f"Car Fuel Rate after refueling: {car.fuel_rate}")

office.hire(employee)
print(f"Number of employees after hiring: {Office.employees_num}")
