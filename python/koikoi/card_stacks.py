from .card import Card
import dataclasses
import random


@dataclasses.dataclass(frozen=True)
class CardStacks(object):
    """
        山札, 場札, 親の手札, 親の取り札, 子の手札, 子の取り札.
    """

    stocked: list[Card] = dataclasses.field(default_factory=Card.list, init=False)
    """山札"""

    field: list[Card] = dataclasses.field(default_factory=list, init=False)
    """場札"""

    parent: list[Card] = dataclasses.field(default_factory=list, init=False)
    """親の手札"""

    parent_gained: list[Card] = dataclasses.field(default_factory=list, init=False)
    """親の取り札"""

    child: list[Card] = dataclasses.field(default_factory=list, init=False)
    """子の手札"""

    child_gained: list[Card] = dataclasses.field(default_factory=list, init=False)
    """子の取り札"""

    def __post_init__(self) -> None:
        """
            山札を混ぜ, 札を配る.
        """
        while True:
            # 山札を混ぜる.
            random.shuffle(self.stocked)

            # 山札から子に 2 枚, 場に 2 枚, 親に 2 枚配ることを 4 回繰り返す.
            for i in range(4):
                self.child.append(self.stocked.pop())
                self.child.append(self.stocked.pop())
                self.field.append(self.stocked.pop())
                self.field.append(self.stocked.pop())
                self.parent.append(self.stocked.pop())
                self.parent.append(self.stocked.pop())

            # 場札に同じ月の札が 4 枚出た場合は配り直す.
            if self._contains_four_cards_of_same_month(self.field):
                continue

            break

    def _contains_four_cards_of_same_month(
            self,
            field_cards: list[Card]
            ) -> bool:
        """
            同じ月の札が 4 枚あることを判定する.

            Arguments
            ---------
            field_cards: list[Card]
                場札.

            Returns
            -------
            bool
                True の場合, field_cards に同じ月の札が 4 枚含まれる.
        """
        # counts[N] に N 月の札の枚数を保持する.
        counts = [0] * 13

        for card in field_cards:
            counts[card.month] += 1
            if counts[card.month] == 4:
                return True
        return False

