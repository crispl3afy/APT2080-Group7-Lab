# The fuunction to convert Celsius to Fahrenheit and vice versa
def celsius_to_fahrenheit(celsius):

# Formula: (°C × 9/5) + 32 = °F
    return (celsius * 9/5) + 32

# The function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
# Formula: (°F − 32) × 5/9 = °C
    return (fahrenheit - 32) * 5/9

# Function that handles user interaction and conversion choices
def temperature_conversion():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

# User input for the conversion choice
    choice = input("Choose conversion (1 or 2): ")

# Perform conversion based on user choice    
    if choice == "1":
        # The User inputs for the Celsius temperature
        c = float(input("Enter temperature in Celsius: "))
        # Calls the conversion function and displays the result
        f = celsius_to_fahrenheit(c)

        #Results displayed to the user inform of 2 decimal places
        print(f"{c}°C = {f:.2f}°F")

        # The User inputsthe Fahrenheit temperature
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        #Converts to Celsius 
        c = fahrenheit_to_celsius(f)

        #Results displayed to the user inform of 2 decimal places
        print(f"{f}°F = {c:.2f}°C")

        # Handles invalid choice
    else:
        print("Invalid choice.")

# Main function to run the temperature conversion program
def main():
    # Call the temperature conversion function to start the program
    temperature_conversion()
    
#Enables the script to be run directly
if __name__ == "__main__":
    main()