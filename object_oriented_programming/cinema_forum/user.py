class User:
    deleted = False

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def watch(self, film):
        if not self.deleted and not film.deleted:
            film.number_of_views += 1
            return f'{self.username} is watching {film.name}.'
        elif film.deleted:
            return f'Film {film.name} was deleted!'
        return f'{self.username} was deleted!'

    def comment(self, film, comment):
        if not self.deleted:
            film.number_of_comments += 1
            return f'Here is what {self.username} thinks about {film.name}: {comment}'
        elif film.deleted:
            return f'Film {film.name} was deleted!'
        return f'{self.username} was deleted!'
