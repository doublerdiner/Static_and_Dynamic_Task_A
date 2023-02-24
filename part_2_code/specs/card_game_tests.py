import unittest 
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    card_1 = Card("Spades", 7)
    card_2 = Card("Clubs", 1)

    def test_check_for_ace__True(self):
        answer = CardGame.check_for_ace(self, self.card_2)
        self.assertEqual(True, answer)

    def test_check_for_ace__False(self):
        answer = CardGame.check_for_ace(self, self.card_1)
        self.assertEqual(False, answer)

    def test_highest_card(self):
        answer = CardGame.highest_card(self, self.card_1, self.card_2)
        self.assertEqual(self.card_1, answer)

    def test_cards_total(self):
        cards = [self.card_1, self.card_2]
        answer = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 8", answer)

        