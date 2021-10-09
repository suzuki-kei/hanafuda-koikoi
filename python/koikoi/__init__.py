"""
    花札の "こいこい" に関する機能を提供する.

    用語定義
    --------
    こいこい (koikoi)
        本モジュールが対象とする花札の競技.
        こいこいは 12 回の試合で構成される.
        各試合における得失点の積み重ねによって, 競技全体の勝ち負けを決する.

    競技 (game)
        最終的な勝ち負けが決する単位.
        こいこいでは 12 回の試合を行う.

    試合 (round)
        得失点が決する最小単位.
        試合は 12 回行い, それぞれ以下の名前が付けられている.

         * 1 月 ... 1 回目の試合
         * 2 月 ... 2 回目の試合
         * 3 月 ... 3 回目の試合
         * ...
         * 12 月 ... 12 回目の試合

    競技者 (player)
        こいこいに参加する人.

    親 (parent)
        各試合において, 先攻して行動する競技者.

    子 (child)
        各試合において, 後攻して行動する競技者.

    山札 (stocked cards)
        裏向きに置かれた札.
        試合開始時点では 24 枚ある.
        試合の進行とともに, 競技者にめくられることで減る.

    場札 (field cards)
        場に表向きに置かれる札.
        試合開始時点では 8 枚ある.
        場札は合い札によって減り, 捨て札によって増える.

    手札 (player's cards)
        試合開始時点で各競技者に配られる札.

    合い札 (matched cards)
        手札から出した札と場札のいずれかの札の月が合うこと.
        もしくは, 山札から取った札と場札のいずれかの札の月が合うこと.
        合い札となった場合, その競技者の取り札となる.

    捨て札 (unmatched card)
        手札から出した札と場札のいずれとも札の月が合わないこと.
        もしくは, 山札から取った札と場札のいずれとも札の月が合わないこと.
        捨て札となった場合, その札は場札となる.

    取り札 (gained cards)
        合い札となり取得した札.

    役 (hand)
        得点となる札の組み合わせのこと.
"""


from .card import Card
from .card_stacks import CardStacks
from .game import Game
from .game import GameIsOver
from .hand import Hand
from .hand_judgement import HandJudgement
from .player import Player
from .player import SimplePlayer

