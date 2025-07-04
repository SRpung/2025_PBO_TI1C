class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.skills = []

class Skill:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.progress_log = []

class Progress:
    def __init__(self, date, description, duration, level):
        self.date = date
        self.description = description
        self.duration = duration
        self.level = level