from steamworks.exceptions import *


class SteamMusic(object):
    def __init__(self, steam: object):
        self.steam = steam
        if not self.steam.loaded():
            raise SteamNotLoadedException('STEAMWORKS not yet loaded')

    def music_is_enabled(self) -> bool:
        """Is Steam music enabled

        :return: bool
        """
        return self.steam.MusicIsEnabled()

    def music_is_playing(self) -> bool:
        """Is Steam music playing something

        :return: bool
        """
        return self.steam.MusicIsPlaying()

    def music_get_volume(self) -> float:
        """Get the volume level of the music.

        :return: float
        """
        return self.steam.MusicGetVolume()

    def music_pause(self) -> None:
        """Pause whatever Steam music is playing

        :return: None
        """
        self.steam.MusicPause()

    def music_play(self) -> None:
        """Play current track/album.

        :return: None
        """
        self.steam.MusicPlay()

    def music_play_next(self) -> None:
        """Play next track/album.

        :return: None
        """
        self.steam.MusicPlayNext()

    def music_play_prev(self) -> None:
        """Play previous track/album.

        :return: None
        """
        self.steam.MusicPlayPrev()

    def music_set_volume(self, volume: float) -> None:
        """Set the volume of Steam music

        :param volume: float 0,0 -> 1,0
        :return: None
        """
        self.steam.MusicSetVolume(volume)
