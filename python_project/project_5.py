'''QUESTION 5'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data: Years and CO2 concentrations
years = np.array([
    1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 
    2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009
])
ppm = np.array([
    356.8, 358.2, 360.3, 361.8, 364.0, 365.7, 366.7, 368.2,
    370.5, 372.2, 374.9, 376.7, 378.7, 381.0, 382.9, 384.7
])

# Perform linear regression to fit a straight line through the data
slope, intercept, r_value, p_value, std_err = linregress(years, ppm)

# Calculate the average increase per year (slope)
average_increase_per_year = slope

# Calculate the standard deviation of the CO2 concentration
standard_deviation = np.std(ppm)

# Print the results
print(f"Average increase in CO2 concentration per year: {average_increase_per_year:.2f} ppm/year")
print(f"Standard deviation of CO2 concentration: {standard_deviation:.2f} ppm")

# Plot the data points and the fitted line
plt.figure(figsize=(10, 6))
plt.scatter(years, ppm, color='blue', label='Data Points')
plt.plot(years, slope * years + intercept, color='red', label='Fitted Line')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration (ppm)')
plt.title('Annual Atmospheric CO2 Concentration in Antarctica')
plt.legend()
plt.grid(True)
plt.show()

