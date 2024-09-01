def generate_id(d: dict) -> int:
    """returns the last key of a dict +1"""
    if not d:
        return 1
    last_deck_id = list(d.keys())[-1]
    return last_deck_id + 1