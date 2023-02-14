from slope_y_intercept import slope
from slope_y_intercept import y_intercept

def linear_functions():
	"""Display Linear Equations"""
	while True:
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

		b = input("Enter the y-intercept (b)")

		try:
			m_slope = slope(x_1, y_1, x_2, y_2)
			the_y_intercept = y_intercept(b)

			print(f"Slope(m) of the line that passes through points "
				f"({x_1}, {y_1}) and ({x_2}, {y_2}) is {m_slope}.\nThe "
				f"equation of the line in slope-intecept form is "
				f"y = {m_slope}x + {the_y_intercept}.")

		except (ValueError, ArithmeticError):
			print("Invalid input!")
			continue



