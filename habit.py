from datetime import date
from typing import List 

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

    def __init__(self, id: int, name: str, periodicity: str, creation_date: date = date.today()):
       """
       Initializes a new Habit instance.

       Args:
           id (int): Unique habit ID.
           name (str): Name of the habit.
           periodicity (str): Frequency of the habit.
           creation_date (date, optional): Date of creation. Defaults to today.
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
            bool: True if today was succesfully marked, False if already completed.
        """
        today = date.today()
        if today not in self.completion_dates:
           self.completion_dates.append(today)
           self.update_streak()
           return True
        return False
    
    def update_streak(self):

        """
        Updates the current streak based on consecutive completion dates.
        """
        sorted_dates = sorted(self.completion_dates, reverse=True)
        streak = 0
        today = date.today()

        for i, d in enumerate(sorted_dates):
           if (today - d) .days == i:
                streak += 1
           else:
               break
           
        self.current_streak = streak

    def reset_habit(self):
        """
        Resets the habit streak and clears completion history.
        """
        self.completion_dates.clear()
        self.current_streak = 0
        
    def __repr__(self) -> str:
        """
        Returns a string representation of the Habit instance.
    
        Returns: 
             str: Formatted string with habit details.
        """
    
        return (f"Habit(id={self.id}, name='{self.name}', periodicity='{self.periodicity}', "
                f"created='{self.creation_date}', streak={self.current_streak})")
    
    

   



