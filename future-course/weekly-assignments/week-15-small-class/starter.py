class CourseTask:
    def __init__(self, title, points, due_week):
        self.title = title
        self.points = points
        self.due_week = due_week

    def summary(self):
        return self.title + ' is worth ' + str(self.points) + ' points'


def main():
    task = CourseTask('Project', 25, 15)
    print(task.summary())


if __name__ == '__main__':
    main()
