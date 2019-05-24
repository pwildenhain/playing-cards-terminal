""""All global configuration options for a the Card class"""

from colorama import Fore, Back

SUIT_SYMBOL_DICT = {
    "diamonds": {"symbol": "\u2666", "style": Back.WHITE + Fore.RED},
    "hearts": {"symbol": "\u2665", "style": Back.WHITE + Fore.RED},
    "clubs": {"symbol": "\u2663", "style": Back.WHITE + Fore.BLACK},
    "spades": {"symbol": "\u2660", "style": Back.WHITE + Fore.BLACK},
}

CARD_FACE_DICT = {
    "A": {"coords": [(3, 5)]},
    "2": {"coords": [(0, 2), (6, 8)]},
    "3": {"coords": [(0, 5), (3, 5), (6, 5)]},
    "4": {"coords": [(0, 2), (0, 8), (6, 2), (6, 8)]},
    "5": {"coords": [(0, 2), (0, 8), (3, 5), (6, 2), (6, 8)]},
    "6": {"coords": [(0, 3), (3, 3), (6, 3), (0, 7), (3, 7), (6, 7)]},
    "7": {"coords": [(0, 3), (3, 3), (6, 3), (1, 5), (0, 7), (3, 7), (6, 7)]},
    "8": {"coords": [(0, 3), (3, 3), (6, 3), (1, 5), (5, 5), (0, 7), (3, 7), (6, 7)]},
    "9": {
        "coords": [
            (0, 2),
            (2, 2),
            (4, 2),
            (6, 2),
            (3, 5),
            (0, 8),
            (2, 8),
            (4, 8),
            (6, 8),
        ]
    },
    "10": {
        "coords": [
            (0, 2),
            (2, 2),
            (4, 2),
            (6, 2),
            (1, 5),
            (5, 5),
            (0, 8),
            (2, 8),
            (4, 8),
            (6, 8),
        ]
    },
    "J": {"picture": "\u2694"},
    "Q": {"picture": "\u265B"},
    "K": {"picture": "\u265A"},
}
