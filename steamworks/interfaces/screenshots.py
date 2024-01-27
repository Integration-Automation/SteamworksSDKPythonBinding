from steamworks.exceptions import *


class SteamScreenshots(object):
    def __init__(self, steam: object):
        self.steam = steam
        if not self.steam.loaded():
            raise SteamNotLoadedException('STEAMWORKS not yet loaded')

    def add_screenshot_to_library(self, filename: str, thumbnail_filename: str, width: int, height: int) -> int:
        """Adds a screenshot to the user's Steam screenshot c_library from disk

        :param filename: str
        :param thumbnail_filename: str
        :param width: int
        :param height: int
        :return: int
        """
        return self.steam.AddScreenshotToLibrary(filename, thumbnail_filename, width, height)

    def hook_screenshots(self, hook: bool) -> None:
        """Toggles whether the overlay handles screenshots

        :param hook: bool
        :return: None
        """
        self.steam.HookScreenshots(hook)

    def is_screenshots_hooked(self) -> bool:
        """Checks if the app is hooking screenshots

        :return: bool
        """
        return self.steam.IsScreenshotsHooked()

    def set_location(self, screenshot_handle: int, location: str) -> bool:
        """Sets optional metadata about a screenshot's location

        :param screenshot_handle: int
        :param location: str
        :return: bool
        """
        return self.steam.SetLocation(screenshot_handle, location)

    def trigger_screenshot(self) -> None:
        """Causes Steam overlay to take a screenshot

        :return: None
        """
        self.steam.TriggerScreenshot()
