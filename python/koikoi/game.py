from .card import Card
from .hand_judgement import HandJudgement
from .player import Player
import dataclasses
import random
import typing


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


@dataclasses.dataclass(frozen=True)
class Players(object):
    """
        親と子.
    """

    parent: Player
    """親"""

    child: Player
    """子"""


class GameIsOver(Exception):
    """
        競技が終了していることを表す例外.
    """


class Game(object):
    """
        競技.
    """

    _Action = typing.Callable[["Game"], typing.Callable]
    """
        競技を 1 ステップ進行するプライベートメソッド.
        競技を 1 ステップ進行してから, 次の _Action を返す.
        self._next に設定しておき, next() メソッドで使用される.
    """

    def __init__(
            self,
            player1: Player,
            player2: Player,
            hand_judgement: HandJudgement
            ) -> None:
        """
            インスタンスを初期化する.

            Arguments
            ---------
            player1: Player
                競技者.
            player2: Player
                競技者.
            hand_judgement: HandJudgement
                役判定.
        """
        self._player1 = player1
        self._player2 = player2
        self._hand_judgement = hand_judgement
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

    def _start_game(self) -> _Action:
        """
            競技を開始する.
        """
        return self._decide_playing_order

    def _decide_playing_order(self) -> _Action:
        """
            競技の順番 (親と子) を決める.
        """
        self._players = _decide_playing_order(self._player1, self._player2)
        return self._initialize_round_counter

    def _initialize_round_counter(self) -> _Action:
        """
            試合のカウントを初期化する.
        """
        self._round = 1
        return self._initialize_points

    def _initialize_points(self) -> _Action:
        """
            親と子の得点を初期化する.
        """
        self._parent_point = 0
        self._child_point = 0
        return self._start_round

    def _start_round(self) -> _Action:
        """
            試合を開始する.
        """
        return self._distribute_cards

    def _distribute_cards(self) -> _Action:
        """
            札を配る.
        """
        self._card_stacks = CardStacks()
        return self._parent_player_plays

    def _parent_player_plays(self) -> _Action:
        """
            親が行動する.
        """
        return self._parent_choose_from_own_cards

    def _parent_choose_from_own_cards(self):
        """
            親が手札から 1 枚選ぶ.
        """
        card = self._players.parent.choose_from_own_cards(self._card_stacks.parent)
        _decide_gained_card(self._players.parent, card, self._card_stacks.field, self._card_stacks.parent_gained)
        return self._parent_take_out_from_stocked_cards

    def _parent_take_out_from_stocked_cards(self) -> _Action:
        """
            親が山札から 1 枚引く.
        """
        card = self._card_stacks.stocked.pop()
        _decide_gained_card(self._players.parent, card, self._card_stacks.field, self._card_stacks.parent_gained)
        # TODO 役が成立しているか判定する.
        # TODO 勝負 or こいこい, を決める.
        return self._child_player_plays

    def _child_player_plays(self) -> _Action:
        """
            子が行動する.
        """
        return self._child_choose_from_own_cards

    def _child_choose_from_own_cards(self):
        """
            子が手札から 1 枚選ぶ.
        """
        card = self._players.child.choose_from_own_cards(self._card_stacks.child)
        _decide_gained_card(self._players.child, card, self._card_stacks.field, self._card_stacks.child_gained)
        return self._child_take_out_from_stocked_cards

    def _child_take_out_from_stocked_cards(self) -> _Action:
        """
            子が山札から 1 枚引く.
        """
        card = self._card_stacks.stocked.pop()
        _decide_gained_card(self._players.child, card, self._card_stacks.field, self._card_stacks.child_gained)
        # TODO 役が成立しているか判定する.
        # TODO 勝負 or こいこい, を決める.

        if len(self._card_stacks.child) > 0:
            return self._parent_player_plays
        else:
            return self._finish_round

    def _finish_round(self) -> _Action:
        """
            試合を終了する.
        """
        if self._round < 12:
            self._round += 1
            return self._start_round
        else:
            return self._finish_game

    def _finish_game(self) -> _Action:
        """
            競技を終了する.
        """
        self._round = None
        return self._game_is_over

    def _game_is_over(self) -> typing.NoReturn:
        """
            競技は終了している.

            Raises
            ------
            GameIsOver
                常に GameIsOver を raise する.
        """
        raise GameIsOver()


def _decide_playing_order(player1: Player, player2: Player) -> Players:
    """
        競技の順番 (親と子) を決める.

        Arguments
        ---------
        player1: Player
            競技者.
        player2: Player
            競技者.

        Returns
        -------
        Players
            親と子.
    """
    while True:
        # 札を混ぜる.
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


def _decide_gained_card(
        player: Player,
        card: Card,
        field_cards: list[Card],
        gained_cards: list[Card]
        ) -> None:
    """
        取り札を決定する.

        決定内容に従い, 引数の field_card, gained_cards を変更する.

        Arguments
        ---------
        player: Player
            競技者.
        card: Card
            手札または山札から場に出された札.
        field_cards: list[Card]
            場札.
        gained_cards: list[Card]
            取り札.
    """
    # 場札のうち, 合い札だけを取り出す.
    month_matches = lambda _: _.month == card.month
    matched_cards = list(filter(month_matches, field_cards))

    match len(matched_cards):
        # 合い札ができなければ, 場に札を置いて終了する.
        case 0:
            field_cards.append(card)

        # 場札に合い札の候補が 1 枚だけの場合, その札を取る.
        case 1:
            gained_cards.append(card)
            gained_cards.append(matched_cards[0])

        # 場札に合い札の候補が 2 枚だけの場合, 競技者が取り札を選択する.
        case 2:
            choosed_card = player.choose_gained_card(card, matched_cards)
            field_cards.remove(choosed_card)
            gained_cards.append(card)
            gained_cards.append(choosed_card)

        # 場札に合い札の候補が 3 枚だけの場合, 全ての札を取る.
        case 3:
            gained_cards.append(card)
            gained_cards.append(matched_cards[0])
            gained_cards.append(matched_cards[1])
            gained_cards.append(matched_cards[2])

        case _:
            raise Exception("The bug.")

