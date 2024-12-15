# finance_calculator.py

# Get user input for monthly income and expenses using the required prompt
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

# Calculate monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

# Calculate projected annual savings with 5% interest
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Output results
print(f"Your monthly savings: ${monthly_savings:.2f}")
print(f"Your projected annual savings after interest: ${annual_savings:.2f}")
