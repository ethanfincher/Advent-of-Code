from sympy import symbols, Eq
from sympy.solvers.diophantine import diophantine

# Define the symbols
x, y = symbols('x y')

# Define the equation 5x + 3y = 1
eq = Eq(5*x + 3*y, 1)

# Solve the Diophantine equation
solutions = diophantine(eq)

# Output the solutions
print(solutions)