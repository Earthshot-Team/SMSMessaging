from twilio.rest import Client
import keys
from student import Student

client = Client(keys.account_sid, keys.auth_token) # Twilio Client
students = [Student('Nicolas', '+13439985454'), Student('Mom', '+16134004208')] # Student List

# Loop Through Each Student In List
for student_index in range(len(students)):
    student = students[student_index]

    # Construct Message
    message = client.messages.create(
        body = f"Welcome, {student.first_name}! This is your first lesson with 🧱 Foundations \n 🔗 Press This Link To Continue To Your First Lesson: https://www.youtube.com/watch?v=iik25wqIuFo",
        from_ = keys.twilio_number,
        to = student.phone_number
    )

    # Debug Message
    print(f"Sent: {message.body} to {student.phone_number}")