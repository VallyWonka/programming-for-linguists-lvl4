from object_oriented_programming.cinema_forum import Film, User


class Admin(User):
    def delete_user(self, user):
        user.deleted = True
        return f'User {user.username} was deleted by {self.username}'

    def add_fim(self, film_name):
        print(f'Film {film_name} was added by {self.username}')
        return Film(film_name)

    def delete_film(self, film):
        film.deleted = True
        return f'Film {film.name} was deleted by {self.username}'
