# Twilo client setup
#User Input
#Scheduling logic
#Sending SMS

#Install Twilio library if not already installed
from twilio.rest import Client
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os
#Twilio credentials
load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

Client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#send message function
def send_message(to, message_body):
    try:
        message = Client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',  # Twilio sandbox number
            to= f'whatsapp:{to}'

        )
        print(f"Message sent to {to}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {to}: {e}")


#User Input
name = input("Enter the recipient name: ")
recipient_number = input("Enter the recipient WhatsApp number (in format +1234567890): ")
message_body = input("Enter the message body: ")

#Parse date/time and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM): ")

#date-time parsing
schedule_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calclulate delay
if schedule_time <= current_datetime:
    print("The scheduled time is in the past. Please enter a future date and time.")
else:
    delay = (schedule_time - current_datetime).total_seconds()
    print(f"Message will be sent in {delay} seconds.")

    #Wait for the delay
    time.sleep(delay)

    #Send the message
    send_message(recipient_number, f"Hello {name}, {message_body}")




