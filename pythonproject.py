# Python Study Tracker for General Studies
import math

# First, I'll be adding my functions to my project
# Each function is specific and unique to the task attached to it
# I've also added a list for the specific class subject the student will be adding to the tracker

class_subject = ["Math", "History", "Science", "English",]
def choose_class_subject():
    class_subject = str(input("Which subject are you going to be studying?"))
    if class_subject == "Math":
        print(f"")


    
def get_study_hours_goal():

    daily_study_hours = float(input("Enter how many hours you've studied today: "))
    if daily_study_hours == 0:
        print(f"You haven't studied at all! Either you're a genius, or you're going to flunk out of college. You decide.")
    elif daily_study_hours >= 1:
        print(f"You've studied for {daily_study_hours} hours today. That's {daily_study_hours * 7} study hours per week.")
    else:
        print(f"Invalid response. Please resond with a number from 1-4.")

    weekly_study_hours = float(input("Enter how many hours you've studied this week: "))
    if weekly_study_hours == 0:
        print(f"You haven't studied at all! Either you're a genius, or you're going to flunk out of college. You decide.")
    elif weekly_study_hours >= 1:
        print(f"You've studied for {weekly_study_hours} hours this week. That's {weekly_study_hours * 4} study hours per month.")
    else:
        print(f"Invalid response. Please resond with a number from 1-28.")
    
    monthly_study_hours = float(input("Enter how many hours you've studied this month: "))
    if monthly_study_hours == 0:
        print(f"You haven't studied at all! Either you're a genius, or you're going to flunk out of college. You decide.")
    elif monthly_study_hours >= 1:
        print(f"You've studied for {monthly_study_hours} hours this month. That's {monthly_study_hours * 3} per semester.")
    else:
        print(f"Invalid response. Please resond with a number from 1-112.")
get_study_hours_goal()

# Next, I'll be adding a list to my project
# Each study session will be stored as a dictionary inside a list

study_sessions = []

