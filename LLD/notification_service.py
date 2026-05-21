from abc import ABC, abstractmethod

from enum import Enum

class MessageType(Enum):
    EMAIL = "email"
    TEXT_MESSAGE = "text_message"
    PUSH = "push"



class Notification:
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        self.send_email(message)
    
    def send_email(self, message: str):
        pass

class TextNotification(Notification):
    def send(self, message: str):
        self.send_text(message)

    def send_text(self, message: str):
        pass

class PushNotification(Notification):
    def send(self, message: str):
        self.send_push(message)

    def send_push(self, message: str):
        pass


class NotificationFactory:
    def __init__(self):
        self.notifcations: dict = {
            MessageType.EMAIL: EmailNotification,
            MessageType.TEXT_MESSAGE: TextNotification,
            MessageType.PUSH: PushNotification,
        }

    def get_notification(self, message_type: MessageType) -> Notification:
        if message_type in self.notifcations:
            return self.notifications[message_type]()
        return None
    
    def add_notifications(self, notification: Notification) -> bool:
        pass

            
notification_factory = NotificationFactory()

class NotificationService:
    def __init__(self, num_retries: int, notification: NotificationFactory):
        self.num_retries = num_retries 
        self.notification = notification

    def send_notification(self, notification_type: MessageType, message: str):
        if self.num_retries <= 3:
            sender = self.notification.get_notification(notification_type)
            sender.send(message)
