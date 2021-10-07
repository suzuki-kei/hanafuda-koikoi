

from .card import Card
import abc


class Player(abc.ABC):
    """
        プレイヤー.
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
        print("!!!")


class SimplePlayer(Player):
    """
        単純な戦略のプレイヤー.
    """

    def choose_from_own_cards(self, cards: list[Card]) -> Card:
        return cards.pop()

