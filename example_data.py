from datetime import date, timedelta
from habit import Habit

""" 
example_data.py

Purpose: Provides sample habits for testing and demonstration
of the Digital Detox Tracker project.

It defines:
5 digital detox habits (3 daily, 2 weekly),
each with 4 weeks of sample completions

These examples help demonstrate how the Habit Tracker app stores,
tracks, and analyzes habits.
"""
# Create today's data reference
today = date.today()

# Daily Habit Example 
daily_habit = Habit(
    name="No Social Media After 9pm",
    periodicity="daily",
    creation_date=today - timedelta(days=28)
)

#Mark as completed for 28 consecutive days (4 weeks)
for i in range(28):
   daily_habit.completion_dates.append(today - timedelta(days=i))
daily_habit.update_streak()


# Weekly Habit Example
weekly_habit = Habit( 
    name="Screen-Free Sunday",
    periodicity="weekly",
    creation_date=today - timedelta(weeks=4)
)

#Mark as completed for the last 4 weeks
for i in range(4):
    weekly_habit.completion_dates.append(today - timedelta(weeks=i))
weekly_habit.update_streak()

#Additional Daily Habit
daily_habit2 = Habit( 
    name="No Phone During Meals",
    periodicity="daily",
    creation_date=today - timedelta(days=28)
)
for i in range (28):
    daily_habit2.completion_dates.append(today - timedelta(days=i))
daily_habit2.update_streak()

#Additional Daily Habit
daily_habit3 = Habit( 
    name="Read Instead of Scrolling",
    periodicity="daily",
    creation_date=today - timedelta(days=28)
)
for i in range(28):
    daily_habit3.completion_dates.append(today - timedelta(days=i))
daily_habit3.update_streak()


#Additional Habit
weekly_habit2 = Habit(
    name="No TV Saturday",
    periodicity="weekly",
    creation_date=today - timedelta(weeks=4)
)
for i in range(4):
    weekly_habit2.completion_dates.append(today - timedelta(weeks=i))
weekly_habit2.update_streak()

    
#Combine the habits into a list for easy import in other modules
habits = [daily_habit, daily_habit2, daily_habit3, weekly_habit, weekly_habit2]

def get_example_habits():
    """
    Returns the example habits (daily and weekly) for testing and demonstration.
    
    Returns:
        list[Habit]: A list containing the 5 example Habit instances, 
        with pre-filled completion dates.
    """    
    return habits





