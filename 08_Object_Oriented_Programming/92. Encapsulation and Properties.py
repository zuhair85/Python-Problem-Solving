# 1. Problem statement
# Create a Temperature class that stores a temperature value in Celsius.
#
# Your class should protect its internal data by using encapsulation and Python properties.
#
# The temperature must always satisfy the validation rules defined below, regardless of whether the value is assigned during object creation or changed afterward.
# 2. Requirements
# Your class must:
# - Store a temperature in Celsius.
# - Allow users to retrieve the temperature.
# - Allow users to change the temperature.
# - Reject invalid temperature values.
# - Provide a Fahrenheit representation of the stored Celsius temperature.
# - Ensure validation happens whenever the temperature is modified.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius      #Calls the celsius setter

    #getter
    @property
    def celsius(self):
        return self._celsius

    #setter
    @celsius.setter
    def celsius(self, new_celsius):
        if (isinstance(new_celsius, (int, float))
                and not isinstance(new_celsius, bool)
                and new_celsius >= -273.15):
            self._celsius = new_celsius
        else:
            raise ValueError("Invalid temperature value!")


    @property
    def fahrenheit(self):
        return (self._celsius * (9/5)) + 32




temp = Temperature(25)

print(temp.celsius)
print(temp.fahrenheit)

temp.celsius = 30

print(temp.celsius)
print(temp.fahrenheit)