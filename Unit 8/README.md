Grade Estimator Script (gradeestimator_1726400.py) – Unit 8

The gradeestimator_1726400.py script is designed to calculate students' grades based on their scores recorded in CSV files. It reads grading criteria from a JSON file, processes student scores, and computes key grading metrics, including:
Total earned points
Maximum possible points
Grade percentage
Corresponding letter grades

Prerequisites
Install Required Dependencies
The script requires the pandas library. Ensure it is installed before running the script: pip install pandas

Prepare Input Files
Create and store the following CSV files in the same directory as the script:
grades_0.csv
grades_50.csv
Ensure the JSON file containing grading criteria is also available in the same folder.

Output
Upon execution, the script processes the input files and outputs the following:
Computed grades including total, maximum, percentage, and letter grades.
The results are displayed in the terminal and saved in the same directory.
