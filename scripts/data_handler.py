# Libraries
import json
from os.path import exists

# External Scripts
from components import Student


student = Student('Nicolas', 'Gatien', '+13439985454')
path = f'students/{student.first_name}_{student.last_name}.json'

global_variables = json.load(open('scripts\global_variables.json'))

def Increase_Number_Of_Students():
    global_variables['number_of_students'] += 1
    
    global_variables_json = json.dumps(global_variables)

    with open('scripts\global_variables.json', 'w') as outfile:
        outfile.write(global_variables_json)

def Create_JSON_File_For_Student():
    # Create a Dictionary With All Information
    student_dict = {
        "ID": global_variables['number_of_students'],
        "first_name": student.first_name,
        "last_name": student.last_name,
        "phone_number": student.phone_number,
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
        print(f"✅ {student.first_name} {student.last_name} Already Has a File")
    else:
        # Write JSON File in students folder, name the file after the student
        with open(f'students/{student.first_name}_{student.last_name}.json', 'w') as outfile:
            outfile.write(student_json)
        
        # Log Student Into Global Variables
        Increase_Number_Of_Students()

        # Debug
        print(f"📰 Create File For {student.first_name} {student.last_name}")


Create_JSON_File_For_Student()

# Up Module By 1
file = open(path)
python_dictionary = json.load(file)

python_dictionary['module'] += 1

student_json2 = json.dumps(python_dictionary)

print(python_dictionary['module'])

with open(path, 'w') as outfile:
    outfile.write(student_json2)