# Newton's Method
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


def newton_method(func, grad, x0, tol=1e-6, max_iter=100):
    """Approximate solution of f(x)=0 by Newton-Raphson's method.

        Parameters
        ----------
        func : function 
            Function value for which we are searching for a solution f(x)=0,
        grad: function
            Gradient value of function f(x)
        x0 : number
            Initial guess for a solution f(x)=0.
        tol : number
            Stopping criteria is abs(f(x)) < tol.
        max_iter : integer
            Maximum number of iterations of Newton's method.

        Returns
        -------
        xn : root

        Example
        --------
        # >>> fun = lambda x: x**2 - x - 1
        # >>> grad = lambda x: 2*x - 1
        # >>> root = newton_method(fun, grad, 1, max_iter=20)
        """
    iter_count = 1
    while iter_count <= max_iter:
        if abs(grad(x0)) <= 1e-12:
            print("Math Error! Found root may not be correct.")
            return x0
        x1 = x0 - func(x0) / grad(x0)
        x0 = x1
        if abs(func(x0)) <= tol:
            return x0
        iter_count += 1

    print("Warning! Exceeded the maximum number of iterations.")
    return x0


if __name__ == "__main__":
    # func = lambda x: x ** 2 - x - 1  # First Function
    # grad = lambda x: 2 * x - 1  # Gradient of first function

    func = lambda x: x ** 3 - x ** 2 - 2 * x + 1  # Second Function
    grad = lambda x: 3 * x ** 2 - 2 * x - 2  # Gradient of second function

    plot_function(func, -2, 3)

    # For first root
    x0 = -1.3  # Initial guess for 1st root
    our_root_1 = newton_method(func, grad, x0)
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()
    print(f"1st root found by Newton's Method = {our_root_1:.8f}")
    print(f"1st root found by SciPy = {sp_root_1:.8f}")

    # For second root
    print()
    x0 = 0.4  # Initial guess for 2nd root
    our_root_2 = newton_method(func, grad, x0)
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()
    print(f"2nd root found by Newton's Method = {our_root_2:.8f}")
    print(f"2nd root found by SciPy = {sp_root_2:.8f}")
    
    # For third root
    print()
    x0 = 1.8  # Initial guess for 3rd root
    our_root_3 = newton_method(func, grad, x0)
    sp_result_3 = sp.optimize.root(func, x0)
    sp_root_3 = sp_result_3.x.item()
    print(f"3rd root found by Newton's Method = {our_root_3:.8f}")
    print(f"3rd root found by SciPy = {sp_root_3:.8f}")
