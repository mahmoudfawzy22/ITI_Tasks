from Person_module import Person
from Car_module import Car

class Employee(Person):

    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            raise ValueError("Salary must be 1000 or more.")

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def send_mail(self, to, subject, msg, receiver_name):
        with open("emails.txt", "a") as email_file:
            email_file.write(f"To: {to}\nSubject: {subject}\nMessage: {msg}\nFrom: {receiver_name}\n\n")

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gas_amount=100):
        if self.car.fuel_rate + gas_amount > 100:
            self.car.fuel_rate = 100
        else:
            self.car.fuel_rate += gas_amount