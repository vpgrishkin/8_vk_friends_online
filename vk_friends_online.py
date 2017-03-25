import vk
from getpass import getpass

APP_ID = 5940900


def get_user_login():
    return input('Enter your vk login:')


def get_user_password():
    return getpass('Enter your password:')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    online_friend_ids = api.friends.getOnline()
    return api.users.get(user_ids=online_friend_ids)


def output_friends_to_console(friends_online):
    if len(friends_online) == 0:
        print('No friends are online')
    else:
        print('Friends online:')
        for friend in friends_online:
            print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
