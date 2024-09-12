from twilio.rest import Client

TWILIO_SID = "AC6e554281b2d2814bd12f585860df3a79"
TWILIO_AUTH_TOKEN = "6d1ed50f944f4d2810250c246ca7fe7d"
TWILIO_VIRTUAL_NUMBER = '+12565791915'
TWILIO_VERIFIED_NUMBER = '+919359323128'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
