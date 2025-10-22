import sqlite3
from habit import Habit
from datetime import date
from typing import List, Optional

class DatabaseConnector:
    """
    Handles SQLite3 database operations for storing and retrieving habits.
    """

    def __init__(self, db_path: str = "habits.db"):
        """ 
        Initializes the database connection and ensures the habits table exists.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """
        Creates the habits table if it doesn't already exist.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                periodicity TEXT NOT NULL,
                creation_date TEXT NOT NULL,
                completion_dates TEXT,
                current_streak INTEGER
            )
        """)
        self.conn.commit()

    def save_habit(self, habit: Habit):
        """
        Saves a habit to the database.

        Args:
            habit (Habit): The habit to save.
        """

        cursor = self.conn.cursor()
        dates_str = ",".join([d.isoformat() for d in habit.completion_dates])

        if habit.id is None:
           cursor.execute("""
            INSERT INTO habits (name, periodicity, creation_date, completion_dates, current_streak)
            VALUES (?, ?, ?, ?, ?)
        """,(habit.name, habit.periodicity, habit.creation_date.isoformat(), dates_str, habit.current_streak)) 
           habit.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE habits 
                SET name=?, periodicity=?, creation_date=?, completion_dates=?, current_streak=?
                WHERE id=?
        """,(habit.name, habit.periodicity, habit.creation_date.isoformat(), dates_str, habit.current_streak, habit.id))

        self.conn.commit()
                            
    
    def load_habits(self) -> List[Habit]:
        """
        Loads all habits from the database.

        Returns:
            List[Habit]: List of Habit instances.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, periodicity,  creation_date, completion_dates, current_streak FROM habits")
        rows = cursor.fetchall()
        habits = []
        for row in rows:
          id, name, periodicity, creation_date, dates_str, streak = row
          dates = [date.fromisoformat(d) for d in dates_str.split(",") if d]
          habit = Habit(id=id, name=name, periodicity=periodicity, creation_date=date.fromisoformat(creation_date))
          habit.completion_dates = dates
          habit.current_streak = streak
          habits.append(habit)
        return habits

    
    def get_all_habits(self) -> List[Habit]:
        """
        Returns all habits from the database (alias for the load_habits).
        """
        return self.load_habits()

    def get_habit_by_id(self, habit_id: int) -> Optional[Habit]:
        """
        Find one habit using its ID:
        habit_id (int): The number linked to the habit.

        Returns:
        The habit if it exists, otherwise None.
        
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, name , periodicity, creation_date, completion_dates, current_streak FROM habits Where id=?",
            (habit_id,)
        )
        row = cursor.fetchone()
        if row is None:
            return None
        id, name, periodicity, creation_date, dates_str, streak = row
        completion_dates = [date.fromisoformat(d) for d in dates_str.split(",") if d]
    
        habit = Habit(id=id, name=name, periodicity=periodicity, creation_date=date.fromisoformat(creation_date))
        habit.completion_dates = completion_dates
        habit.current_streak = streak
        return habit
    

    def delete_habit(self, habit_id: int) -> bool:
        """
        Deletes a habit from the database by its ID.
 
        Args:
            habit_id (int): The unique identifier of the habit to delete.

        Returns:
            bool: True if the habit was deleted successfully, False if no such habit exists.
        """
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        self.conn.commit()

        if cursor.rowcount > 0:
            return True # Habit deleted successsfully
        else:
            return False #  Habit not found
        



         
        

        


      


