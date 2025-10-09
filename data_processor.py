"""
data_processor.py

A small module to process numerical data.

Author: Rose Maina
Date: 07/10/2025
"""

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
    
    total = sum(numbers)  # Sum all the numbers
    count = len(numbers)  # Count how many numbers are in the list
    
    average = total / count  # Compute the average
    return average


if __name__ == "__main__":
    # Example usage of the module
    sample_data = [10, 20, 30, 40, 50]
    avg = calculate_average(sample_data)
    print(f"The average of {sample_data} is {avg}")
