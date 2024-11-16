import os
import sys
import math
import random
import datetime
import json

# os module
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# sys module
print(f"Python Version: {sys.version}")

# math module
circle_radius = 5
circle_area = math.pi * math.pow(circle_radius, 2)
print(f"Area of Circle: {circle_area:.2f}")

# random module
random_number = random.randint(1, 100)
print(f"Random Number between 1 and 100: {random_number}")

# datetime module
current_time = datetime.datetime.now()
print(f"Current Date and Time: {current_time}")

# json module
data = {"name": "Srinivas", "role": "Data Analyst", "skills": ["Python", "SQL", "ML"]}
json_data = json.dumps(data, indent=4)
print("JSON Data:")
print(json_data)
