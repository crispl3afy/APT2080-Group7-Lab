

"""
This is a four arithmetic operation calculator
    - Addition
    - Subtration
    - Multiply
    - Divide
    
By: Thomas wotoro Joseph
ID: 674609
"""

class Calculator:
    """
    A class that performs four arithmetic 
    
    Methods:
        add()
        subtract()
        multiply()
        divide()
    """
 
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
    """
    This main function handles the operation of the calculator
    """
    
    print("Welcome to 4-operation Calc.\n")
    while True:
        try:
            num1 = int(input("Num 1: "))
            operator = input("Operator: ")
            num2 = int(input("Num 2: "))
        except ValueError:
            return "Please enter an integer"
        except Exception as e:
            return f"Error occured: {e}"
        
        # Instantiating the calculator class
        calc = Calculator(num1, num2, operator)
        # Add
        if operator == '+':
            print(calc.add()) 
        # Subtract
        elif operator == '-':
            print(calc.subtract()) 
        # Multiply
        elif operator == '*':
            print(calc.multiply())
        # Divide
        elif operator == '-':
            print(calc.divide())
        else:
            return "Invalid operation"
        
        # asking user whether to continue or not
        continue_choice = input("Do you want to continue? (yes/no) ").lower()
        if continue_choice != 'yes':
            print("Thanks for using my program. BYE!!!")
            break
    
# Entry point 
if __name__ == "__main__":
    main()
         
        
    
