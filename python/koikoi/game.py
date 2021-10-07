from .card import Card
from .player import Player
import collections
import random
import typing


StockedCards = list[Card]
"""
    山札.
"""


FieldCards = list[Card]
"""
    場札.
"""


ParentCards = list[Card]
"""
    親の手札.
"""


ChildCards = list[Card]
"""
    子の手札.
"""


CardStacks = collections.namedtuple("CardStacks", (
    "stocked",
    "field",
    "parent",
    "parent_gained",
    "child",
    "child_gained",
))
"""
    山札, 場札, 親の手札, 親の取り札, 子の手札, 子の取り札.
"""


Players = collections.namedtuple("Players", (
    "parent",
    "child",
))
"""
    親プレイヤーと子プレイヤー.
"""


Action = typing.Callable[["Game"], typing.Callable]
"""
    競技の状態を進める Game クラスのインスタンスメソッド.
"""


class GameIsOver(Exception):
    """
        競技が終了していることを表す例外.
    """


class Game(object):
    """
        ゲーム.
    """

    def __init__(
            self,
            player1: Player,
            player2: Player
            ) -> None:
        """
            インスタンスを初期化する.

            Arguments
            ---------
            player1: Player
                プレイヤー.
            player2: Player
                プレイヤー.
        """
        self._player1 = player1
        self._player2 = player2
        self._next = self._start_game

    def __str__(self) -> str:
        def card_stacks_to_string(card_stacks):
            if card_stacks is None:
                return "None"
            return "(stocked={}, field={}, parent={}, parent_gained={}, child={}, child_gained={})".format(
                len(self._card_stacks.stocked),
                len(self._card_stacks.field),
                len(self._card_stacks.parent),
                len(self._card_stacks.parent_gained),
                len(self._card_stacks.child),
                len(self._card_stacks.child_gained),
            )

        return "round={}, card_stacks={}, next={}".format(
            getattr(self, "_round", None),
            card_stacks_to_string(getattr(self, "_card_stacks", None)),
            self._next.__name__,
        )

    def is_over(self) -> bool:
        """
            競技が終了していることを判定する.
        """
        return self._next == self._game_is_over

    def next(self) -> None:
        """
            競技を進行する.
        """
        self._next = self._next()

    def _start_game(self) -> Action:
        """
            競技を開始する.
        """
        return self._decide_playing_order

    def _decide_playing_order(self) -> Action:
        """
            競技の順番 (親と子) を決める.
        """
        self._players = _decide_playing_order(self._player1, self._player2)
        return self._initialize_round_counter

    def _initialize_round_counter(self) -> Action:
        """
            試合のカウントを初期化する.
        """
        self._round = 1
        return self._initialize_points

    def _initialize_points(self) -> Action:
        """
            親と子の得点を初期化する.
        """
        self._parent_point = 0
        self._child_point = 0
        return self._start_round

    def _start_round(self) -> Action:
        """
            試合を開始する.
        """
        return self._distribute_cards

    def _distribute_cards(self) -> Action:
        """
            札を配る.
        """
        self._card_stacks = _distribute_cards()
        return self._parent_player_plays

    def _parent_player_plays(self) -> Action:
        """
            親が行動する.
        """
        return self._parent_choose_from_own_cards

    def _parent_choose_from_own_cards(self):
        """
            親が手札から 1 枚選ぶ.
        """
        card = self._players.parent.choose_from_own_cards(self._card_stacks.parent)
        # TODO 場札とマッチさせる.
        #_parent_matches_to_field_cards(self._players.parent, self._card_stacks, card)
        return self._parent_take_out_from_stocked_cards

    def _parent_take_out_from_stocked_cards(self) -> Action:
        """
            親が山札から 1 枚引く.
        """
        card = self._card_stacks.stocked.pop()
        # TODO 場札とマッチさせる.
        return self._child_player_plays

    def _child_player_plays(self) -> Action:
        """
            子が行動する.
        """
        return self._child_choose_from_own_cards

    def _child_choose_from_own_cards(self):
        """
            子が手札から 1 枚選ぶ.
        """
        card = self._players.child.choose_from_own_cards(self._card_stacks.child)
        # TODO 場札とマッチさせる.
        return self._child_take_out_from_stocked_cards

    def _child_take_out_from_stocked_cards(self) -> Action:
        """
            子が山札から 1 枚引く.
        """
        card = self._card_stacks.stocked.pop()
        # TODO 場札とマッチさせる.

        if len(self._card_stacks.child) > 0:
            return self._parent_player_plays
        else:
            return self._finish_round

    def _finish_round(self) -> Action:
        """
            試合を終了する.
        """
        if self._round < 12:
            self._round += 1
            return self._start_round
        else:
            return self._finish_game

    def _finish_game(self) -> Action:
        """
            競技を終了する.
        """
        self._round = None
        return self._game_is_over

    def _game_is_over(self):
        """
            競技は終了している.
        """
        raise GameIsOver()


def _decide_playing_order(player1: Player, player2: Player) -> Players:
    """
        競技の順番 (親と子) を決める.

        Arguments
        ---------
        player1: Player
            プレイヤー.
        player2: Player
            プレイヤー.

        Returns
        -------
        Players
            親プレイヤーと子プレヤー.
    """
    while True:
        # 札をシャッフルする.
        cards = Card.list()
        random.shuffle(cards)

        # 先頭から 1 枚ずつ札を取る.
        player1_card = cards[0]
        player2_card = cards[1]

        # 月の小さい方が親となる.
        if player1_card.month < player2_card.month:
            return Players(parent=player1, child=player2)
        if player1_card.month > player2_card.month:
            return Players(parent=player2, child=player1)

        # 月が同じ場合は, 札の点数が大きい方が親となる.
        if player1_card.point > player2_card.point:
            return Players(parent=player1, child=player2)
        if player1_card.point < player2_card.point:
            return Players(parent=player2, child=player1)

        # 点数も同じ場合はやり直し.
        continue


def _distribute_cards() -> CardStacks:
    """
        試合を開始するために, 札を配る.

        Returns
        -------
        CardStacks
            CardStacks.
    """
    # 全てのカードをシャッフルし, 山札とする.
    stocked_cards = Card.list()
    random.shuffle(stocked_cards)

    # 子の手札, 場札, 親の手札.
    child_cards, field_cards, parent_cards = [], [], []

    # 山札から子に 2 枚, 場に 2 枚, 親に 2 枚配ることを 4 回繰り返す.
    for i in range(4):
        child_cards.append(stocked_cards.pop(0))
        child_cards.append(stocked_cards.pop(0))
        field_cards.append(stocked_cards.pop(0))
        field_cards.append(stocked_cards.pop(0))
        parent_cards.append(stocked_cards.pop(0))
        parent_cards.append(stocked_cards.pop(0))

    return CardStacks(
        stocked=stocked_cards,
        field=field_cards,
        parent=parent_cards,
        parent_gained=[],
        child=child_cards,
        child_gained=[],
    )

