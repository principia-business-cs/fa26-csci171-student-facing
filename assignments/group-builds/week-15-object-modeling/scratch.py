class Task:
    def __init__(self, title):
        self.title = title

    def summary(self):
        return self.title

print(Task('Practice').summary())
