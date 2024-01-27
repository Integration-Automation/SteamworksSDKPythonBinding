from steamworks.enums import *
from steamworks.exceptions import *


class SteamFriends(object):
    def __init__(self, steam: object):
        self.steam = steam
        if not self.steam.loaded():
            raise SteamNotLoadedException('STEAMWORKS not yet loaded')

    def get_friend_count(self, flag: bytes = FriendFlags.ALL) -> int:
        """ Get number of friends user has

        :param flag: FriendFlags
        :return: int
        """
        return self.steam.GetFriendCount(flag.value)

    #
    def get_friend_by_index(self, friend_index: int, flag: bytes = FriendFlags.ALL) -> int:
        """Get a friend by index

        :param friend_index: int position
        :param flag: FriendFlags
        :return: int steam64
        """
        return self.steam.GetFriendByIndex(friend_index, flag.value)

    def get_player_name(self) -> str:
        """Get the user's Steam username

        :return: str
        """
        return self.steam.GetPersonaName()

    def get_player_state(self) -> int:
        """Get the user's state on Steam

        :return: int
        """
        return self.steam.GetPersonaState()

    def get_friend_persona_name(self, steam_id: int) -> str:
        """ Get given friend's Steam username

        :param steam_id: int
        :return: str
        """
        return self.steam.GetFriendPersonaName(steam_id)

    def set_game_info(self, server_key, server_value) -> None:
        """Set the game information in Steam; used in 'View Game Info'
        # Steamworks documentation is missing this method, still relevant?
        :param serverKey: str
        :param serverValue: str
        :return: None
        """
        self.steam.SetGameInfo(server_key, server_value)

    def clear_game_info(self) -> None:
        """Clear the game information in Steam; used in 'View Game Info'
        # Steamworks documentation is missing this method, still relevant?
        :return: None
        """
        self.steam.ClearGameInfo()

    def invite_friend(self, steam_id: int, connection: str) -> None:
        """Invite friend to current game/lobby
        # Steamworks documentation is missing this function but "InviteUserToGame" is present, does this need an update?
        :param steam_id: int steam64
        :param connection: str connection string
        :return:
        """
        self.steam.InviteFriend(steam_id, connection)

    def set_played_with(self, steam_id: int) -> None:
        """Set player as 'Played With' for game

        :param steam_id: int steam64
        :return: None
        """
        self.steam.SetPlayedWith(steam_id)

    def activate_game_overlay(self, dialog: str = '') -> None:
        """Activates the overlay with optional dialog

        :param dialog: str ["Friends", "Community", "Players", "Settings", "OfficialGameGroup", "Stats", "Achievements", "LobbyInvite"]
        :return: None
        """
        self.steam.ActivateGameOverlay(dialog.encode())

    def activate_game_overlay_to_user(self, dialog: str, steam_id: int) -> None:
        """Activates the overlay to the specified dialog

        :param dialog: str ["steamid", "chat", "jointrade", "stats", "achievements", "friendadd", "friendremove", "friendrequestaccept", "friendrequestignore"]
        :param steam_id: int steam64
        :return: None
        """
        self.steam.ActivateGameOverlayToWebPage(dialog.encode(), steam_id)

    def activate_game_overlay_to_web_page(self, url: str) -> None:
        """Activates the overlay with specified web address

        :param url: str
        :return: None
        """
        self.steam.ActivateGameOverlayToWebPage(url.encode())

    def activate_game_overlay_to_store(self, app_id: int) -> None:
        """Activates the overlay with the application/game Steam store page

        :param app_id: int
        :return: None
        """
        self.steam.ActivateGameOverlayToWebPage(app_id)

    def activate_game_overlay_invite_dialog(self, steam_lobby_id: int) -> None:
        """Activates game overlay to open the invite dialog. Invitations will be sent for the provided lobby

        :param steam_lobby_id:
        :return: None
        """
        self.steam.ActivateGameOverlayInviteDialog(steam_lobby_id)
