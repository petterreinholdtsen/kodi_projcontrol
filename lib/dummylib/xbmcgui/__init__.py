#
NOTIFICATION_ERROR = 0
NOTIFICATION_INFO = 1

class Dialog():
    def notification(self, title, message, type, time, sound):
        print(title)
        print(message)
