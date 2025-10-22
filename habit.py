from datetime import date, timedelta
from typing import List, Optional

class Habit:
    """
    Represents a digital detox habit tracked by the user.
    Attributes:
        id (int): Unique identifier for the habit.
        name (str): Name of the Habit (eg., "No phone after 9pm" or "No phone on Sundays" ).
        periodicity (str): Frequency of the habit ("daily" or "weekly").
        creation_date (date): Date the habit was created.
        completion_dates ( List[date]): Dates when the habit was marked as completed.
        current_streak (int): Number of consecutive successful completions.
    """

    def __init__(self, name: str, periodicity: str, creation_date: date = date.today(), id: Optional[int] = None):
       """
       Initializes a new Habit instance.

       Args:
           name (str): Name of the habit.
           periodicity (str): Frequency of the habit ("daily" or "weekly").
           creation_date (date, optional): Date of creation. Defaults to today.
           id (Optional[int], optional): Unique habit ID: Defaults to None.
        """ 
       self.id = id 
       self.name = name
       self.periodicity = periodicity
       self.creation_date = creation_date
       self.completion_dates: List[date] = []
       self.current_streak = 0
    
    def complete_today(self) -> bool:
        """
        Marks today's date as completed for the habit.
        
        Returns:
            bool: True if today was successfully marked, False if already completed.
        """
        today = date.today()
        if today not in self.completion_dates:
           self.completion_dates.append(today)
           self.update_streak()
           return True
        return False
    
    def update_streak(self):

        """ Updates the current streak based on consecutive completion dates.
            Daily habits increase by 1 per day; weekly habits increase by 1 per week.
        """
        if not self.completion_dates:
           self.current_streak = 0
           return

        dates_to_check = sorted(list(set(self.completion_dates)))  #use unique date

        gap_days = 1 if self.periodicity == "daily" else 7

        streak = 1


        for i in range(1, len(dates_to_check)):
            previous_date = dates_to_check[i -1]
            current_date_check = dates_to_check[i]
            gap = (current_date_check - previous_date).days

            if gap == gap_days:
                streak +=1
            elif gap < gap_days:

                continue
            else:
                break

        self.current_streak = streak


    def reset_habit(self):
        """
        Resets the habit streak and clears completion history.

        Returns:
            None
        """
        self.completion_dates.clear()
        self.current_streak = 0
        
    def __repr__(self) -> str: 
        """
        Returns a string representation of the Habit instance.
    
        Returns: 
             str: Formatted string showing id, name, periodicity, creation date, and current streak.
        """
    
        return (f"Habit(id={self.id}, name='{self.name}', periodicity='{self.periodicity}', "
                f"created='{self.creation_date}', streak={self.current_streak})")
    
    

   



