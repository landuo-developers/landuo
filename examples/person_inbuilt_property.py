# from landuo import property # add this one line for cached property
import time


class Person:

    def __init__(self, name, height, weight):
        self._name = name
        self._height = height
        self._weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError(
                "A Person's name cannot be less than 2 characters!")
        self._name = value

    def _introduction(self):
        return f"Hi, my name is {self.name}!"

    # different way to initialize a property
    introduction = property(_introduction)

    @property
    def weight(self):
        print(f"Getting {self.name}'s weight...")
        print(f"Doing complex calculations weight...")
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Invalid Weight!")
        self._weight = value
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def BMI(self):
        self._BMI = self.weight / (self.height)**2
        print(f"Doing complex calculations BMI...")
        time.sleep(1.5)
        return self._BMI

    @BMI.setter
    def BMI(self, value):
        print(f"Doing complex calculations for BMI...")
        time.sleep(1.5)
        self.weight = value * (self.height)**2
        self._BMI = value


class Employee(Person):

    def __init__(self, name, height, weight, occupation):
        super().__init__(name, height, weight)
        self._occupation = occupation

    @property
    def introduction(self):  # subclass modifies the superclass' managed attribute
        # call the superclass' managed attribute and edit/extend it.
        return super().introduction + \
            f' I am a happy person and my occupation is {self.occupation}!'

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        if not isinstance(value, str):
            raise Exception(f"{value} is not of string type.")
        self._occupation = value
