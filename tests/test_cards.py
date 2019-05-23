"""Test the Card and Deck classes"""

from TerminalPlayingCards.cards import Card


def test_card_str_value():
    """Ensure the string value given the card"""
    ace_spades = Card("A", "spades")
    ace_spades_string = "\x1b[47m\x1b[30m\nA          \n\u2660          \n           \n     \u2660     \n           \n          \u2660\n          A"
    queen_hearts = Card("Q", "hearts")
    queen_hearts_string = "\x1b[47m\x1b[31m\nQ          \n\u2665          \n           \n     \u265B     \n           \n          \u2665\n          Q"
    ten_clubs = Card("10", "clubs")
    ten_clubs_string = "\x1b[47m\x1b[30m\n10 \u2663     \u2663  \n\u2663    \u2663      \n  \u2663     \u2663   \n            \n  \u2663     \u2663   \n     \u2663    \u2663 \n  \u2663     \u2663 10"
    # Pair cards together
    real_cards = [ace_spades, queen_hearts, ten_clubs]
    test_cards = [ace_spades_string, queen_hearts_string, ten_clubs_string]
    test_pairs = list(zip(real_cards, test_cards))

    for real_card, test_card in test_pairs:
        assert str(real_card) == test_card
