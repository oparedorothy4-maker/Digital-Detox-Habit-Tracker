import pytest
from datetime import date, timedelta
from habit import Habit
from habit_manager import HabitManager
from db import DatabaseConnector
from analysis import calculate_average_success_rate, find_longest_streak


@pytest.fixture
def habit_manager():
    """Fixture to initialize a HabitManager with an in-memory database for testing."""

    db = DatabaseConnector(":memory:")
    manager = HabitManager(db)
    return manager

def test_create_habit(habit_manager):
    """
    Test the creation of a new habit.
    
    Verifies that:
    The habit receives an ID.
    The periodicity is correctly set.
    The initial streak is zero.
    """
    habit = habit_manager.create_habit("No Phone After 9pm", "daily")
    assert habit.id is not None
    assert habit.periodicity == "daily"

    assert habit.current_streak == 0

def test_complete_habit(habit_manager):
    """
    Test completing a habit.
    
    Verifies that:
    Completing a habit today succeeds.
    Attempting to complete the habit again today does not increase the streak.
    The habit's current streak is correctly updated.
    """
    habit = habit_manager.create_habit("No Social Media", "daily")
    success = habit_manager.complete_habit(habit.id)
    assert success is True

    success_again = habit_manager.complete_habit(habit.id)
    assert success_again is False
    loaded_habit = habit_manager.db.get_habit_by_id(habit.id)
    assert date.today() in loaded_habit.completion_dates
    assert loaded_habit.current_streak == 1

def test_delete_habit(habit_manager):
    """
    Test deleting a habit.
    
    Verifies that:
    A habit can be deleted successfully.
    Deleted habits are no longer retrievable from the database.
    """
    habit = habit_manager.create_habit("Read Instead of Scrolling", "daily")
    deleted = habit_manager.delete_habit(habit.id)
    assert deleted is True

    removed = habit_manager.db.get_habit_by_id(habit.id)
    assert removed is None

def test_list_by_periodicity(habit_manager):
    """
    Test listing habits by their periodicity.
    
    Verifies that:
    Daily habits are correctly listed under 'daily'.
    Weekly habits are correctly listed under 'weekly'.
    """
    habit_manager.create_habit("Daily Habit", "daily")
    habit_manager.create_habit("Weekly Habit", "weekly")
    daily = habit_manager.list_by_periodicity("daily")
    weekly = habit_manager.list_by_periodicity("weekly")
    assert all(h.periodicity == "daily" for h in daily)
    assert all(h.periodicity == "weekly" for h in weekly)
    
def test_analytics_functions(habit_manager):
    """
    Test analytics functions: average success rate and longest streak.
    
    Verifies that:
    - Average success rate is greater than 0 after completing habits.
    - The longest streak is reported correctly.
    """
    habit1 = habit_manager.create_habit("Habit 1", "daily")
    habit2 = habit_manager.create_habit("Habit 2", "daily")

    habit_manager.complete_habit(habit1.id)
    habit_manager.complete_habit(habit2.id)

    habits = habit_manager.db.get_all_habits()
    avg_rate = calculate_average_success_rate(habits)
    longest_name, longest_streak = find_longest_streak(habits)

    assert avg_rate > 0
    assert longest_name in [habit1.name, habit2.name]
    assert longest_streak >= 1
    
   
   