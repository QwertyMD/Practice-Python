## Name: Aaryan Dhakal
## Student ID: 2505814

## Title: Graph Plotting
## Description: This script generates and plots two mathematical functions on the same graph.

# Import the matplotlib.pyplot module for plotting graph
import matplotlib.pyplot as plt

# Initialize an empty list to store x values
x = []
# Loop through the range from -5 to 15
for i in range(-5, 16):
    # Append each value to the x list
    x.append(i)


def graph01():
    """
    Generate y values for the function 3x^2.

    Returns:
        list: A list of y values corresponding to the x values.
    """
    # Initialize an empty list to store y values
    y = []
    # Loop through each value in the x list
    for j in x:
        # Calculate the function value for 3x^2
        fx = 3 * j ** 2
        # Append the calculated value to the y list
        y.append(fx)
    # Return the list of y values
    return y


def graph02():
    """
    Generate y values for the function 4x - 3.

    Returns:
        list: A list of y values corresponding to the x values.
    """
    # Initialize an empty list to store y values
    y = []
    # Loop through each value in the x list
    for j in x:
        # Calculate the function value for 4x - 3
        fx = 4 * j - 3
        # Append the calculated value to the y list
        y.append(fx)
    # Return the list of y values
    return y


# Only runs when executed directly, not when imported in another file.
if __name__ == "__main__":
    # Plot the first graph with a label and markers
    plt.plot(x, graph01(), label="Graph 01: f(x) = 3x^2", marker='o')
    # Plot the second graph with a label and markers
    plt.plot(x, graph02(), label="Graph 02: f(x) = 4x - 3", marker='x')
    # Add a title to the graph
    plt.title("Graph Plotting of Two Functions")
    # Label the x-axis
    plt.xlabel("X values")
    # Label the y-axis
    plt.ylabel("Y values")
    # Display the legend
    plt.legend()
    # Add a grid to the graph
    plt.grid(True)
    # Show the plot
    plt.show()
