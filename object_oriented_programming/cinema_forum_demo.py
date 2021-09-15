from object_oriented_programming.cinema_forum import *

free_guy = Film('Free Guy')

heyho = User('heyho', '123')
vallywonka = User('vallywonka', '456')
ocolorra = User('ocolorra', '789')

superuser = Admin('big boss', 'password')

print(ocolorra.watch(free_guy))
print(vallywonka.watch(free_guy))
print(heyho.watch(free_guy))

print(vallywonka.comment(free_guy, 'this film is awesome'))
print(heyho.comment(free_guy, 'this film sucks'))

print(free_guy.number_of_views)
print(free_guy.number_of_comments)

print(superuser.delete_user(heyho))

print(heyho.comment(free_guy, 'hey what happened'))

print(ocolorra.comment(free_guy, 'admin please delete free guy'))

print(superuser.delete_film(free_guy))

print(vallywonka.comment(free_guy, 'hey this was my favourite film!!!'))

carol = superuser.add_fim('carol')

print(ocolorra.watch(carol))

print(ocolorra.comment(carol, 'nice.'))
