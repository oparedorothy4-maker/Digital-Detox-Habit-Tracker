from typing import List, Tuple
from habit import Habit
import datetime

#HABIT LISTING FUNCTIONS

def list_all_habits(habits: List[Habit])-> List[str]:
    """
    Return a list containing the names of all tracked habits.
    
    Args:
    habits (List[Habit]): List of Habit objects.
    
    Returns:
    List[str] Names of all habits
    """

    return [h.name for h in habits]
def list_by_periodicity(habits: List[Habit],periodicity: str) -> List[str]:
    """
    Returns habit names filtered by periodicity.
    
    Args:
        habits (List[Habit]): List of Habit objects.
        periodicity (str): 'daily' or 'weekly'.
    
    Returns:
        List[str]: Names of matching habits.
    """
    
    return [h.name for h in habits if h.periodicity == periodicity]


def calculate_average_success_rate(habits: List[Habit]) -> float:
    """
    Calculates the average success rate across all habits since creation.

    Args:
        habits (List[Habit]): List of Habit objects.

        Returns:
            float: Average completion rate as a percentage (rounded to 2 decimal places.)
    """

    if not habits:
        return 0.0
    
    rates = []
    today = datetime.date.today()
    for habit in habits:
        if habit.periodicity == "daily":
            total_periods = (today - habit.creation_date).days + 1
        elif habit.periodicity == "weekly":
            total_periods = ((today - habit.creation_date).days // 7) + 1
        else:
            total_periods = 1

        rate = (len(habit.completion_dates) /total_periods) * 100 if total_periods > 0 else 0
        rates.append(rate)
    return round(sum(rates) / len(rates), 2)

def find_longest_streak(habits: List[Habit]) -> Tuple[str,int]:
    """
    Find the habit with the longest currently active streak.
    
    Args:
        habits (List[Habit]): List of Habit objects.
        
    Returns:
        Tuple[str, int]: Habit name and its current streak count.
        Returns("None", 0) if the input list is empty.
    """

    if not habits:
        return ("None", 0)
    longest = max(habits, key=lambda h: h.current_streak)
    return (longest.name, longest.current_streak)

def longest_streak_for_habit(habit: Habit) -> int:
    """
    Returns the currently active streak count for a single habit.
    
    Args:
        habit (Habit): The habit object to check.
    
    Returns:
        int: The current streak count.
    """
    return habit.current_streak 

#MISSED DAYS ANALYSIS

def get_missed_days(habit: Habit) -> List[datetime.date]:
    """
    Identifies all missed periods (days or weeks) since the habit creation.
    
    Args:
        habit (Habit): The habit to analyze.

    Returns:
        List[datetime.date]: Dates of missed periods.
         ( For weekly habits, this is the start date of the missed week).
    """
    
    today = datetime.date.today()
    expected_dates = []
    missed = []
    
    if habit.periodicity == "daily":
        delta = (today - habit.creation_date).days
        expected_dates = [habit.creation_date + datetime.timedelta(days=i) for i in range(delta + 1)]
    elif habit.periodicity == "weekly":
        delta = (today -habit.creation_date).days // 7
        expected_dates = [habit.creation_date + datetime.timedelta(weeks=i) for i in range(delta + 1)]
    
    for expected_date in expected_dates:
        if expected_date not in habit.completion_dates:
            missed.append(expected_date)

    return missed


 

  