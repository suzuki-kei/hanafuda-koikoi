"""
    花札の "こいこい" に関する機能を提供する.
"""


import functools
import operator
import typing


class Card(object):
    """
        札.
    """

    @classmethod
    def list(
            self,
            *,
            month: typing.Optional[int] = None,
            point: typing.Optional[int] = None
            ) -> list["Card"]:
        """
        """
        is_match = lambda card: \
            (month is None or card.month == month) and \
            (point is None or card.point == point)
        return list(filter(is_match, self.cards))

    @classmethod
    def init(self) -> None:
        self.cards = (
            Card( 1, 20, "松に鶴",       "まつ に つる"),
            Card( 1,  5, "松に赤短",     "まつ に あかたん"),
            Card( 1,  1, "松のカス",     "まつ の かす"),
            Card( 1,  1, "松のカス",     "まつ の かす"),
            Card( 2, 10, "梅に鶯",       "うめ に うぐいす"),
            Card( 2,  5, "梅に赤短",     "うめ に あかたん"),
            Card( 2,  1, "梅のカス",     "うめ の かす"),
            Card( 2,  1, "梅のカス",     "うめ の かす"),
            Card( 3, 20, "桜に幕",       "さくら に まく"),
            Card( 3,  5, "桜に赤短",     "さくら に あかたん"),
            Card( 3,  1, "桜のカス",     "さくら の かす"),
            Card( 3,  1, "桜のカス",     "さくら の かす"),
            Card( 4, 10, "藤に時鳥",     "ふじ に ほととぎす"),
            Card( 4,  5, "藤に短冊",     "ふじ に たんざく"),
            Card( 4,  1, "藤のカス",     "ふじ の かす"),
            Card( 4,  1, "藤のカス",     "ふじ の かす"),
            Card( 5, 10, "菖蒲に八ツ橋", "あやめ に やつはし"),
            Card( 5,  5, "菖蒲に短冊",   "あやめ に たんざく"),
            Card( 5,  1, "菖蒲のカス",   "あやめ の かす"),
            Card( 5,  1, "菖蒲のカス",   "あやめ の かす"),
            Card( 6, 10, "牡丹に蝶",     "ぼたん に ちょう"),
            Card( 6,  5, "牡丹に青短",   "ぼたん に あおたん"),
            Card( 6,  1, "牡丹のカス",   "ぼたん の かす"),
            Card( 6,  1, "牡丹のカス",   "ぼたん の かす"),
            Card( 7, 10, "萩に猪",       "はぎ に いのしし"),
            Card( 7,  5, "萩に短冊",     "はぎ に たんざく"),
            Card( 7,  1, "萩のカス",     "はぎ の かす"),
            Card( 7,  1, "萩のカス",     "はぎ の かす"),
            Card( 8, 20, "芒に月",       "すすき に つき"),
            Card( 8, 10, "芒に雁",       "すすき に かり"),
            Card( 8,  1, "芒のカス",     "すすき の かす"),
            Card( 8,  1, "芒のカス",     "すすき の かす"),
            Card( 9, 10, "菊に盃",       "きく に さかずき"),
            Card( 9,  5, "菊に青短",     "きく に あおたん"),
            Card( 9,  1, "菊のカス",     "きく の かす"),
            Card( 9,  1, "菊のカス",     "きく の かす"),
            Card(10, 10, "紅葉に鹿",     "もみじ に しか"),
            Card(10,  5, "紅葉に青短",   "もみじ に あおたん"),
            Card(10,  1, "紅葉のカス",   "もみじ の かす"),
            Card(10,  1, "紅葉のカス",   "もみじ の かす"),
            Card(11, 20, "柳に小野道風", "やなぎ に おののみちかぜ"),
            Card(11, 10, "柳に燕",       "やなぎ に つばめ"),
            Card(11,  5, "柳に短冊",     "やなぎ に たんざく"),
            Card(11,  1, "柳のカス",     "やなぎ の かす"),
            Card(12, 20, "桐に鳳凰",     "きり に ほうおう"),
            Card(12,  1, "桐のカス",     "きり の かす"),
            Card(12,  1, "桐のカス",     "きり の かす"),
            Card(12,  1, "桐のカス",     "きり の かす"),
        )

    _VALID_MONTHS: tuple[int] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    _VALID_POINTS: tuple[int] = (1, 5, 10, 20)

    def __init__(
            self,
            month: int,
            point: int,
            name: str,
            pronounce: str
            ) -> None:
        """
            インスタンスを初期化する.

            Arguments
            ---------
            month: int
                月.
                1 以上 12 以下の整数を指定する.
            point: int
                点数.
                1, 5, 10, 20 のいずれかを指定する.
            name: str
                名前.
            pronounce: str
                読み方.

            Raises
            ------
            ValueError
                無効な値が指定された場合.
        """
        if month not in self._VALID_MONTHS:
            raise ValueError("invalid month", month)
        if point not in self._VALID_POINTS:
            raise ValueError("invalid point", point)
        if name is None:
            raise ValueError("name is None")
        if pronounce is None:
            raise ValueError("pronounce is None")

        self._month = month
        self._name = name
        self._pronounce = pronounce
        self._point = point

    def __repr__(self) -> str:
        return "{:s}({:s}, {:s}, {:s}, {:s})".format(
            self.__class__.__name__,
            repr(self._month),
            repr(self._name),
            repr(self._pronounce),
            repr(self._point),
        )

    @property
    def month(self) -> int:
        return self._month

    @property
    def point(self) -> int:
        return self._point

    @property
    def name(self) -> str:
        return self._name

    @property
    def pronounce(self) -> str:
        return self._pronounce

    @property
    def name_with_pronounce(self) -> str:
        return "{:s} ({:s})".format(self._name, self._pronounce)

    @property
    def is_kasu(self) -> bool:
        return self._point == 1

    @property
    def is_tan(self) -> bool:
        return self._point == 5

    @property
    def is_tane(self) -> bool:
        return self._point == 10

    @property
    def is_hikari(self) -> bool:
        return self._point == 20


