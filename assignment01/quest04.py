## Name: Aaryan Dhakal
## Student ID: 2505814

## Title: Missing Numbers Finder
## Description: This program finds the missing numbers in a given list from 1 to 10.

def missing_nums(lst):
    """
    Finds the missing numbers in a given list from 1 to 10.

    Parameters:
        lst (list): The list of numbers to check.

    Returns:
        list: A list containing the missing numbers from 1 to 10.
    """
    # Initialize an empty list to store the missing numbers
    seq = []
    # Iterate over the range of numbers from 1 to 10
    for i in range(1, 11):
        # Check if the current number is not in the given list
        if i not in lst:
            # If true, append the number to the missing numbers list
            seq.append(i)
    # Return the list of missing numbers
    return seq


# Only runs when executed directly, not when imported in another file.
if __name__ == "__main__":
    # Print the missing numbers from the given list
    print(missing_nums([1, 2, 3, 4, 6, 7, 10]))
