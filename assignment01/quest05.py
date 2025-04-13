## Name: Aaryan Dhakal
## Student ID: 2505814

## Title: Fibonacci Sequence Generator
## Description: This program generates a Fibonacci sequence up to the 20th term.

def fibonacci(n):
    """
    Generates a Fibonacci sequence up to the nth number.

    Parameters:
        n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
        list: A list containing the Fibonacci sequence up to the 20th term.
    """
    # Check if the input number is less than 1
    if n < 1:
        # Return None if the input number is less than 1
        return None
    # Check if the input number is less than 2
    elif n < 2:
        # Return a list containing only the first Fibonacci number if n is less than 2
        return [0]
    # Check if the input number is less than 3
    elif n < 3:
        # Return a list containing the first two Fibonacci numbers if n is less than 3
        return [0, 1]
    else:
        # Initialize the sequence with the first two Fibonacci numbers
        seq = [0, 1]
        # Initialize the first Fibonacci number
        a = 0
        # Initialize the second Fibonacci number
        b = 1
        # Iterate to generate the remaining Fibonacci numbers
        for i in range(n - 2):
            # Calculate the next Fibonacci number
            c = a + b
            # Append the next Fibonacci number to the sequence
            seq.append(c)
            # Update the first Fibonacci number
            a = b
            # Update the second Fibonacci number
            b = c
    # Return the generated Fibonacci sequence
    return seq


# Only runs when executed directly, not when imported in another file.
if __name__ == "__main__":
    # Print the Fibonacci sequence up to the 20th number
    print(fibonacci(20))
