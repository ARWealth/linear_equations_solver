"""
Solve and graph linear functions.
Write linear equations in slope intercept form
y = mx + b
"""

from slope_and_y_intercept import slope
from slope_and_y_intercept import y_intercept
import matplotlib.pyplot as plt
import numpy as np

# Main loop
while True:
	# Enter values
	x_1 = input("Enter X1: ")
	if x_1 == 'q' or x_1 == 'Q':
		break
	y_1 = input("Enter Y1: ")
	if y_1 == 'q' or y_1 == 'Q':
		break
	x_2 = input("Enter X2: ")
	if x_2 == 'q' or x_2 == 'Q':
		break
	y_2 = input("Enter Y2: ")	
	if y_2 == 'q' or y_2 == 'Q':
		break
	b = input("Enter the y-intercept (b): ")
	if b == 'q' or b == 'Q':
		break

	try:
		m_slope = slope(x_1, y_1, x_2, y_2)
		the_y_intercept = y_intercept(b)

		# Use numpy array to calculate the root
		root = np.roots([m_slope, the_y_intercept])

		print(f"Slope(m) of the line that passes through points "
			f"({x_1}, {y_1}) and ({x_2}, {y_2}) is {m_slope}.\nThe "
			f"equation of the line in slope-intecept form is "
			f"y = {m_slope}x + {the_y_intercept}.\nThe x-intercept "
			f"is {root[0]}.")

		# Graphing 
		# Set up array of 100 linearly spced x values
		x = np.linspace(-10, 10, 100)
		# Function to be graphed
		y = (m_slope*x) + (the_y_intercept)

		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)

		# Add title, labels and grid
		plt.title(f"Graph of y = {m_slope}x + {the_y_intercept}", fontsize=12, fontweight='bold', color='r')
		plt.xlabel("x axis", c='b', loc='right')
		plt.ylabel("y axis", c='b', loc='top')
		plt.grid(True)

		# Design axes
		ax.spines['left'].set_position('center')
		ax.spines['bottom'].set_position('zero')
		ax.spines['left'].set_color('b')
		ax.spines['bottom'].set_color('b')
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		
		# Plot and show the function
		plt.plot(x, y, 'r')
		plt.show()
	
	except (ValueError, ArithmeticError):
		print("Invalid input!")
		continue



