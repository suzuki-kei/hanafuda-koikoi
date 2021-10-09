"""
    koikoi.Card のテストケース.
"""


from koikoi import Card
import unittest


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
        Card._cards のテストケース.
    """

    def test_there_are_48_cards_in_total(self):
        """
            全体で 48 枚の札が存在する.
        """
        self.assertEqual(48, len(Card._cards))

    def test_there_are_4_cards_for_each_month(self):
        """
            どの月にも 4 枚の札が存在する.
        """
        for month in range(1, 13):
            with self.subTest(month=month):
                cards = [card for card in Card._cards if card.month == month]
                self.assertEqual(4, len(cards))

    def test_there_are_5_hikari_cards(self):
        """
            光札は 5 枚存在する.
        """
        cards = [card for card in Card._cards if card.is_hikari]
        self.assertEqual(5, len(cards))

    def test_there_are_9_tane_cards(self):
        """
            タネ札は 9 枚存在する.
        """
        cards = [card for card in Card._cards if card.is_tane]
        self.assertEqual(9, len(cards))

    def test_there_are_10_tan_cards(self):
        """
            タン札は 10 枚存在する.
        """
        cards = [card for card in Card._cards if card.is_tan]
        self.assertEqual(10, len(cards))

    def test_there_are_24_kasu_cards(self):
        """
            カス札は 24 枚存在する.
        """
        cards = [card for card in Card._cards if card.is_kasu]
        self.assertEqual(24, len(cards))


if __name__ == "__main__":
    unittest.main()

