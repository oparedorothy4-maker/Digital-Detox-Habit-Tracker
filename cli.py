from habit_manager import HabitManager
from db import DatabaseConnector
from analysis import calculate_average_success_rate
from analysis import find_longest_streak

def create_habit_cli(manager: HabitManager):
    """
    CLI interface for creating a new habit.
    Prompts the user to enter a habit name and choose a periodicity
    (daily or weekly), then creates the habit in the system.
    """

    name = input("Enter habit name: ").strip() # Remove extra spaces
    periodicity = input ("Enter periodicity (daily/weekly):").strip().lower()
    
    # Validates periodicity
    if periodicity not in ["daily", "weekly"]:
        print("Invalid periodicity! Please enter 'daily' or 'weekly'.")
        return
    
    # Check for Duplicate
    existing = [h for h in manager.list_habits() if h.name.lower() == name.lower()]
    if existing:
        print(f"Habit '{name}' already exists!")
        return
    
    # Creates the Habit
    habit = manager.create_habit(name, periodicity)
    print(f"Habit '{habit.name}' created successfully with ID {habit.id}.")

def complete_habit_cli(manager: HabitManager):
    """
    Mark habit as completed through the CLI.

    Prompts the user to enter the habit ID and marks it as completed
    if it exists in the system.
    """

    try:
        habit_id = int(input("Enter habit ID to complete: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    success = manager.complete_habit(habit_id)
    if success:
        print("Habit marked as completed.")
    else:
        print("Habit not found.")


def delete_habit_cli(manager: HabitManager):
    """
    Delete a habit by its ID using the CLI.
    Asks the user for a habit ID and deletes if it exists.
    """

    try: 
        habit_id = int(input("Enter habit ID to delete: "))
    except ValueError: 
        print("Invalid input! Please enter a number.")
        return
    success = manager.delete_habit(habit_id)
    if success:
        print(f"Habit with ID {habit_id} has been deleted.")
    else:
        print("Habit not found.")


def list_habits_cli(manager: HabitManager):
    """
    Display all tracked habits and their current streaks.

    Shows habit ID, name, periodicity, and current streak
    for each habit stored in the database.
    """

    habits = manager.db.get_all_habits()
    if not habits:
        print("No habits found.")
        return
    print("\n=== Your Habits ===")
    for habit in habits:
        print(f"ID: {habit.id} /  Name: {habit.name} / Periodicity: {habit.periodicity} / Current Streak: {habit.current_streak}")
    print()

def show_analysis_cli(manager: HabitManager):
    """
    Display simple analytics for all habits.

    Shows the average success rate across habits and the habit
    with the longest current streak.
    """

    habits = manager.db.get_all_habits()
    if not habits:
        print("No habits found.")
        return
    
    avg_rate = calculate_average_success_rate(habits)
    longest_name, longest_streak = find_longest_streak(habits)
    print("\n=== Habit Analytics ===")
    print(f"Average success rate: {avg_rate:.2f}%")
    print(f"Longest streak: {longest_name} with {longest_streak} days\n")

def main():
    """
    Run the main CLI loop for the Habit Tracker.

    Provides a simple text-based interface where users can
    create, complete, list , delete habits, or view analytics
    """

    db = DatabaseConnector()
    manager = HabitManager(db)

    while True:
        print("1. Create a habit")
        print("2. Complete a habit")
        print("3. List habits")
        print("4. Show analytics")
        print("5. Delete a habit")
        print("6. Exit)")
        choice = input ("Choose an option: ").strip()


        if choice == "1":
            create_habit_cli(manager)
        elif choice == "2":
            complete_habit_cli(manager)
        elif choice == "3":
            list_habits_cli(manager)
        elif choice == "4":
            show_analysis_cli(manager)
        elif choice == "5":
            delete_habit_cli(manager)    
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.\n")

if __name__ == "__main__":
    main()

