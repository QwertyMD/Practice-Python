## Name: Aaryan Dhakal
## Student ID: 2505814

## Title: AP Sequence Generator
## Description: This program generates a sequence: 0,4,8,,12,16,... containing the first 100 terms.

def sequence():
    """
    Generates a sequence of numbers from 0 to 100 that are divisible by 4.

    Returns:
        list: A list containing the numbers from 0 to 100 that are divisible by 4.
    """
    # Initialize an empty list to store the sequence
    seq = []
    # Iterate over the range of numbers from 0 to 99
    for i in range(100):
        # Append 4 times the number to the sequence list
        seq.append(4 * i)
    # Return the generated sequence
    return seq


# Only runs when executed directly, not when imported in another file.
if __name__ == "__main__":
    # Print the generated sequence
    print(sequence())
