# multiplication_table.py

def main():
    try:
        # Prompt user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
