# Last updated: 19/10/2026, 16:21:32
class Solution(object):
    def convertTemperature(self, celsius):
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        return [Kelvin, Fahrenheit]