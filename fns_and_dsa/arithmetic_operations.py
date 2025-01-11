def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation based on the operation parameter.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform. Possible values: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
    - The result of the arithmetic operation, or an appropriate message for invalid operations or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
