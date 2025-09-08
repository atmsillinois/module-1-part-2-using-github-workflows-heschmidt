"""Assignment 1.

Function to multiply three numbers
"""


def multiply_three_numbers(a, b, c):
    return a * b * c

def main():
    # Get user inputs
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    num3 = float(input("Enter the 3rd number: "))

    # Calculate
    result = multiply_three_numbers(num1, num2, num3)

    # Print 
    print(f"Results: {result}")

if __name__ == "__main__":
    main()