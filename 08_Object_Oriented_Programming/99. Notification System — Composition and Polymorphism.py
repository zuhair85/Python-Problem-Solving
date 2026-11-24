# Objective: Design a notification system that can send notifications through email, SMS, and the console. Use composition to separate notification management from individual delivery methods, and polymorphism to allow different notification types to be used interchangeably.
# Requirements
# 1. Create three notification classes:
# - EmailNotification
# - SMSNotification
# - ConsoleNotification
# Each class should have a method called send(message) that handles delivering the message through its respective channel.
#
# For this exercise, simulate delivery by printing an appropriate message. You don't need actual email or SMS services.
#
# 2. Create a NotificationManager class.
# - Its constructor should accept a notification object.
# - Store that object as an instance attribute.
# - Provide a method called notify(message) that uses the stored notification object to send the message.
# 3. Demonstrate composition.
#
# The NotificationManager should contain a notification object rather than inherit from one of the notification classes.
#
# 4. Demonstrate polymorphism.
#
# Create instances of all three notification classes and use them with NotificationManager.

class EmailNotification:
    def send(self, message):
        print(f'Sending email: {message}')
        print()

class SMSNotification:
    def send(self, message):
        print(f'Sending SMS: {message}')
        print()

class ConsoleNotification:
    def send(self, message):
        print(f'Cosole Notification: {message}')
        print()

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def notify(self, message):
        self.notification.send(message)

    def set_notification(self, new_notification):
        self.notification = new_notification

msg = 'Your assignment is due tomorrow!'

notifications = [EmailNotification(), SMSNotification(), ConsoleNotification()]

for n in notifications:
    manager = NotificationManager(n)
    manager.notify(msg)

# manager = NotificationManager(EmailNotification())
#
# manager.notify("Hello!")  # Email
#
# manager.set_notification(SMSNotification())
#
# manager.notify("Hello!")  # SMS