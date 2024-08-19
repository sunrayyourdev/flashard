class Card:

    def __init__(self, card_id, front, back):
        self.__card_id = card_id
        self.__front = front
        self.__back = back
        self.__rating = 0

    def get_card_id(self):
        return self.__card_id
    
    def get_front(self):
        return self.__front
    
    def set_front(self, front):
        self.__front = front
    
    def get_back(self):
        return self.__back
    
    def set_back(self, back):
        self.__back = back
    
    def get_rating(self):
        return self.__rating
    
    def set_rating(self, rating):
        if rating >= 0 and rating <= 4: 
            self.__rating = rating
        else:
            raise ValueError("Invalid rating, must fall between 0 and 4 inclusive")