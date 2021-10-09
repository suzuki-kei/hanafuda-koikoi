

from .card import Card
import abc


class Player(abc.ABC):
    """
        競技者.
    """

    @abc.abstractmethod
    def choose_from_own_cards(self, cards: list[Card]) -> Card:
        """
            手札から 1 枚選ぶ.

            Arguments
            ---------
            cards: list[Card]
                手札.

            Returns
            -------
            Card
                札.
        """

    @abc.abstractmethod
    def choose_gained_card(self, card: Card, matched_cards: list[Card]) -> Card:
        """
            場札から取り札を選択する.

            Arguments
            ---------
            card: Card
                手札または山札から場に出された札.
            matched_cards: list[Card]
                合い札となる場札.

            Returns
            -------
            Card
                matched_cards から取り札として選択した札.
        """


class SimplePlayer(Player):
    """
        単純な戦略の競技者.
    """

    def choose_from_own_cards(self, cards: list[Card]) -> Card:
        return cards.pop()

    def choose_gained_card(self, card: Card, matched_cards: list[Card]) -> Card:
        return matched_cards[0]

