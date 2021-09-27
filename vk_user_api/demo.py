import vk_api

from collections import Counter
from vk_user_api import TOKEN, LOGIN, PASSWORD


vk_session = vk_api.VkApi(LOGIN, PASSWORD, token=TOKEN)
vk_session.auth()
vk = vk_session.get_api()

print("Задание 1. Соотношение полов среди учатников группы")
group_members = vk.groups.getMembers(group_id="dark.faculty")
user_info = vk.users.get(user_ids=group_members["items"], fields=["sex"])
user_sexes = Counter([user["sex"] for user in user_info])
print(f"В сообществе {round(user_sexes[1] / group_members['count'] * 100, 2)}% женщин \
и {round(user_sexes[2] / group_members['count'] * 100, 2)}% мужчин.")

print()

print("Задание 2. Пользователи, лайкнувшие фото")
photo_info = vk.likes.getList(type="photo",
                              item_id=456244789)
user_info = vk.users.get(user_ids=photo_info["items"])
for user in user_info:
    print(f"{user['first_name']} {user['last_name']}")

print()

print("Задание 3. Информация о подарках пользователя")
gifts_info = vk.gifts.get()
print(f"Всего подарков: {gifts_info['count']}")
print("Топ-5 фанатов:")
gift_givers = Counter([gift["from_id"] for gift in gifts_info["items"]]).most_common(5)
for gift_giver, gift_count in gift_givers:
    user = vk.users.get(user_ids=[gift_giver])
    print(f"{user[0]['first_name']} {user[0]['last_name']}: {gift_count}")
