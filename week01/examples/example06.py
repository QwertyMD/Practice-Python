def order_numbers(number1, number2):  # Function to order two numbers
    if number2 > number1:  # If the second number is greater
        return number1, number2  # Return in ascending order
    else:  # If the first number is greater or equal
        return number2, number1  # Return in ascending order

smaller, bigger = order_numbers(100, 99)  # Order the numbers 100 and 99
print(smaller, bigger)  # Print the ordered numbers