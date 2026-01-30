import random

cards = [
    ("Sun", "You gain 50,000 XP and a wondrous magic item."),
    ("Void", "Your soul is trapped in an object somewhere."),
    ("Moon", "You are granted 1d3 wishes.")
]

def draw_card():
    """Returns one random card from the deck."""
    return random.choice(cards)
