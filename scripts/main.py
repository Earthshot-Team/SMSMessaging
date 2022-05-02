from twilio.rest import Client
import keys
import student

client = Client(keys.account_sid, keys.auth_token)
numbers = [student.Student('Nicolas', '+13439985454'), student.Student('Mom', '+16134004208')]

for number in range(len(numbers)):
    message = client.messages.create(
        body = f"Welcome, {numbers[number].name}! This is your first lesson with 🧱 Foundations \n 🔗 Press This Link To Continue To Your First Lesson: https://www.youtube.com/watch?v=iik25wqIuFo",
        from_ = keys.twilio_number,
        to = numbers[number].phone_number
    )

    print(message.body)