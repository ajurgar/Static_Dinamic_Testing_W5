import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card('As', 1)
        self.card2 = Card('Poker', 8)
        self.card3 = Card('Horse', 7)
        self.cards = [self.card, self.card2, self.card3]

    def test_check_for_ace(self):
        self.assertEqual(True, self.card.check_for_ace(self.card))

    def test_check_for_ace_2(self):
        card1 = Card('As', 4)
        self.assertEqual(False, card1.check_for_ace(card1))


    def test_highest_card(self):
        card1 = Card('As', 8)
        card2 = Card('Poker', 6)
        self.assertEqual(card1, self.card.highest_card(card1, card2))

    def test_highest_card_2(self):
        card1 = Card('As', 6)
        card2 = Card('Poker', 8)
        self.assertEqual(card2, self.card.highest_card(card1, card2))
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 16", self.card.cards_total(self.cards))
