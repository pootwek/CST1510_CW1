"""Play a simple blackjack game with each hand keeping its own cards."""

import random


def deal_card():
    """Pick one card value."""
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])


class Hand:
    """Store one player's cards and work out their score."""

    def __init__(self):
        """Start this hand with no cards."""
        self.cards = []

    def add_card(self):
        """Deal one card and add it to this hand."""
        self.cards.append(deal_card())

    def score(self):
        """Return this hand's score, counting aces as 1 when needed."""
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0

        score = sum(self.cards)
        aces = self.cards.count(11)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score


def compare(user_score, dealer_score):
    """Compare the two scores and return the result."""
    if user_score == dealer_score:
        return "It's a draw."
    if dealer_score == 0:
        return "The dealer has blackjack. You lose."
    if user_score == 0:
        return "Blackjack! You win."
    if user_score > 21:
        return "You went over 21. You lose."
    if dealer_score > 21:
        return "The dealer went over 21. You win."
    if user_score > dealer_score:
        return "You win."
    return "You lose."


def play_blackjack():
    """Run one game using two Hand objects."""
    user_hand = Hand()
    dealer_hand = Hand()
    user_hand.add_card()
    user_hand.add_card()
    dealer_hand.add_card()
    dealer_hand.add_card()

    game_over = False
    while not game_over:
        user_score = user_hand.score()
        dealer_score = dealer_hand.score()
        print(f"Your cards: {user_hand.cards} (score: {user_score})")
        print(f"Dealer's first card: {dealer_hand.cards[0]}")

        if user_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to take another card, or 'n' to stop: ").strip().lower()
            if choice == "y":
                user_hand.add_card()
            else:
                game_over = True

    user_score = user_hand.score()
    dealer_score = dealer_hand.score()
    while dealer_score < 17 and dealer_score != 0:
        dealer_hand.add_card()
        dealer_score = dealer_hand.score()

    print(f"Your final cards: {user_hand.cards} (score: {user_score})")
    print(f"Dealer's final cards: {dealer_hand.cards} (score: {dealer_score})")
    print(compare(user_score, dealer_score))


if __name__ == "__main__":
    play_blackjack()
