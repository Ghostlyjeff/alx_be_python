# pattern_drawing.py

def main():
    try:
        # Prompt user for pattern size
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Initialize row counter for the while loop
        row = 0

        while row < size:
            # Use a for loop to print asterisks for the current row
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after the row is complete
            row += 1

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
