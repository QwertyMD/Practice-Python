def square(n):  # Function to return the square of a number
    return n * n  # Return the square of n

def sum_squares(x):  # Function to return the sum of squares from 0 to x-1
    sum = 0  # Initialize sum to 0
    for n in range(x):  # Loop through numbers from 0 to x-1
        sum += square(n)  # Add the square of n to sum
    return sum  # Return the final sum

print(sum_squares(10))  # Print the sum of squares from 0 to 9