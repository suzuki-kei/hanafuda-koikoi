from .card import Card
from .hand import Hand
import functools
import operator


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

