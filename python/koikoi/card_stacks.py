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
        random.shuffle(self.stocked)

        # 山札から子に 2 枚, 場に 2 枚, 親に 2 枚配ることを 4 回繰り返す.
        for i in range(4):
            self.child.append(self.stocked.pop())
            self.child.append(self.stocked.pop())
            self.field.append(self.stocked.pop())
            self.field.append(self.stocked.pop())
            self.parent.append(self.stocked.pop())
            self.parent.append(self.stocked.pop())

