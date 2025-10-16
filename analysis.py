


from typing import List, Tuple
from habit import Habit
import datetime

def calculate_average_success_rate(habits: List[Habit]) -> float:
    """
    Calculates the average success rate across all habits.

    Args:
        habits (List[Habit]): List of Habit objects.

    Returns:
        float: Average completion rate as a percentage.
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

        rate = (len(habit.completion_dates) / total_periods) * 100 if total_periods > 0 else 0
        rates.append(rate)

    return sum(rates) / len(rates)


def find_longest_streak(habits: List[Habit]) -> Tuple[str, int]:
    """
    Finds the habit with the longest streak.

    Args:
        habits (List[Habit]): List of Habit objects.

    Returns:
        Tuple[str, int]: Habit name and streak count.
    """
    if not habits:
        return ("None", 0)
    longest = max(habits, key=lambda h: h.current_streak)
    return (longest.name, longest.current_streak)


def get_missed_days(habit: Habit) -> List[datetime.date]:
    """
    Identifies missed days or weeks for a habit.

    Args:
        habit (Habit): The habit to analyze.

    Returns:
        List[datetime.date]: Dates where the habit was missed.
    """
    today = datetime.date.today()
    expected_dates = []
    missed = []

    if habit.periodicity == "daily":
        delta = (today - habit.creation_date).days
        expected_dates = [habit.creation_date + datetime.timedelta(days=i) for i in range(delta + 1)]
    elif habit.periodicity == "weekly":
        delta = (today - habit.creation_date).days // 7
        expected_dates = [habit.creation_date + datetime.timedelta(weeks=i) for i in range(delta + 1)]

    for expected_date in expected_dates:
        if expected_date not in habit.completion_dates:
            missed.append(expected_date)

    return missed
