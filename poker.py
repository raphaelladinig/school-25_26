import random
from collections import Counter
from functools import total_ordering


@total_ordering
class Card:
    SUITS = ["Herz", "Karo", "Kreuz", "Pik"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Bube",
        "Dame",
        "König",
        "Ass",
    ]
    VALUES = {rank: i + 2 for i, rank in enumerate(RANKS)}

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise ValueError(f"Ungültige Farbe: {suit}")
        if rank not in self.RANKS:
            raise ValueError(f"Ungültiger Rang: {rank}")

        self.suit = suit
        self.rank = rank
        self.value = self.VALUES[rank]

    def __repr__(self):
        return f"Card('{self.suit}', '{self.rank}')"

    def __str__(self):
        return f"{self.rank} von {self.suit}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards=1):
        if num_cards > len(self.cards):
            raise ValueError("Nicht genügend Karten im Deck zum Austeilen.")

        if num_cards == 1:
            return self.cards.pop()

        return [self.cards.pop() for _ in range(num_cards)]


class HandEvaluator:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError("Eine Hand muss aus genau 5 Karten bestehen.")
        self.cards = sorted(cards, reverse=True)

        self.values = [card.value for card in self.cards]
        self.suits = [card.suit for card in self.cards]

        self.rank_counts = Counter(self.values)

        self.counts = sorted(self.rank_counts.values(), reverse=True)

        self.is_flush = self._check_flush()
        self.is_straight = self._check_straight()

    def _check_flush(self):
        return len(set(self.suits)) == 1

    def _check_straight(self):
        if self.values == [14, 5, 4, 3, 2]:
            return True

        is_consecutive = self.values[0] - self.values[4] == 4
        has_no_pairs = len(self.rank_counts) == 5

        return is_consecutive and has_no_pairs

    def evaluate_hand(self):
        if self.is_straight and self.is_flush:
            if self.values[0] == Card.VALUES["Ass"]:
                return "Royal Flush"
            return "Straight Flush"

        if self.counts == [4, 1]:
            return "Poker (Vierling)"

        if self.counts == [3, 2]:
            return "Full House"

        if self.is_flush:
            return "Flush"

        if self.is_straight:
            return "Strasse"

        if self.counts == [3, 1, 1]:
            return "Drilling"

        return ("Zwei Paare", "Ein Paar", "Höchste Karte")[
           0 if self.counts == [2, 2, 1] else 1 if self.counts == [2, 1, 1, 1] else 2
        ]


def run_simulation(num_games):
    hand_counts = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Poker (Vierling)": 0,
        "Full House": 0,
        "Flush": 0,
        "Strasse": 0,
        "Drilling": 0,
        "Zwei Paare": 0,
        "Ein Paar": 0,
        "Höchste Karte": 0,
    }

    for _ in range(num_games):
        deck = Deck()

        hand_cards = deck.deal(5)

        evaluator = HandEvaluator(hand_cards)
        result = evaluator.evaluate_hand()

        hand_counts[result] += 1

    return hand_counts


def compare_with_reality(sim_results, num_games):
    real_probabilities = {
        "Royal Flush": (4 / 2598960) * 100,  # 0.000154%
        "Straight Flush": (36 / 2598960) * 100,  # 0.00139%
        "Poker (Vierling)": (624 / 2598960) * 100,  # 0.0240%
        "Full House": (3744 / 2598960) * 100,  # 0.1441%
        "Flush": (5108 / 2598960) * 100,  # 0.1965%
        "Strasse": (10200 / 2598960) * 100,  # 0.3925%
        "Drilling": (54912 / 2598960) * 100,  # 2.1128%
        "Zwei Paare": (123552 / 2598960) * 100,  # 4.7539%
        "Ein Paar": (1098240 / 2598960) * 100,  # 42.2569%
        "Höchste Karte": (1302540 / 2598960) * 100,  # 50.1177%
    }

    print(f"{'Kombination':<20} | {'Simulation (%)':<15} | {'Echt (%)':<15}")
    print("-" * 50)

    for hand_name, sim_count in sim_results.items():
        sim_perc = (sim_count / num_games) * 100
        real_perc = real_probabilities[hand_name]
        print(f"{hand_name:<20} | {sim_perc:<15.4f} | {real_perc:<15.4f}")


if __name__ == "__main__":
    num_games = 100000
    results = run_simulation(num_games)
    compare_with_reality(results, num_games)
