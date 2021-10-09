from .player import Player
import dataclasses


@dataclasses.dataclass(frozen=True)
class Players(object):
    """
        親と子.
    """

    parent: Player
    """親"""

    child: Player
    """子"""

