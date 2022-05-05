# Libraries
from twilio.rest import Client
import os
import json

# Other Scripts
import keys.twilio_keys
from components import Student
import data_handler

client = Client(keys.twilio_keys.account_sid, keys.twilio_keys.auth_token) # Twilio Client
students = 'data\students' # Students Directory

# Store Student Data Locally
data_handler.Download_Student_Data()
data_handler.Export_Student_Data_In_JSON()

# Loop Through Each Student In Student Directory
for filename in os.scandir(students):
    # Make sure the file still exists
    if filename.is_file():
        file = json.load(open(filename.path)) # Reference the actual file instead of the file name

        # Construct Message
        message = client.messages.create(
            body = f"Welcome, {file['first_name']}! This is your first lesson with 🧱 Foundations \n 🔗 Press This Link To Continue To Your First Lesson: https://www.youtube.com/watch?v=iik25wqIuFo",
            from_ = keys.twilio_keys.twilio_number,
            to = file['phone_number']
        )

        # Debug Message
        print(f"Sent: {message.body} to {file['phone_number']}")