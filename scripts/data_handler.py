# Libraries
import json
import pandas as pd
from os.path import exists
from csv import DictReader
import re

# External Scripts
global_variables = json.load(open('data\global_variables.json'))

def Build_Sheet_URL(doc_id, sheet_id):
    # Construct a Google Sheet URL so Pandas can Access Data
    return f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid={sheet_id}'

def Write_Dataframe_To_File(df, file_path):
    # Turn Dataframe to a CSV file
    df.to_csv(file_path)

def Download_Student_Data():
    # Pulled From The Google Sheet URL
    doc_id = '1yI5kt3E-nkFA2-juvulEkFuWxpQ-BuFHURGqTunkc-E'
    sheet_id = '1090354940'

    # Construct URL
    sheet_url = Build_Sheet_URL(doc_id, sheet_id)
    
    # Use Pandas to read the sheet
    dataframe = pd.read_csv(sheet_url)
    export_path = 'data\data.csv' # Export Location

    # Export Data
    Write_Dataframe_To_File(dataframe, export_path)

def Export_Student_Data_In_JSON():
    # Read Student Data
    with open('data\data.csv', 'r') as read_obj:
        data = DictReader(read_obj)
        
        # Loop through each row and create JSON file for student
        for row in data:
            Create_JSON_File_For_Student(row["Student's First Name"], row["Student's Last Name"], row["Student's Phone Number"])

def Increase_Number_Of_Students():
    # Increase Variable
    global_variables['number_of_students'] += 1
    
    # Create JSON Object With Modified Values
    global_variables_json = json.dumps(global_variables)

    # Modify The File
    with open('data\global_variables.json', 'w') as outfile:
        outfile.write(global_variables_json)

def Format_Phone_Number(phone_number):
    # Examples
    # +1 613 822 9592   ->   +16138229592
    # +1 (613) 822 9592 ->   +16138229592
    # (+1) 6138229592   ->   +16138229592
    # +1-613-822-9592   ->   +16138229592

    # Remove Uncessessary Spaces
    formatted_number = re.sub(r"\s+", "", phone_number, flags=re.UNICODE)

    # Add a + at Beginning
    first_character = formatted_number[0]

    if(first_character != '+'):
        formatted_number = '+' + formatted_number

    # Return Phone Number
    return formatted_number

def Create_JSON_File_For_Student(first_name, last_name, phone_number):
    # Initialize Path
    path = f'data/students/{first_name}_{last_name}.json'

    # Create a Dictionary With All Information
    student_dict = {
        "ID": global_variables['number_of_students'],
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": Format_Phone_Number(phone_number),
        "region_code": "+41",
        "module": 1,
        "progress": 0
    }

    # Turn the Dictionary Into a JSON Object
    student_json = json.dumps(student_dict)

    # Check If Student Data Is Already Recorded
    file_exists = exists(path) # Returns True if file is found, False if not

    if (file_exists):   
        # Debug     
        print(f"✅ {first_name} {last_name} Already Has a File")
    else:
        # Write JSON File in students folder, name the file after the student
        with open(f'data/students/{first_name}_{last_name}.json', 'w') as outfile:
            outfile.write(student_json)
        
        # Log Student Into Global Variables
        Increase_Number_Of_Students()

        # Debug
        print(f"📰 Create File For {first_name} {last_name}")