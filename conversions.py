def convertCelsiusToKelvin(celsius):
    """
    Converts Celsius to Kelvin
    """
    return (celsius + 273.15)

def covertCelsiusToFahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit
    """
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def convertKelvinToCelsius(kelvin):
    """
    Converts celsius to Kelvin
    """
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    """
    Converts Celsius to Fahrenheit
    """
    fahrenheit = kelvin * 1.8 - 459.67
    return fahrenheit


def convertFahrenheitToKelvin(fahrenheit):
    """
    Converts celsius to kelvin
    """
    kelvin = (fahrenheit + 459.67) * (5/9)
    return kelvin


def convertFahrenheitToCelsius(fahrenheit):
    """
    Converts Celsius to Fahrenheit
    """
    celsius = (fahrenheit - 32) * (5/9)
    return celsius
