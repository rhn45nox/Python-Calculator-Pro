import math
from datetime import datetime

# ==========================================
#          PYTHON CALCULATOR PRO
# ==========================================

history = []

def display_header():
    print("\n" + "=" * 45)
    print("          PYTHON CALCULATOR PRO")
    print("=" * 45)
    print("       Smart | Fast | Accurate")
    print("=" * 45)


def display_menu():
    print("\nAVAILABLE OPERATIONS")
    print("-" * 35)
    print("  +   Addition")
    print("  -   Subtraction")
    print("  *   Multiplication")
    print("  /   Division")
    print("  %   Modulus")
    print("  **  Power")
    print("  //  Floor Division")
    print("  H   View History")
    print("  Q   Exit")
    print("-" * 35)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

    elif operator == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot use zero as divisor.")
        return num1 % num2

    elif operator == "**":
        result = num1 ** num2
        if isinstance(result, complex) or not math.isfinite(result):
            raise ValueError("Result is outside the supported range.")
        return result

    elif operator == "//":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 // num2

    else:
        raise ValueError("Invalid operator.")


def show_history():
    print("\n========== CALCULATION HISTORY ==========")

    if not history:
        print("No calculations performed yet.")
    else:
        for index, item in enumerate(history, start=1):
            print(f"{index}. {item}")

    print("=" * 43)


def main():

    display_header()

    while True:

        display_menu()

        operator = input("\nChoose operation: ").strip()

        if operator.lower() == "q":
            print("\nThank you for using Python Calculator Pro!")
            print("Have a great day!")
            break

        elif operator.lower() == "h":
            show_history()
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(num1, operator, num2)

            # Display clean result
            print("\n" + "=" * 35)
            print("              RESULT")
            print("=" * 35)
            print(f"  {num1:g} {operator} {num2:g} = {result:g}")
            print("=" * 35)

            # Save history
            timestamp = datetime.now().strftime("%H:%M:%S")

            history.append(
                f"{num1:g} {operator} {num2:g} = {result:g} [{timestamp}]"
            )

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()