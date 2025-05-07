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
    # Main Loop starts here
    iter_count = 1
    while iter_count <= max_iter:
        # Your code goes here
        if abs(grad(x0) <= tol):
            print("Math Error! Found root may not be correct.")
            return x0
        x1 = x0 - func(x0) / grad(x0)
        x0 = x1
        if abs(func(x0)) <= tol:
            return x0
        iter_count += 1

    print("Warning! Exceeded the maximum number of iterations.")
    return x0


# Main Driver Function:
if __name__ == "__main__":
    # Define the 1st Function for which the root is to be found
    func1 = lambda x: x ** 2 - x - 1
    # Define the gradient of the Function
    grad1 = lambda x: 2 * x - 1

    # Uncomment the next two lines to use the 2nd Function
    func2 = lambda x: x ** 3 - x ** 2 - 2 * x + 1
    grad2 = lambda x: 3 * x ** 2 - 2 * x - 2

    # Call plot_function to plot graph of the function
    # Your code goes here
    plot_function(func1, 1, 3)  # For first function
    plot_function(func2, -2, 4)  # For second function

    x0 = 1  # Initial guess for 1st (change the value as required)
    # Call the Newton's method for 1st root
    our_root_1 = newton_method(func1, grad1, x0)  # Your code goes here

    # Call SciPy method (reference method) for 1st root
    sp_result_1 = sp.optimize.root(func1, x0)
    sp_root_1 = sp_result_1.x.item()

    # Call the Newton's method for 2nd root
    x0 = 2  # Initial guess for 2nd root (change the value as required)
    our_root_2 = newton_method(func2, grad2, x0)  # Your code goes here

    # Call SciPy method (reference method) for 2nd root
    sp_result_2 = sp.optimize.root(func2, x0)
    sp_root_2 = sp_result_2.x.item()

    # Print the result
    print(f"1st root found by Newton's Method = {our_root_1:.8f}")
    print(f"1st root found by SciPy = {sp_root_1:.8f}")
    print()
    print(f"2nd root found by Newton's Method = {our_root_2:.8f}")
    print(f"2nd root found by SciPy = {sp_root_2:.8f}")
