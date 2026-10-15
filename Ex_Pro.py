while True:

    print("\n===== Simple Calculator =====")
    print("Type 'exit' to stop the program.")

    first_input = input("Enter first number: ")

    # Check if user wants to exit
    if first_input.lower() == "exit":
        print("Calculator closed.")
        break

    second_input = input("Enter second number: ")

    # Check if user wants to exit
    if second_input.lower() == "exit":
        print("Calculator closed.")
        break

    operator = input("Enter operator (+, -, *, //): ")

    # Check if user wants to exit
    if operator.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        # Convert input into numbers
        num1 = float(first_input)
        num2 = float(second_input)

        # Addition
        if operator == "+":
            result = num1 + num2

        # Subtraction
        elif operator == "-":
            result = num1 - num2

        # Multiplication
        elif operator == "*":
            result = num1 * num2

        # Division
        elif operator == "//":
            result = num1 // num2

        # Invalid operator
        else:
            print("Error: Invalid operator.")
            continue

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")