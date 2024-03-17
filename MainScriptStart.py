from HotelDataModel import Hotel

# Define an empty list as the fake DB
hotel_list = []


def load_db():
    # Create objects using constructor
    hotel1 = Hotel("Hotel Aria", "Olten", 10, 4, True, 100.50)
    hotel_list.append(hotel1)


def show_menu():
    pass


def navigate():
    pass


# Start: Main script
load_db()
# End: Main script
