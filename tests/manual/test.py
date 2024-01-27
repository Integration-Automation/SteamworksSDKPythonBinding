import os
os.add_dll_directory(os.getcwd())

from steamworks import STEAMWORKS

steamworks = STEAMWORKS()
steamworks.initialize()

my_steam64 = steamworks.Users.get_steam_id()
my_steam_level = steamworks.Users.get_player_steam_level()

print(f'Logged on as {my_steam64}, level: {my_steam_level}')
print('Is subscribed to current app?', steamworks.Apps.is_subscribed())
