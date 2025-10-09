def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list of float or int): List containing numerical values.

    Returns:
        float: The average of the numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty. Cannot compute average.")

    # Validate that all elements are numeric
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError(f"Invalid value detected: {n}. All elements must be numbers.")
    
    total = sum(numbers)   # Sum all the numbers
    count = len(numbers)   # Count numbers in the list
    average = total / count
    return average~~~


if __name__ == "__main__":
    print("=== Average Calculator ===")
    try:
        # Ask user to enter numbers separated by commas
        raw_input = input("Enter numbers separated by commas (e.g., 10, 20, 30): ")

        # Convert input string into list of floats
        numbers = [float(x.strip()) for x in raw_input.split(",")]

        avg = calculate_average(numbers)
        print(f"The average of {numbers} is {avg:.2f}")

    except ValueError as e:
        print(f"Error: {e}")  # User-friendly error message
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




