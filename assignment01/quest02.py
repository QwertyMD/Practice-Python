## Name: Aaryan Dhakal
## Student ID: 2505814

## Title: GP Sequence Generator
## Description: This program generates a sequence of powers of 2 from 2^1 to 2^20.

def method_one():
    """
    Generates a sequence of powers of 2 from 2^1 to 2^20.

    Returns:
        list: A list containing the powers of 2 from 2^1 to 2^20.
    """
    # Initialize an empty list to store the sequence
    seq = []
    # Iterate over the range of numbers from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Append the power of 2 to the sequence list
        seq.append(2 ** i)
    # Return the generated sequence
    return seq


def method_two(n=1, seq=None):
    """
    Generates a sequence of powers of 2 from 2^1 to 2^20 using recursion.

    Parameters:
        n (int): The current exponent (default is 1).
        seq (list): The list to store the sequence (default is None).

    Returns:
        list: A list containing the powers of 2 from 2^1 to 2^20.
    """
    if seq is None:
        # Initialize the sequence list if it is not provided
        seq = []
    if n > 20:
        # Base case: if the current exponent is greater than 20, return the sequence
        return seq
    # Append the current power of 2 to the sequence list
    seq.append(2 ** n)
    # Recursive call to generate the next power of 2
    return method_two(n + 1, seq)


# Only runs when executed directly, not when imported in another file.
if __name__ == "__main__":
    # Print the generated sequence
    print(method_one())
    print(method_two())
