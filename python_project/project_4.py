'''QUESTION 4'''
import numpy as np

# Resistor values in ohms
R1 = 1
R2 = 2
R3 = 2
R4 = 3
R5 = 2
G = 4

# Voltage source value in volts
V1 = 2

# Coefficient matrix for the equations
A = np.array([
    [R1 + R3 + G, -G, -R3],
    [-G, R2 + G + R4, -G],
    [-R3, -G, R3 + R5 + G]
])

# Constants vector
B = np.array([0, V1, 0])

# Solve for the currents I1, I2, I3
currents = np.linalg.solve(A, B)
I1, I2, I3 = currents

# Print the results
print(f"Loop Currents:")
print(f"I1 = {I1:.2f} A")
print(f"I2 = {I2:.2f} A")
print(f"I3 = {I3:.2f} A")
