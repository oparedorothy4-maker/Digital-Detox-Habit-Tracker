from typing import List
from habit import Habit
from db import DatabaseConnector
import datetime

class HabitManager:
    """
    Manages habit creation, completion, and retrieval logic.
    Interfaces with the database connector to persist habit data.
    """

    def __init__(self, db_connector: DatabaseConnector):
        self.db: DatabaseConnector = db_connector
        """
        Initializes the HabitManager with a database connector.

        Args:
            db_connector (DatabaseConnector): An instance for database operations.
        """    
        self.db = db_connector

    def create_habit(self, name: str, periodicity: str) -> Habit:
        """
        Creates a new habit and stores it in the database.

        Args:
            name (str): The name of the habit.
            periodicity (str) The frequency of the habit ('daily' or 'weekly').

        Returns:
            Habit: The newly created Habit object.
        """
        new_habit = Habit(name=name, periodicity=periodicity, creation_date=datetime.date.today())
        self.db.save_habit(new_habit)
        return new_habit
    
    def complete_habit(self, habit_id: int) -> bool:
        """
        Marks a habit as completed for the current date.

        Args:
            habit_id (int): The unique identifier of the habit.

            Returns:
                bool: True if completion was successful, False otherwise.
        """
        habit = self.db.get_habit_by_id(habit_id)
        if habit:
            habit.complete_today()
            self.db.save_habit(habit)
            return True
        return False
    def list_by_periodicity(self, periodicity: str) -> List[Habit]:
        """
        Retrieves all habits filtered by periodicity.

        Args:
            periodicity (str): The frequency to filter by ('daily' or 'weekly').

        Returns:
            List[Habit]: A list of matching Habit objects.
        """
        all_habits = self.db.get_all_habits()
        return [habit for habit in all_habits if habit.periodicity == periodicity]
    
    def list_current_streaks(self) -> List[str]:  
        """
        Lists the current steaks for all habits.
        
        Returns:
            List[str]: A formatted list of habit names and their current streaks.
        """
        all_habits = self.db.get_all_habits()
        return [f"{habit.name}: {habit.current_streak} days" for habit in all_habits] 



   

       


  
      
        
