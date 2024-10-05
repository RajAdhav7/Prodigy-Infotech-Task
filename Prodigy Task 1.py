def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit.lower() == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        return None, None

def main():
    print("Temperature Conversion Program")
    
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
        
        fahrenheit, kelvin = convert_temperature(value, unit)
        
        if fahrenheit is not None and kelvin is not None:
            print(f"Converted Values:")
            if unit.lower() == 'celsius':
                print(f"{value} °C = {fahrenheit:.2f} °F")
                print(f"{value} °C = {kelvin:.2f} K")
            elif unit.lower() == 'fahrenheit':
                print(f"{value} °F = {fahrenheit:.2f} °C")
                print(f"{value} °F = {kelvin:.2f} K")
            elif unit.lower() == 'kelvin':
                print(f"{value} K = {fahrenheit:.2f} °F")
                print(f"{value} K = {kelvin:.2f} °C")
        else:
            print("Invalid unit entered. Please use 'Celsius', 'Fahrenheit', or 'Kelvin'.")
    
    except ValueError:
        print("Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()
