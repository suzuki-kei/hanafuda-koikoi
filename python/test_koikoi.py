"""
    koikoi のテストケース.
"""


from koikoi import Card
from koikoi import Hand
from koikoi import HandJudgement
import unittest
import itertools


class CardInitTestCase(unittest.TestCase):
    """
        Card.__init__() のテストケース.
    """

    def test_if_invalid_month_passed(self):
        months = (
            -1,     # 負数
            0, 13,  # 有効値の前後
        )
        for month in months:
            with self.subTest(month=month):
                with self.assertRaises(ValueError):
                    Card(month, 1, "テスト", "てすと")

    def test_if_invalid_point_passed(self):
        points = (
            -1,     # 負数
            0, 2,   # 有効値の前後
            4, 6,   # 有効値の前後
            9, 11,  # 有効値の前後
            19, 21, # 有効値の前後
        )
        for point in points:
            with self.subTest(point=point):
                with self.assertRaises(ValueError):
                    Card(1, point, "テスト", "てすと")


class CardCardsInitTestCase(unittest.TestCase):
    """
        Card.cards のテストケース.
    """

    def test_there_are_48_cards_in_total(self):
        """
            全体で 48 枚の札が存在する.
        """
        self.assertEqual(48, len(Card.cards))

    def test_there_are_4_cards_for_each_month(self):
        """
            どの月にも 4 枚の札が存在する.
        """
        for month in range(1, 13):
            with self.subTest(month=month):
                cards = [card for card in Card.cards if card.month == month]
                self.assertEqual(4, len(cards))

    def test_there_are_5_hikari_cards(self):
        """
            光札は 5 枚存在する.
        """
        cards = [card for card in Card.cards if card.is_hikari]
        self.assertEqual(5, len(cards))

    def test_there_are_9_tane_cards(self):
        """
            タネ札は 9 枚存在する.
        """
        cards = [card for card in Card.cards if card.is_tane]
        self.assertEqual(9, len(cards))

    def test_there_are_10_tan_cards(self):
        """
            タン札は 10 枚存在する.
        """
        cards = [card for card in Card.cards if card.is_tan]
        self.assertEqual(10, len(cards))

    def test_there_are_24_kasu_cards(self):
        """
            カス札は 24 枚存在する.
        """
        cards = [card for card in Card.cards if card.is_kasu]
        self.assertEqual(24, len(cards))


