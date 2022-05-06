# Libraries
from twilio.rest import Client
import os
import json

# Other Scripts
import keys.twilio_keys
import data_handler

client = Client(keys.twilio_keys.account_sid, keys.twilio_keys.auth_token) # Twilio Client
students = 'data\students' # Students Directory

# Store Student Data Locally
data_handler.Download_Student_Data()
data_handler.Export_Student_Data_In_JSON()

def File_Is_JSON(file_path):
    # Get last 5 character
    last_5_characters = file_path[-5:]

    if (last_5_characters == ".json"):
        return True
    else:
        return False

# Loop Through Each Student In Student Directory
for file in os.scandir(students):
    # Make sure the file still exists
    if file.is_file():

        if File_Is_JSON(file.path):
            student = json.load(open(file.path)) # Reference the actual file instead of the file name

            # Construct Message
            message = client.messages.create(
                body = f"Welcome, {student['first_name']}! This is your first lesson with 🧱 Foundations \n 🔗 Press This Link To Continue To Your First Lesson: https://youtu.be/h4FjjPneNw8",
                from_ = keys.twilio_keys.twilio_number,
                to = student['phone_number']
            )

            # Debug Message
            print(f"Sent: {message.body} to {student['phone_number']}")