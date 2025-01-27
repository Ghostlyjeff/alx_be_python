# match_case_calculator.py

def main():
    try:
        # Prompt for user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()

        # Perform the calculation using match-case
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}.")
            case "-":
                result = num1 - num2
                print(f"The result is {result}.")
            case "*":
                result = num1 * num2
                print(f"The result is {result}.")
            case "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result is {result}.")
                else:
                    print("Division by zero is not allowed.")
            case _:
                print("Invalid operation selected.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
