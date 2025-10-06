# A simple calculator that performs the four basic operations

class Calculator:
    """
    A class that performs four arithmetic 
    """
    # initializing the class Constructor
    def __init__(self, num1, num2, operator):
        # Initializing the class attributes
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    # Method for adding numbers    
    def add(self):
        return self.num1 + self.num2
    
    # Method for subtracting numbers    
    def subtract(self):
        return self.num1 - self.num2
    
    # Method for multiplying numbers    
    def multiply(self):
        return self.num1 * self.num2
    
    # Method for dividing numbers    
    def divide(self):
        if self.num2 == 0:
            # Making sure to avoid unnecessary errors.
            raise ZeroDivisionError('Cannot divide by zero.')
        return self.num1 / self.num2
        

# Main function for testing the calculator operations
def main():
    num1 = int(input("Num 1: "))
    operator = input("Operator: ")
    num2 = int(input("Num 2: "))
    
    # Instantiating the calculator class
    calc = Calculator(num1, num2, operator)
    # Add
    print(calc.add()) 
    # Subtract
    print(calc.subtract()) 
    # Multiply
    print(calc.multiply())
    # Divide
    print(calc.divide())
    
# Entry point 
if __name__ == "__main__":
    main()
         
        
    