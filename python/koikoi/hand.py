

class Hand(object):
    """
        役.
    """

    def __init__(
            self,
            name: str,
            pronounce: str,
            point: int
            ) -> None:
        """
            インスタンスを初期化する.

            Arguments
            ---------
            name: str
                役名.
            pronounce: str
                読み方.
            point: int
                点数.
        """
        self._name = name
        self._pronounce = pronounce
        self._point = point

    def __eq__(self, other) -> bool:
        return self.to_tuple() == other.to_tuple()

    def __repr__(self) -> str:
        return "{:s}({:s}, {:s}, {:s})".format(
            self.__class__.__name__,
            repr(self._name),
            repr(self._pronounce),
            repr(self._point),
        )

    def to_tuple(self) -> tuple[str, str, int]:
        return (self._name, self._pronounce, self._point)

    @property
    def name(self) -> str:
        return self._name

    @property
    def pronounce(self) -> str:
        return self._pronounce

    @property
    def point(self) -> int:
        return self._point

