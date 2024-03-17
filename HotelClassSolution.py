# Define hotel as a class
# object's state = data fields/members
# object's behavior = methods

class Hotel:
    # Define the attributes of the class as class variables
    # hotel_name = "some name"
    # city = "some city"
    # no_of_rooms = 0
    # stars = 0
    # is_available = False
    # price_per_night = 0.00

    # Define a constructor and initialize attributes as instance variables
    def __init__(self, name, city, no_of_rooms, stars, is_available, price_per_night):
        self.hotel_name = name
        self.city = city
        self.no_of_rooms = no_of_rooms
        self.stars = stars
        self.is_available = is_available
        self.price_per_night = price_per_night


# Define an empty list as the fake DB
hotel_list = []


def load_db():
    # create an object of the class Hotel
    # hotel1 = Hotel()
    # hotel1.hotel_name = "Hotel Aria"
    # hotel1.city = "Olten"
    # hotel1.stars = 4
    # hotel1.no_of_rooms = 10
    # hotel1.is_available = True
    # hotel1.price_per_night = 100.50
    # hotel_list.append(hotel1)
    # print(
    #     f"Created hotel: Hotel name: {hotel1.hotel_name}, City: {hotel1.city}, No. of rooms: {hotel1.no_of_rooms}, Stars: {hotel1.stars}, Available: {hotel1.is_available}, Price per night: {hotel1.price_per_night}")
    #
    # hotel2 = Hotel()
    # hotel2.hotel_name = "Hotel Amaris"
    # hotel2.city = "Olten"
    # hotel2.stars = 3
    # hotel2.no_of_rooms = 10
    # hotel2.is_available = False
    # hotel2.price_per_night = 168.50
    # hotel_list.append(hotel2)
    #
    # hotel3 = Hotel()
    # hotel_list.append(hotel3)

    # Create objects using constructor
    hotel1 = Hotel("Hotel Aria", "Olten", 10, 4, True, 100.50)
    hotel_list.append(hotel1)


def show_all_hotels():
    print(f"There are {len(hotel_list)} hotel(s) in the DB.")
    for hotel in hotel_list:
        print(
            f"Hotel name: {hotel.hotel_name}, City: {hotel.city}, No. of rooms: {hotel.no_of_rooms}, Stars: {hotel.stars}, Available: {hotel.is_available}, Price per night: {hotel.price_per_night}")


# Start: Main script
load_db()
# show_all_hotels()
# Hotel.hotel_name = "Hotel Victoria"
show_all_hotels()
# End: Main script
