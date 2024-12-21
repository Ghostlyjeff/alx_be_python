# daily_reminder.py

def main():
    try:
        # Prompt for task input
        task = input("Enter your task for today: ").strip()
        priority = input("Enter the priority level (high, medium, low): ").strip().lower()
        time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

        # Process the task based on priority
        match priority:
            case "high":
                reminder = f"Task: '{task}' has HIGH priority."
            case "medium":
                reminder = f"Task: '{task}' has MEDIUM priority."
            case "low":
                reminder = f"Task: '{task}' has LOW priority."
            case _:
                print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
                return

        # Check if the task is time-bound
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
        elif time_bound != "no":
            print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
            return

        # Print the customized reminder
        print(reminder)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
