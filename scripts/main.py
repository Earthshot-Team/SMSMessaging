# Libraries
from twilio.rest import Client

# Other Scripts
import keys.twilio_keys
from components import Student
import data_handler

client = Client(keys.twilio_keys.account_sid, keys.twilio_keys.auth_token) # Twilio Client
students = [Student('Nicolas', 'Gatien', '+13439985454')] # Student List

data_handler.Download_Student_Data()
data_handler.Export_Student_Data_In_JSON()

# Loop Through Each Student In List
'''for student in students:

    # Construct Message
    message = client.messages.create(
        body = f"Welcome, {student.first_name}! This is your first lesson with 🧱 Foundations \n 🔗 Press This Link To Continue To Your First Lesson: https://www.youtube.com/watch?v=iik25wqIuFo",
        from_ = keys.twilio_keys.twilio_number,
        to = student.phone_number
    )

    # Debug Message
    print(f"Sent: {message.body} to {student.phone_number}")'''