class Office:
    employees_num = 0
    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num

    def get_all_employees(self):
        return self.employees

    def get_employee(self, id):
        for emp in self.employees:
            if emp.id == id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, id):
        employee = self.get_employee(id)
        if employee:
            self.employees.remove(employee)
            Office.employees_num -= 1

    def deduct(self, emp_id, deduction):
        employee = self.get_employee(id)
        if employee:
            employee.salary -= deduction

    def reward(self, id, reward):
        employee = self.get_employee(id)
        if employee:
            employee.salary += reward

    def check_lateness(self, id, moveHour, targetHour):
        employee = self.get_employee(id)
        if employee:
            is_late = self.calculate_lateness(targetHour, moveHour, employee.distance_to_work, employee.car.velocity)
            if is_late:
                self.deduct(id, 10)
            else:
                self.reward(id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        travel_time = distance / velocity
        arrival_hour = moveHour + travel_time
        return arrival_hour > targetHour