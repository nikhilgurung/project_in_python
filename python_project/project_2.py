'''QUESTION NUMBER 2'''

import numpy as np
import matplotlib.pyplot as plt

def calculate_pi_approximation(N):
    """Calculate the approximation of pi using the Madhava-Leibniz series."""
    pi_approx = 0
    for k in range(N):
        pi_approx += ((-1)**k) / (2 * k + 1)
    pi_approx *= 4  # Madhava-Leibniz series gives pi/4, so multiply by 4
    return pi_approx

def plot_error(N):
    """Plot the error in the approximation of pi as the number of terms increases."""
    actual_pi = np.pi  # Use numpy's pi for the actual value of pi
    errors = []  # List to store error values

    for i in range(1, N + 1):
        pi_approx = calculate_pi_approximation(i)
        error = abs(actual_pi - pi_approx)  # Calculate the error
        errors.append(error)

    # Plotting the error
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, N + 1), errors, label='Error', color='blue')
    plt.xlabel('Number of Terms (N)')
    plt.ylabel('Error')
    plt.title('Error in Pi Approximation using Madhava-Leibniz Series')
    plt.yscale('log')  # Use a logarithmic scale for better visualization
    plt.grid(True)
    plt.legend()
    plt.show()

# Input number of terms
N = 100  # Given N = 100
plot_error(N)


