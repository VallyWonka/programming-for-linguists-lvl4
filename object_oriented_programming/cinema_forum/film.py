class Film:
    number_of_views = 0
    number_of_comments = 0
    deleted = False

    def __init__(self, name):
        self.name = name
