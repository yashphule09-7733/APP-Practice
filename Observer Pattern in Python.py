class Observer:
    def update(self, message):
        print(f"Notification: {message}")


class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


# Create subject
youtube_channel = Subject()

# Create observers
user1 = Observer()
user2 = Observer()

# Subscribe users
youtube_channel.subscribe(user1)
youtube_channel.subscribe(user2)

# Notify all observers
youtube_channel.notify("New Python video uploaded!")