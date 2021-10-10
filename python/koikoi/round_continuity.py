import enum


class RoundContinuity(enum.Enum):
    """
        試合の継続性.
    """

    END = enum.auto()
    """
        終了.

        手役ができたときに, "こいこい" を宣言しないことを意味する.
    """

    CONTINUE = enum.auto()
    """
        継続.

        手役ができたときに, "こいこい" を宣言することを意味する.
    """

