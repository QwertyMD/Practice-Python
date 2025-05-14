# Root Finding Method
"""
This script imports essential libraries for numerical computations, 
optimization, and plotting.

Modules:
- numpy: Provides support for numerical operations and array handling.
- scipy: Offers algorithms, including root-finding methods.
- matplotlib.pyplot: Enables plotting and visualization of data.
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    # Your code goes here
    x = np.linspace(a, b, 100)
    y = func(x)
    plt.plot(x, y, label="f(x)")
    plt.title("Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Bisection method to find the root of a function within a given interval.

    Parameters:
    - func: The function for which the root is to be found.
    - a, b: Interval [a, b] within which the root is searched for.
    - tol: Tolerance level for checking convergence of the method.
    - max_iter: Maximum number of iterations.

    Returns:
    - root: Approximation of the root.
    
    Example
    --------
    # >>> fun = lambda x: x**2 - x - 1
    # >>> root = bisection_method(fun, 1, 2, max_iter=20)
    """

    # Check if the interval is valid (signs of f(a) and f(b) are different)
    # Your code goes here
    if func(a) * func(b) >= 0 or a >= b:
        raise ValueError("The function must have different signs at a and b.")

    # Main loop starts here
    iter_count = 1
    while iter_count <= max_iter:
        # your code goes here
        c = (a + b) / 2
        fa = func(a)
        fc = func(c)
        if abs(fc) < tol or (b - a) <= tol:
            return c
        iter_count += 1
        if fa * fc > 0:
            a = c
        else:
            b = c

    print("Warning! Exceeded the maximum number of iterations.")
    return c


# Example usage:
if __name__ == "__main__":
    # Define the function for which the root is to be found
    func1 = lambda x: x ** 2 - x - 1  # First Function

    # Uncomment the below line to use the Second Function
    func2 = lambda x: x ** 3 - x ** 2 - 2 * x + 1  # Second Function
    # Call plot_function to plot graph of the function
    # Your code goes here
    # plot_function(func1, 1, 3)  # For first function
    # plot_function(func2, 1, 3)  # For second function

    # Set the interval [a, b] for the search
    a_1 = 1
    b_1 = 2  # For first root (change the values as required)
    a_2 = 1
    b_2 = 2  # For second root (change the values as required)

    # Call the bisection method
    our_root_1 = bisection_method(func1, a_1, b_1)  # your code goes here
    our_root_2 = bisection_method(func2, a_2, b_2)  # your code goes here

    # Call SciPy method root, which we consider as a reference method.
    x0 = (a_1 + b_1) / 2
    sp_result_1 = sp.optimize.root(func1, x0)
    sp_root_1 = sp_result_1.x.item()

    x0 = (a_2 + b_2) / 2
    sp_result_2 = sp.optimize.root(func2, x0)
    sp_root_2 = sp_result_2.x.item()

    # Print the result
    print(f"1st root found by Bisection Method = {our_root_1:.8f}")
    print(f"1st root found by SciPy = {sp_root_1:.8f}")
    print()
    print(f"2nd root found by Bisection Method = {our_root_2:.8f}")
    print(f"2nd root found by SciPy = {sp_root_2:.8f}")
