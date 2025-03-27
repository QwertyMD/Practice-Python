## Name: Aaryan Dhakal
## Student ID: 2505814

## Title: Pascal's Triangle Generator
## Description: This program prints the first 10 rows of Pascal's Triangle.

def pascal_triangle(n):
    """
    Print the first n rows of Pascal's Triangle.

    Parameters:
        n (int): The number of rows to print.
    """
    for i in range(n):
        # Initialize the first number in the row
        num = 1
        # Iterate through each position in the current row
        for j in range(i + 1):
            # Print the current number
            print(num, end=" ")
            # Calculate the next number in the row
            num = num * (i - j) // (j + 1)
        # Move to the next line after printing the row
        print()


# Only runs when executed directly, not when imported in another file.
if __name__ == "__main__":
    # Print the first 10 rows of Pascal's Triangle
    pascal_triangle(10)