Card.init()


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


class HandJudgement(object):
    """
        役判定.
    """

    def judge(
            self,
            cards: list[Card]
            ) -> list[Hand]:
        """
            役を判定する.

            Arguments
            ---------
            cards: list[Card]
                取り札.

            Returns
            -------
            list[Hand]
                上がり役のリスト.
                上がり役が 1 つも無い場合は空リスト.
        """
        hands = []

        # 光
        hikari_cards = self._hikari_cards_from_cards(cards)
        hikari_flags = self._flags_from_cards(hikari_cards)
        if len(hikari_cards) == 5:
            hands.append(Hand("五光", "ごこう", 10))
        if len(hikari_cards) == 4 and not (hikari_flags & 0b010000000000):
            hands.append(Hand("四光", "しこう", 8))
        if len(hikari_cards) == 4 and hikari_flags & 0b010000000000:
            hands.append(Hand("雨四光", "あめしこう", 7))
        if len(hikari_cards) == 3 and hikari_flags ^ 0b010000000000:
            hands.append(Hand("三光", "さんこう", 5))

        # 種
        tane_cards = self._tane_cards_from_cards(cards)
        tane_flags = self._flags_from_cards(tane_cards)
        if (tane_flags & 0b001001100000) == 0b001001100000:
            point = 5
            point += len(tane_cards) - 3  # 10 点札が 1 枚増えるごとに +1 点.
            hands.append(Hand("猪鹿蝶", "いのしかちょう", point))
        if len(tane_cards) >= 5:
            point = 1
            point += len(tane_cards) - 5  # 10 点札が 1 枚増えるごとに +1 点.
            hands.append(Hand("タネ", "たね", point))

        # 短冊
        tan_cards = self._tan_cards_from_cards(cards)
        tan_flags = self._flags_from_cards(tan_cards)
        if (tan_flags & 0b000000000111) == 0b000000000111:
            point = 5
            point += len(tan_cards) - 3  # 他の短冊札が 1 枚増えるごとに +1 点.
            hands.append(Hand("赤短", "あかたん", point))
        if (tan_flags & 0b001100100000) == 0b001100100000:
            point = 5
            point += len(tan_cards) - 3  # 他の短冊札が 1 枚増えるごとに +1 点.
            hands.append(Hand("青短", "あおたん", point))
        if len(tan_cards) >= 5:
            point = 1
            point += len(tan_cards) - 5  # 他の短冊札が 1 枚増えるごとに +1 点.
            hands.append(Hand("タン", "たん", point))

        # カス
        kasu_cards = self._kasu_cards_from_cards(cards)
        if len(kasu_cards) >= 10:
            point = 1
            point += len(kasu_cards) - 10  # 他のカス札が 1 枚増えるごとに +1 点.
            hands.append(Hand("カス", "かす", point))

        # オプション役
        if hikari_flags & 0b000000000100 and tane_flags & 0b000100000000:
            hands.append(Hand("花見で一杯", "はなみ で いっぱい", 5))
        if hikari_flags & 0b000010000000 and tane_flags & 0b000100000000:
            hands.append(Hand("月見で一杯", "つきみ で いっぱい", 5))

        return hands

    def _hikari_cards_from_cards(self, cards):
        return [card for card in cards if card.is_hikari]

    def _tane_cards_from_cards(self, cards):
        return [card for card in cards if card.is_tane]

    def _tan_cards_from_cards(self, cards):
        return [card for card in cards if card.is_tan]

    def _kasu_cards_from_cards(self, cards):
        return [card for card in cards if card.is_kasu]

    def _flags_from_cards(self, cards):
        months = [card.month for card in cards]
        bit_flags = [1 << (month - 1) for month in months]
        return functools.reduce(operator.or_, bit_flags, 0)

