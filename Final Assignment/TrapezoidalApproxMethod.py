"""
This script imports essential libraries for numerical computations, 
and plotting.

Modules:
- numpy: Provides support for numerical operations and array handling. 
- matplotlib.pyplot: Enables plotting and visualization of data.
"""
import numpy as np
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


def trapezoidal_approx(func, a, b, N):
    """Compute the Midpoint Approximation of Definite Integral of a function over the interval [a,b].

    Parameters
    ----------
    func : function
           Vectorized function of one variable
    a , b : numbers
        Endpoints of the interval [a,b]
    N : integer
        Number of subintervals of equal length in the partition of [a,b]

    Returns
    -------
    float
        Approximation of the definite integral by Midpoint Approximation.
    """

    dx = (b - a) / N  # Step size
    x = np.linspace(a, b, N + 1)  # Equidistant partition points
    return 0.5 * dx * np.sum(func(x[:-1]) + func(x[1:]))  # Trapezoidal Approximation of Definite Integral


if __name__ == "__main__":
    # 1st Function to be integrated
    func_1 = lambda x: x / (x ** 2 + 1)
    # Indefinite Integral of the function
    antiderivative_1 = lambda x: 0.5 * np.log(x ** 2 + 1)  # Your code goes here

    # 2nd Function to be integrated
    func_2 = lambda x: np.exp(x)
    # Indefinite Integral of the function
    antiderivative_2 = lambda x: np.exp(x)  # Your code goes here

    # End points for 1st Function
    a1 = 0
    b1 = 5  # Change the values as required
    # End points for 2nd Function
    a2 = 0
    b2 = 5  # Change the values as required

    # Call the function to Plot the graph of the functions
    # Your code goes here
    plot_function(func_1, a1, b1)
    plot_function(func_2, a2, b2)

    # Number of partition for 1st Function
    N1 = 500  # Change the value as required
    # Number of partition for 2nd Function
    N2 = 500  # Change the value as required

    # Call midpont_method to compute Trapezoidal Approximation:
    trapezoidal_approx_1 = trapezoidal_approx(func_1, a1, b1, N1)  # Your code for 1st function
    trapezoidal_approx_2 = trapezoidal_approx(func_2, a2, b2, N2)  # Your code for 2nd function

    # Calculate the true value of the definite integral
    definite_integral_1 = antiderivative_1(b1) - antiderivative_1(a1)  # For 1st Function
    definite_integral_2 = antiderivative_2(b2) - antiderivative_2(a2)  # For 2nd Function

    # Calculate the absolute error between the approximate value and true value
    error_1 = np.abs(trapezoidal_approx_1 - definite_integral_1)  # For 1st Function
    error_2 = np.abs(trapezoidal_approx_2 - definite_integral_2)  # For 2nd Function

    print(f"Sub-interval width = {(b1 - a1) / N1:.6f}")
    print(f"Trapezoidal Approximation for 1st Function = {trapezoidal_approx_1:.6f}")
    print(f"Actual Value for 1st Function = {definite_integral_1:.6f}")
    print(f"Absolute error between the above methods = {error_1:.8f}")
    print()
    print(f"Sub-interval width = {(b2 - a2) / N2:.6f}")
    print(f"Trapezoidal Approximation for 2nd Function = {trapezoidal_approx_2:.6f}")
    print(f"Actual Value for 2nd Function = {definite_integral_2:.6f}")
    print(f"Absolute error between the above methods = {error_2:.8f}")
