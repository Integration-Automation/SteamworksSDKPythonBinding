from steamworks.exceptions import *


class SteamApps(object):
    def __init__(self, steam: object):
        self.steam = steam
        if not self.steam.loaded():
            raise SteamNotLoadedException('STEAMWORKS not yet loaded')

    def is_subscribed(self) -> bool:
        """Is user subscribed to current app

        :return: bool
        """
        return self.steam.IsSubscribed()

    def is_low_violence(self) -> bool:
        """Checks if the license owned by the user provides low violence depots

        :return: bool
        """
        return self.steam.IsLowViolence()

    def is_cybercafe(self) -> bool:
        """Checks whether the current App ID is for Cyber Cafes

        :return: bool
        """
        return self.steam.IsCybercafe()

    def is_vac_banned(self) -> bool:
        """Checks if the user has a VAC ban on their account

        :return: bool
        """
        return self.steam.IsVACBanned() or False

    def get_current_game_language(self) -> str:
        """Gets the current language that the user has set

        :return: str language code
        """
        return self.steam.GetCurrentGameLanguage() or 'None'

    def get_available_game_languages(self) -> str:
        """Gets a comma separated list of the languages the current app supports

        :return: str language codes
        """
        return self.steam.GetAvailableGameLanguages() or 'None'

    def is_subscribed_app(self, app_id: int) -> bool:
        """Checks if the active user is subscribed to a specified App ID

        :param app_id: int
        :return: bool
        """
        return self.steam.IsSubscribedApp(app_id)

    def is_dlc_installed(self, dlc_id: int) -> bool:
        """Checks if the user owns a specific DLC and if the DLC is installed

        :param dlc_id: int
        :return: bool
        """
        return self.steam.IsDLCInstalled(dlc_id)

    def get_earliest_purchase_unix_time(self, app_id: int) -> int:
        """Gets the time of purchase of the specified app in Unix epoch format (time since Jan 1st, 1970)

        :param app_id: int
        :return: int timestamp
        """
        return self.steam.GetEarliestPurchaseUnixTime(app_id)

    def is_subscribed_from_free_weekend(self) -> bool:
        """Checks if the user is subscribed to the current app through a free weekend
        This function will return false for users who have a retail or other type of license.
        Suggested you contact Valve on how to package and secure your free weekend properly.

        :return: bool
        """
        return self.steam.IsSubscribedFromFreeWeekend()

    def get_dlc_count(self) -> int:
        """Get the number of DLC the user owns for a parent application/game

        :return: int
        """
        return self.steam.GetDLCCount()

    def install_dlc(self, dlc_id: int) -> None:
        """Allows you to install an optional DLC

        :param dlc_id: int
        :return: None
        """
        self.steam.InstallDLC(dlc_id)

    def uninstall_dlc(self, dlc_id: int) -> None:
        """Allows you to uninstall an optional DLC

        :param dlc_id: int
        :return: None
        """
        self.steam.UninstallDLC(dlc_id)

    def mark_content_corrupt(self, missing_files_only: bool = True) -> bool:
        """ Allows you to force verify game content on next launch

        :param missing_files_only: bool
        :return: bool
        """
        return self.steam.MarkContentCorrupt(missing_files_only)

    def get_app_install_dir(self, app_id: int) -> str:
        """Gets the install folder for a specific AppID

        :param app_id: int
        :return: str install location
        """
        return self.steam.GetAppInstallDir(app_id).decode()

    def is_app_installed(self, app_id: int) -> bool:
        """Check if given application/game is installed, not necessarily owned

        :param app_id: int
        :return: bool
        """
        return self.steam.IsAppInstalled(app_id)

    def get_app_owner(self) -> int:
        """ Gets the Steam ID of the original owner of the current app. If it's different from the current user then it is borrowed

        :return: int
        """
        return self.steam.GetAppOwner()

    def get_launch_query_param(self, key: str) -> str:
        """Gets the associated launch parameter if the game is run via sdk://run/<appid>/?param1=value1;param2=value2;param3=value3 etc

        :param key: str
        :return: str
        """
        return self.steam.GetLaunchQueryParam(key)

    def get_app_build_id(self) -> int:
        """Return the build ID for this app; will change based on backend updates

        :return: int build id
        """
        return self.steam.GetAppBuildId()

    def get_file_details(self, filename: str) -> None:
        """Asynchronously retrieves metadata details about a specific file in the depot manifest

        :param filename:
        :return: None
        """
        self.steam.GetFileDetails(filename)
