from habit_manager import HabitManager
from habit import Habit
from db import DatabaseConnector
from example_data import get_example_habits

# list habits in CLI
def list_habits_cli(manager):
    """List all habits with details including streak"""
    habits= manager.list_habits()
    if not habits:
        print("No habits found.")
        return
    print("\n=== Your Habits ===")
    print("ID | Name | Periodicity | Current Streak")
    print("----------------------------------------")
    for habit in habits:
        print(f"{habit.id} |  {habit.name.strip()} | {habit.periodicity} | {habit.current_streak} day{'s' if habit.current_streak!= 1 else ''}")
    print("------------------------------------------\n")

def main():
    """
    Main function to demonstrate saving and loading habits using SQLite.
    Steps:
    1. Initialize the HabitManagerDB (creates SQLite DB if it doesn't exist).
    2. Load all habits from the database on app startup.
    3. Add a new habit and automatically save it.
    4. Mark a habit as completed today and automatically save it.
    5. Reload all habits and print updates.
    """
    # Initialize data connector and manager
    db = DatabaseConnector()
    manager = HabitManager(db)

    # Load example habits only if database is empty
    if not manager.list_habits():
        for habit in get_example_habits():
            db.save_habit(habit)
        print("Example habits loaded successfuly!\n")
    else:
        print("Habits already exist in the database.\n")   

    # Show all habit in Database
    list_habits_cli(manager)

if __name__ == "__main__":
    main()









   