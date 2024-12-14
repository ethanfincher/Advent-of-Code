import sympy as sp

# Define the known constants
a_x, b_x, a_y, b_y = 94, 22, 34, 67  # Replace with your values
p_x, p_y = 8400, 5400  # Replace with your values


# Define symbols for the unknowns
a, b = sp.symbols('a b')

# Define the system of equations
eq1 = sp.Eq(a_x * a + b_x * b, p_x)
eq2 = sp.Eq(a_y * a + b_y * b, p_y)

# Solve the system of equations
solution = sp.solve([eq1, eq2], (a, b))

# Display the solution
print("Solution for a and b:", solution)