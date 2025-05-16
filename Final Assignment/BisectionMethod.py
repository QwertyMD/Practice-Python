# Bisection Method
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
    if func(a) * func(b) >= 0 or a >= b:
        raise ValueError("The function must have different signs at a and b.")

    iter_count = 1
    while iter_count <= max_iter:
        c = (a + b) / 2
        fa = func(a)
        fc = func(c)
        if abs(fc) <= tol or (b - a) <= tol:
            return c
        iter_count += 1
        if fa * fc > 0:
            a = c
        else:
            b = c

    print("Warning! Exceeded the maximum number of iterations.")
    return c


if __name__ == "__main__":
    # func = lambda x: x ** 2 - x - 1  # First Function
    func = lambda x: x ** 3 - x ** 2 - 2 * x + 1  # Second Function

    plot_function(func, -2, 3)

    # For first root
    a_1 = -2
    b_1 = -1
    our_root_1 = bisection_method(func, a_1, b_1)
    x0 = (a_1 + b_1) / 2
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()
    print(f"1st root found by Bisection Method = {our_root_1:.8f}")
    print(f"1st root found by SciPy = {sp_root_1:.8f}")

    # For second root
    print()
    a_2 = 0
    b_2 = 1
    our_root_2 = bisection_method(func, a_2, b_2)
    x0 = (a_2 + b_2) / 2
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()
    print(f"2nd root found by Bisection Method = {our_root_2:.8f}")
    print(f"2nd root found by SciPy = {sp_root_2:.8f}")

    # For third root
    print()
    a_3 = 1
    b_3 = 2
    our_root_3 = bisection_method(func, a_3, b_3)
    x0 = (a_3 + b_3) / 2
    sp_result_3 = sp.optimize.root(func, x0)
    sp_root_3 = sp_result_3.x.item()
    print(f"3rd root found by Bisection Method = {our_root_3:.8f}")
    print(f"3rd root found by SciPy = {sp_root_3:.8f}")
