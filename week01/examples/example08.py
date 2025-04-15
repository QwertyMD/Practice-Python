def number_group(number):  # Function to determine if a number is positive, zero, or negative
    if number > 0:  # If the number is greater than 0
        return "Positive"  # Return "Positive"
    elif number == 0:  # If the number is 0
        return "Zero"  # Return "Zero"
    else:  # If the number is less than 0
        return "Negative"  # Return "Negative"

print(number_group(10))  # Check if 10 is positive, zero, or negative and print the result
print(number_group(0))  # Check if 0 is positive, zero, or negative and print the result
print(number_group(-5))  # Check if -5 is positive, zero, or negative and print the result