class HandJudgementJudgeTestCase(unittest.TestCase):
    """
        HandJudgement.judge() のテストケース.
    """

    def _judge(self, cards):
        return HandJudgement().judge(cards)

    def test(self):
        cards = []
        self.assertEqual([], HandJudgement().judge(cards))

    def test_五光(self):
        cards = [
            Card.list(month=month, point=20)[0]
            for month in (1, 3, 8, 11, 12)
        ]
        expected = [
            Hand("五光", "ごこう", 10),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_四光(self):
        cards = [
            Card.list(month=month, point=20)[0]
            for month in (1, 3, 8, 12)
        ]
        expected = [
            Hand("四光", "しこう", 8),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_雨四光(self):
        cards = [
            Card.list(month=month, point=20)[0]
            for month in (1, 3, 11, 12)
        ]
        expected = [
            Hand("雨四光", "あめしこう", 7),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_三光(self):
        for months in itertools.combinations([1, 3, 8, 12], 3):
            cards = [
                Card.list(month=month, point=20)[0]
                for month in months
            ]
            with self.subTest(cards=cards):
                expected = [
                    Hand("三光", "さんこう", 5),
                ]
                self.assertEqual(
                    expected,
                    HandJudgement().judge(cards)
                )

    def test_猪鹿蝶(self):
        cards = [
            Card.list(month=month, point=10)[0]
            for month in (6, 7, 10)
        ]
        expected = [
            Hand("猪鹿蝶", "いのしかちょう", 5),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_猪鹿蝶_追加点(self):
        cards = [
            Card.list(month=month, point=10)[0]
            for month in (2, 6, 7, 10)
        ]
        expected = [
            Hand("猪鹿蝶", "いのしかちょう", 6),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_タネ(self):
        for months in itertools.combinations([2, 4, 5, 6, 7, 8, 9, 10, 11], 5):
            cards = [
                Card.list(month=month, point=10)[0]
                for month in months
            ]
            with self.subTest(cards=cards):
                if all(map(lambda month: month in months, (6, 7, 10))):
                    expected = [
                        Hand("猪鹿蝶", "いのしかちょう", 7),
                        Hand("タネ", "たね", 1),
                    ]
                else:
                    expected = [
                        Hand("タネ", "たね", 1),
                    ]
                self.assertEqual(
                    expected,
                    HandJudgement().judge(cards)
                )

    def test_タネ_追加点(self):
        for months in itertools.combinations([2, 4, 5, 6, 7, 8, 9, 10, 11], 6):
            cards = [
                Card.list(month=month, point=10)[0]
                for month in months
            ]
            with self.subTest(cards=cards):
                if all(map(lambda month: month in months, (6, 7, 10))):
                    expected = [
                        Hand("猪鹿蝶", "いのしかちょう", 8),
                        Hand("タネ", "たね", 2),
                    ]
                else:
                    expected = [
                        Hand("タネ", "たね", 2),
                    ]
                self.assertEqual(
                    expected,
                    HandJudgement().judge(cards)
                )

    def test_赤短(self):
        # TODO 5 点札が 1 枚増えるごとに +1 点される場合もテストする.
        cards = [
            Card.list(month=month, point=5)[0]
            for month in (1, 2, 3)
        ]
        expected = [
            Hand("赤短", "あかたん", 5),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_青短(self):
        # TODO 5 点札が 1 枚増えるごとに +1 点される場合もテストする.
        cards = [
            Card.list(month=month, point=5)[0]
            for month in (6, 9, 10)
        ]
        expected = [
            Hand("青短", "あおたん", 5),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_タン(self):
        # TODO 5 点札が 1 枚増えるごとに +1 点される場合もテストする.
        for months in itertools.combinations([1, 2, 3, 4, 5, 6, 7, 9, 10, 11], 5):
            cards = [
                Card.list(month=month, point=5)[0]
                for month in months
            ]
            with self.subTest(cards=cards):
                if all(map(lambda month: month in months, (1, 2, 3))):
                    expected = [
                        Hand("赤短", "あかたん", 7),
                        Hand("タン", "たん", 1),
                    ]
                elif all(map(lambda month: month in months, (6, 9, 10))):
                    expected = [
                        Hand("青短", "あおたん", 7),
                        Hand("タン", "たん", 1),
                    ]
                else:
                    expected = [
                        Hand("タン", "たん", 1),
                    ]
                self.assertEqual(
                    expected,
                    HandJudgement().judge(cards)
                )

    @unittest.skip("80 sec くらいかかった")
    def test_カス(self):
        # TODO 1 点札が 1 枚増えるごとに +1 点される場合もテストする.
        kasu_cards = list(filter(lambda card: card.is_kasu, Card.cards))
        for cards in itertools.combinations(kasu_cards, 10):
            with self.subTest(cards=cards):
                expected = [
                    Hand("カス", "かす", 1),
                ]
                self.assertEqual(
                    expected,
                    HandJudgement().judge(cards)
                )

    def test_花見で一杯(self):
        cards = [
            Card.list(month=3, point=20)[0],
            Card.list(month=9, point=10)[0],
        ]
        expected = [
            Hand("花見で一杯", "はなみ で いっぱい", 5),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_月見で一杯(self):
        cards = [
            Card.list(month=8, point=20)[0],
            Card.list(month=9, point=10)[0],
        ]
        expected = [
            Hand("月見で一杯", "つきみ で いっぱい", 5),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_組み合わせ_五光と赤短(self):
        cards = [
            # 五光
            Card.list(month=1, point=20)[0],
            Card.list(month=3, point=20)[0],
            Card.list(month=8, point=20)[0],
            Card.list(month=11, point=20)[0],
            Card.list(month=12, point=20)[0],

            # 赤短
            Card.list(month=1, point=5)[0],
            Card.list(month=2, point=5)[0],
            Card.list(month=3, point=5)[0],
        ]
        expected = [
            Hand("五光", "ごこう", 10),
            Hand("赤短", "あかたん", 5),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )

    def test_組み合わせ_猪鹿蝶とカス(self):
        cards = [
            # 猪鹿蝶
            Card.list(month=6, point=10)[0],
            Card.list(month=7, point=10)[0],
            Card.list(month=10, point=10)[0],

            # カス
            Card.list(month=1, point=1)[0],
            Card.list(month=2, point=1)[0],
            Card.list(month=3, point=1)[0],
            Card.list(month=4, point=1)[0],
            Card.list(month=5, point=1)[0],
            Card.list(month=6, point=1)[0],
            Card.list(month=7, point=1)[0],
            Card.list(month=8, point=1)[0],
            Card.list(month=9, point=1)[0],
            Card.list(month=10, point=1)[0],
        ]
        expected = [
            Hand("猪鹿蝶", "いのしかちょう", 5),
            Hand("カス", "かす", 1),
        ]
        self.assertEqual(
            expected,
            HandJudgement().judge(cards)
        )


if __name__ == "__main__":
    unittest.main()

