# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process priority using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority level"

# Add time sensitivity note if applicable
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."

# Final output
print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!.")
