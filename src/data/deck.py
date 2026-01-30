import random
import json
import os

# Load cards from JSON
json_path = os.path.join(os.path.dirname(__file__), "cards.json")

with open(json_path, "r", encoding="utf-8") as f:
    CARDS = json.load(f)

# Fool + Jester are special
FOOL_JESTER = {"Fool", "Jester"}


def draw_card(discarded=None):
    """
    OFFICIAL RULES:
    - All cards return to the deck (duplicates allowed)
    - Fool + Jester are removed after being drawn once per session
    """

    if discarded is None:
        discarded = set()

    # Remove Fool/Jester if already drawn
    available = [c for c in CARDS if c["name"] not in discarded]

    if not available:
        raise ValueError("No cards available (Fool/Jester already drawn).")

    card = random.choice(available)

    # If Fool or Jester → discard for session
    if card["name"] in FOOL_JESTER:
        discarded.add(card["name"])

    return card
