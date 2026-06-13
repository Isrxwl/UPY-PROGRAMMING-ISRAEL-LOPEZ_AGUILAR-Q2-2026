import math

# Helper function to evaluate f(x) depending on the user's choice
def evaluate_function(choice, x):
    if choice == 1:
        return (x**2) + (2*x) - 3  # P1: Polynomial
    elif choice == 2:
        return math.sin(x)         # T1: Sine
    elif choice == 3:
        return math.exp(x)         # Tr1: Exponential

# Helper function to calculate the exact analytical value
def calculate_exact_integral(choice, a, b):
    if choice == 1:
        # Integral of x^2 + 2x - 3 is (x^3)/3 + x^2 - 3x
        def F(x): return (x**3)/3 + (x**2) - (3*x)
        return F(b) - F(a)
    elif choice == 2:
        # Integral of sin(x) is -cos(x)
        def F(x): return -math.cos(x)
        return F(b) - F(a)
    elif choice == 3:
        # Integral of e^x is e^x
        def F(x): return math.exp(x)
        return F(b) - F(a)

# ==========================================
# INPUT
# ==========================================
print("--- Numerical Integration ---")
print("Select a function to integrate:")
print("1: Polynomial (x^2 + 2x - 3)")
print("2: Sine (sin(x))")
print("3: Exponential (e^x)")
function_choice = int(input("Choice (1-3): "))

a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))

print("\nSelect a mode:")
print("1: Default (n=100, Midpoint)")
print("2: Custom (You choose n and method)")
print("3: Auto-adjust (Converges to target error)")
mode_choice = int(input("Mode (1-3): "))

# ==========================================
# PROCESS
# ==========================================
# Step 1: Calculate the exact analytical value
exact_value = calculate_exact_integral(function_choice, a, b)

# Step 2: Configure parameters based on the selected mode
if mode_choice == 1:
    n = 100
    method = 3  # 3 corresponds to Midpoint
    target_error = 0
    auto_adjust = False

elif mode_choice == 2:
    n = int(input("Enter the number of subintervals (n): "))
    print("Select a method: 1 (Left), 2 (Right), 3 (Midpoint), 4 (Trapezoid)")
    method = int(input("Method (1-4): "))
    target_error = 0
    auto_adjust = False

elif mode_choice == 3:
    target_error = float(input("Enter the target relative error threshold (%): "))
    n = 10      # Start with n=10 as suggested in tips
    method = 3  # Midpoint is generally the most accurate single rectangle method
    auto_adjust = True

# Step 3: Integration Loop
loop_active = True

while loop_active:
    h = (b - a) / n
    sum_value = 0
    numerical_result = 0
    
    # Left Rectangle Method
    if method == 1:
        for i in range(0, n):
            x_i = a + (i * h)
            sum_value += evaluate_function(function_choice, x_i)
        numerical_result = h * sum_value
        
    # Right Rectangle Method
    elif method == 2:
        for i in range(1, n + 1):
            x_i = a + (i * h)
            sum_value += evaluate_function(function_choice, x_i)
        numerical_result = h * sum_value
        
    # Midpoint Rectangle Method
    elif method == 3:
        for i in range(0, n):
            x_i = a + (i * h) + (h / 2)
            sum_value += evaluate_function(function_choice, x_i)
        numerical_result = h * sum_value
        
    # Trapezoid Method
    elif method == 4:
        for i in range(1, n):
            x_i = a + (i * h)
            sum_value += evaluate_function(function_choice, x_i)
        sum_value = sum_value * 2
        sum_value += evaluate_function(function_choice, a)
        sum_value += evaluate_function(function_choice, b)
        numerical_result = (h / 2) * sum_value

    # Step 4: Error Analysis
    absolute_error = abs(exact_value - numerical_result)
    
    # Avoid division by zero if exact_value is exactly 0
    if exact_value != 0:
        relative_error = (absolute_error / abs(exact_value)) * 100
    else:
        relative_error = 0.0
    
    # Step 5: Check Auto-adjust condition
    if auto_adjust:
        if relative_error <= target_error:
            loop_active = False  # Target reached, exit loop
        else:
            n = n * 2            # Double n and try again
    else:
        loop_active = False      # Run only once for modes 1 and 2

# ==========================================
# OUTPUT
# ==========================================
print("\n--- Results ---")
print(f"Exact integral:       {exact_value:.6f}")
print(f"Numerical integral:   {numerical_result:.6f}")
print(f"Absolute Error:       {absolute_error:.6f}")
print(f"Relative Error (%):   {relative_error:.6f}%")
print(f"Iterations (n) used:  {n}")
