# habit.py
from datetime import datetime, timedelta

class Habit:
    """
    Represents a digital detox habit.
    Example: 'No phone after 9 PM' or 'No social media before breakfast'
    """

    def __init__(self, name: str, periodicity: str):
        """
        Initialize a new habit with its name and periodicity (daily or weekly)
        """
        self.name = name
        self.periodicity = periodicity.lower()
        self.creation_date = datetime.now().date()
        self.completion_dates = []  # stores the days the habit was completed

    def complete_task(self):
        """Mark the habit as completed for today"""
        today = datetime.now().date()
        if today not in self.completion_dates:
            self.completion_dates.append(today)
            print(f"Habit '{self.name}' marked as completed for {today}.")
        else:
            print(f"Habit '{self.name}' is already marked as completed today.")

    def calculate_streak(self):
        """
        Calculate the current streak of consecutive completions
        """
        if not self.completion_dates:
            return 0

        sorted_dates = sorted(self.completion_dates, reverse=True)
        streak = 1
        for i in range(1, len(sorted_dates)):
            if (sorted_dates[i-1] - sorted_dates[i]).days == 1:
                streak += 1
            else:
                break
        return streak

    def missed_days(self):
        """
        Estimate missed days since creation based on periodicity
        """
        today = datetime.now().date()
        total_days = (today - self.creation_date).days + 1

        if self.periodicity == "daily":
            expected_days = total_days
        elif self.periodicity == "weekly":
            expected_days = total_days // 7
        else:
            expected_days = 0

        missed = expected_days - len(self.completion_dates)
        return max(missed, 0)

    def __repr__(self):
        """Readable representation for debugging and CLI output"""
        return (f"Habit(name='{self.name}', periodicity='{self.periodicity}', "
                f"streak={self.calculate_streak()}, missed_days={self.missed_days()})")
