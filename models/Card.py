class Card:
    """A card class which stores information for the user to study"""

    def __init__(self, card_id, front, back):
        self.__card_id = card_id
        self.__front = front
        self.__back = back
        # self.__rating = 0

    @property
    def card_id(self):
        return self.__card_id
    
    @property
    def front(self):
        return self.__front
    
    @front.setter
    def front(self, front):
        self.__front = front
    
    @property
    def back(self):
        return self.__back
    
    @back.setter
    def back(self, back):
        self.__back = back
    
    # @property
    # def rating(self):
    #     return self.__rating
    
    # @rating.setter
    # def rating(self, rating):
    #     if rating >= 0 and rating <= 4: 
    #         self.__rating = rating
    #     else:
    #         raise ValueError("Invalid rating, must fall between 0 and 4 inclusive")