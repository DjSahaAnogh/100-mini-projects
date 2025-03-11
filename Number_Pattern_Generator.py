from sympy import symbols, sympify
def expression_gen():
    n = symbols('n')
    expression = input("Enter an algebraic expression (use 'n' as variable, e.g., '2*n - 1'): ")
    safe_expr = sympify(expression)  # Converts input safely

    num_terms = int(input("How many terms do you want? "))

    # Generate sequence safely
    sequence = [safe_expr.subs(n, i) for i in range(1, num_terms + 1)]
    print("Generated sequence:", sequence)
if __name__ == "__main__":
    expression_gen()