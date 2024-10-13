class Deck:
    def __init__(self, deck_id, name):
        self.__deck_id = deck_id
        self.__name = name
        self.__cards = {}

    @property
    def id(self):
        return self.__deck_id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cards(self):
        return self.__cards
    
    @cards.setter
    def cards(self, value):
        self.__cards = value

    def __len__(self):
        return len(self.__cards)
    
    def __repr__(self):
        return f"Deck({self.name}, {len(self)})"
    
    def __str__(self):
        return f"Deck containing {len(self)} card{'(s)' if len(self) > 1 else ''}"