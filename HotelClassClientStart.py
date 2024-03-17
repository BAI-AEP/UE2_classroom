from HotelClass import Hotel

# Define an empty list as the fake DB
hotel_list = []


def load_db():
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
show_all_hotels()
# End: Main script