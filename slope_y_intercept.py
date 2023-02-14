def slope(x_1, y_1, x_2, y_2):
	"""Calculate the slope of linear equations."""
	x_1 = float(x_1)
	y_1 = float(y_1)
	x_2 = float(x_2)
	y_2 = float(y_2)

	m = (y_2 - y_1) / (x_2 - x_1)
	return m

def y_intercept(b):
	"""Return the y-intercept (b) of the line."""
	b = float(b)
	return b

		
