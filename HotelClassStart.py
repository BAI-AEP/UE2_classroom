# Define hotel as a class
# object's state = data fields/members
# object's behavior = methods

class Hotel:
    # Define the attributes of the class
    hotel_name = "some name"
    city = "some city"
    no_of_rooms = 0
    stars = 0
    is_available = False
    price_per_night = 0.00


# Define an empty list as the fake DB
hotel_list = []


def load_db():
    # create an object of the class Hotel
    hotel1 = Hotel()
    hotel1.hotel_name = "Hotel Aria"
    hotel1.city = "Olten"
    hotel1.stars = 4
    hotel1.no_of_rooms = 10
    hotel1.is_available = True
    hotel1.price_per_night = 100.50
    hotel_list.append(hotel1)
    print(
        f"Created hotel: Hotel name: {hotel1.hotel_name}, City: {hotel1.city}, No. of rooms: {hotel1.no_of_rooms}, Stars: {hotel1.stars}, Available: {hotel1.is_available}, Price per night: {hotel1.price_per_night}")

def show_all_hotels():
    print(f"There are {len(hotel_list)} hotel(s) in the DB.")
    for hotel in hotel_list:
        print(
            f"Hotel name: {hotel.hotel_name}, City: {hotel.city}, No. of rooms: {hotel.no_of_rooms}, Stars: {hotel.stars}, Available: {hotel.is_available}, Price per night: {hotel.price_per_night}")


# Start: Main script
load_db()
show_all_hotels()
# End: Main script
