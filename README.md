
**Digital Detox Project Habit Tracker**
## A Python CLI application to track daily and weekly digital detox habits.

**Installation**
1. ### Clone the Repository
git clone (url)
cd Digital-Detox-Habit-Tracker


2. ### Create and Activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate


3. ### Install Dependencies
pip install -r requirements.txt


**Run**
### Start the CLI application
python main.py

### You will see the menu below
1. Create a habit
2. Complete a habit
3. List habits
4. Show analytics
5. Delete a habit
6. Exit
### Follow the prompt to interact with the habits


**Test**
### Run unit test with pytest

pytest
### This will test habit creation, completion, deletion, and analytics functions.


***Examples**
1. ### Creating a habit
Choose an option: 1
Enter habit name: No phone after 9PM
Enter periodicity (daily/weekly): daily
Habit 'No phone after 9PM' created successfully with ID 1.


2. ### Completing a habit
Choose an option: 2
Enter habit ID to complete: 1
Habit marked as completed.


3. ### List habit
ID: 1 / Name: No phone after 9pm / Periodicity: daily / Current Streak: 1


4. ### Viewing Analytics
Average success rate: 100%
Longest streak: No phone after 9pm with 1 days











