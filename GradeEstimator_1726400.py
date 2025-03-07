
# Prompt the user to enter their first name and storing the input in a variable.
first_name = input("Enter your first name: ") 
# Prompt the user to enter their last name and storing the input in a another different variable.
last_name = input("Enter your last name: ")
# Display's the complete name by joining the first name and last name together. 
print(first_name,last_name)

##unit 8 Assignemnt


#Importing pandas and json libraries
import pandas as pd
import json

# open and load tasks.json file
with open("tasks.json", "r") as file:
    tasks_data = json.load(file)

# Extract homework_types from json
homework_types = tasks_data["homework_types"]

def calculate_grades(grades_file, homework_types):
    
    # Load grades file from CSV file
    grades_df = pd.read_csv(grades_file)
    
    # Replace NaN values with 0 
    grades_df_filled = grades_df.fillna(0)
    
    # Calculating total earned points by sum, all values except first column
    total_earned = grades_df_filled.iloc[:, 1:].sum().sum()
    
    # Compute maximum possible points based on json file homework_type
    max_points = sum(
        hw["number_of_tasks_per_semester"] * hw["maximum_points_per_submission"]
        for hw in homework_types
    )
    
    # Calculate the percentage
    percentage = (total_earned / max_points) * 100
    
    # assigning the letter to the grades
    if percentage > 90:
        letter_grade = "A"
    elif percentage > 80:
        letter_grade = "B"
    elif percentage > 70:
        letter_grade = "C"
    elif percentage > 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    return total_earned, max_points, percentage, letter_grade

#Calculating Grades_0.csv file
earned_0, max_points, percentage_0, letter_0 = calculate_grades("Grades_0.csv", homework_types)
print(f"\nsubmitting Unit 8 assignments with 0:")
print(f"You have {earned_0} out of {max_points}")
print(f"Your percentage is {percentage_0:.1f}%")
print(f"Your letter grade is: {letter_0}")

# calculating Grades_50.csv file
earned_50, _, percentage_50, letter_50 = calculate_grades("Grades_50.csv", homework_types)
print(f"\nAfter submitting Unit 8 assignments:")
print(f"You have {earned_50} out of {max_points}")
print(f"Your percentage is {percentage_50:.1f}%")
print(f"Your letter grade is: {letter_50}")
