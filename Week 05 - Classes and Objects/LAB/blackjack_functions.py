"""Play a simple blackjack game using functions and card lists."""

import random


def deal_card():
    """Pick one card value."""
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])


def calculate_score(cards):
    """Work out a hand's score, including aces and blackjack."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    score = sum(cards)
    while score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
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
    """Run one game using separate card lists and functions."""
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards} (score: {user_score})")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to take another card, or 'n' to stop: ").strip().lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final cards: {user_cards} (score: {user_score})")
    print(f"Dealer's final cards: {dealer_cards} (score: {dealer_score})")
    print(compare(user_score, dealer_score))


if __name__ == "__main__":
    play_blackjack()
