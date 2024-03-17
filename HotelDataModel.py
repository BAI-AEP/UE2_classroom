class Hotel:
    # Define class/static variables, can be used for validation
    MIN_STARS = 0
    MAX_STARS = 5

    # Define a constructor and initialize attributes as instance variables
    def __init__(self, name, city, no_of_rooms, stars, is_available, price_per_night):
        # self.__hotel_name = name
        self.set_hotel_name(name)
        self.__city = city
        self.__no_of_rooms = no_of_rooms
        # self.__stars = stars
        self.set_stars(stars)
        self.__is_available = is_available
        self.__price_per_night = price_per_night

    # Define getter and setter methods

    def get_hotel_name(self):
        return self.__hotel_name

    def set_hotel_name(self, hotel_name):
        self.__hotel_name = hotel_name

    def get_stars(self):
        return self.__stars

    def set_stars(self, stars):
        if stars < Hotel.MIN_STARS or stars > Hotel.MAX_STARS:
            self.__stars = Hotel.MIN_STARS  # default the stars value to 0
        else:
            self.__stars = stars


# Run the following block to see how __name__ works when this class is imported in another script
# Start: Main script
# print(__name__, type(__name__))
# End: Main script