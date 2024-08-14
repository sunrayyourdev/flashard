class Card:
    def __init__(self, id, front, back) -> None:
        self.__id = id
        self.__front = front
        self.__back = back

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_front(self):
        return self.__front
    
    def set_front(self, front):
        self.__front = front
    
    def get_back(self):
        return self.__back
    
    def set_back(self, back):
        self.__back = back


if __name__ == "__main__":
    pass # write tests