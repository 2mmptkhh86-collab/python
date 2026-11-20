
class Television:
    """A class that controls a television."""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Set the starting values for the television."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__previous_volume = Television.MIN_VOLUME

    def power(self) -> None:
        """Turn the television on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the television when it is on."""
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume
                self.__muted = False
            else:
                self.__previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True

    def channel_up(self) -> None:
        """Increase the channel and return to zero after the maximum."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the channel and wrap to the maximum from zero."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Unmute if needed and increase the volume up to the maximum."""
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Unmute if needed and decrease the volume to the minimum."""
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the television's power, channel, and volume."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
