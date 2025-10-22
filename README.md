
## Digital Detox Project Habit Tracker

### GitHub Repository:


[Digital-Detox-Habit-Tracker](https://github.com/oparedorothy4-maker/Digital-Detox-Habit-Tracker)



### Description
A Python CLI application to track daily and weekly digital detox habits.
It allows creating, completing, listing, deleting habits, and viewing analytics.





## Installation

### Clone the Repository
```bash

git clone https://github.com/oparedorothy4-maker/Digital-Detox-Habit-Tracker
cd Digital-Detox-Habit-Tracker
```


### Create and Activate a virtual environment
   
```bash

python -m venv venv
# On Windows:
.\venv\Scripts\Activate
# On Linux/Mac:
source venv/bin/activate
```



## Install Dependencies
   
```bash

pip install -r requirements.txt
```



## Run
### Start the CLI application

```bash

python main.py
```


### You will see the menu below:

```
1. Create a habit
2. Complete a habit
3. List habits
4. Show analytics
5. Delete a habit
6. Exit
```

### Follow the prompt to interact with the habits




## Test
### Run unit test with pytest

```bash

pytest
```

### This will test habit creation, completion, deletion, and analytics functions.




## Examples

### Creating a habit

```
Choose an option: 1
Enter habit name: No phone after 9PM
Enter periodicity (daily/weekly): daily
Habit 'No phone after 9PM' created successfully with ID 1.
```


### Completing a habit
   
```
Choose an option: 2
Enter habit ID to complete: 1
Habit marked as completed.
```


### List habit

```
ID: 1 / Name: No phone after 9pm / Periodicity: daily / Current Streak: 1
```

### Viewing Analytics

```
Average success rate: 100%
Longest streak: No phone after 9pm with 1 days
```










