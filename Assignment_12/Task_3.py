import pulp

# --- 1. Problem Formulation ---

# Decision Variables:
# x = Number of units of Chocolate A to produce
# y = Number of units of Chocolate B to produce

# Objective Function: Maximize Z = 6x + 5y (Profit)

# Constraints:
# 1. Milk: 1x + 1y <= 5
# 2. Choco: 3x + 2y <= 12
# 3. Non-negativity and Integer: x >= 0, y >= 0, x and y are integers

def solve_chocolate_production():
    """
    Sets up and solves the chocolate production optimization problem
    using PuLP, aiming to maximize profit.
    """
    # 1. Create the LP problem object (Maximization)
    prob = pulp.LpProblem("Chocolate Production Maximization", pulp.LpMaximize)

    # 2. Define Decision Variables
    # The 'Integer' category ensures that the solution will be whole units.
    x = pulp.LpVariable("Units_A", lowBound=0, cat='Integer')
    y = pulp.LpVariable("Units_B", lowBound=0, cat='Integer')

    # 3. Define the Objective Function (to be maximized)
    # Maximize Profit: 6x + 5y
    prob += 6 * x + 5 * y, "Total Profit"

    # 4. Define the Constraints
    # Constraint 1: Milk Availability (max 5 units)
    # 1 unit of A + 1 unit of B <= 5
    prob += 1 * x + 1 * y <= 5, "Milk Constraint"

    # Constraint 2: Choco Availability (max 12 units)
    # 3 units of A + 2 units of B <= 12
    prob += 3 * x + 2 * y <= 12, "Choco Constraint"

    # 5. Solve the problem
    # PuLP automatically chooses an appropriate solver (like Coin-OR's CBC)
    prob.solve()

    # --- 6. Output and Results ---
    
    print("--- Optimization Results ---")
    print(f"Status: {pulp.LpStatus[prob.status]}")

    if prob.status == pulp.LpStatus.Optimal:
        print("\nOptimal Production Plan:")
        
        # Extract and print the optimal values for the variables
        units_a = pulp.value(x)
        units_b = pulp.value(y)
        max_profit = pulp.value(prob.objective)
        
        print(f"Units of Chocolate A to produce (x): {units_a:.0f} units")
        print(f"Units of Chocolate B to produce (y): {units_b:.0f} units")
        print(f"\nMaximum Profit Achieved: Rs {max_profit:.2f}")
        
    else:
        print("\nCould not find an optimal solution.")
        
# Execute the solver function
if __name__ == "__main__":
    # Ensure pulp is installed: pip install pulp
    solve_chocolate_production()