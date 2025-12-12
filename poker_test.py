import unittest
from poker import Card, Deck, HandEvaluator


class TestPokerMethods(unittest.TestCase):
    def test_card_init(self):
        card = Card("Herz", "Ass")
        self.assertEqual(card.suit, "Herz")
        self.assertEqual(card.value, 14)

        with self.assertRaises(ValueError):
            Card("Ungültig", "10")

        with self.assertRaises(ValueError):
            Card("Pik", "11")

    def test_deck_deal(self):
        deck = Deck()

        self.assertEqual(len(deck.cards), 51, "Deck länge ist falsch")

        card = deck.deal(1)
        self.assertIsInstance(card, Card)

        deck.cards = []
        with self.assertRaises(ValueError):
            deck.deal(1)

    def test_check_flush(self):
        flush_hand = [
            Card("Herz", "2"),
            Card("Herz", "5"),
            Card("Herz", "9"),
            Card("Herz", "Bube"),
            Card("Herz", "König"),
        ]
        evaluator_flush = HandEvaluator(flush_hand)
        self.assertTrue(evaluator_flush.is_flush)

        mixed_hand = [
            Card("Herz", "2"),
            Card("Karo", "5"),
            Card("Herz", "9"),
            Card("Herz", "Bube"),
            Card("Herz", "König"),
        ]
        evaluator_mixed = HandEvaluator(mixed_hand)
        self.assertFalse(evaluator_mixed.is_flush)

    def test_evaluate_full_house(self):
        full_house_hand = [
            Card("Pik", "König"),
            Card("Herz", "König"),
            Card("Karo", "König"),
            Card("Pik", "Dame"),
            Card("Kreuz", "Dame"),
        ]

        evaluator = HandEvaluator(full_house_hand)
        result = evaluator.evaluate_hand()

        self.assertEqual(result, "Full House")
        self.assertEqual(evaluator.counts, [3, 2])


if __name__ == "__main__":
    unittest.main()
