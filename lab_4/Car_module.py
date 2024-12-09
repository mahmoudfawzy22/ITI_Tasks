class Car:

    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            raise ValueError("Fuel rate must be between 0 and 100.")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self.velocity = value
        else:
            raise ValueError("Velocity must be between 0 and 200.")

    def run(self, velocity, distance):
        self.velocity = velocity
        while distance > 0 and self.fuel_rate > 0:
            distance -= velocity
            self.fuel_rate -= 1
        self.stop(distance)

    def stop(self, remaining_distance=0):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Stopped with {remaining_distance} km remaining.")
        else:
            print("Arrived at the destination.")