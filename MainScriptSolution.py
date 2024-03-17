from HotelDataModel import Hotel
from SearchManager import SearchHotelManager

# Define an empty list as the fake DB
hotel_list = []


def load_db():
    # Create objects using constructor
    hotel1 = Hotel("Hotel Aria", "Olten", 10, 4, True, 100.50)
    global hotel_list
    hotel_list.append(hotel1)
    print("Database loaded...")


def show_menu():
    print("Menu: ")
    print("Print 0 to search hotels based on your criteria")
    print("Print 1 to manage your user account")
    print("Print 2 login as a registered user or an admin")
    print("Print x to quit the hotel reservation system")


def navigate():
    choice = input("Choose an option for your desired action: ")
    match choice:
        case 'x':
            print("Goodbye, see you soon!")
            exit(0)
        case '0':
            print("Entering the Search module...")
            # call functions in SearchManager
            search_manager = SearchHotelManager()
            location = input("Enter the location you are looking for: ")
            search_manager.search_hotels_by_location(location)
        case '1':
            print("Entering the User Account module...")
            # call functions in UserAccountManager
        case '2':
            print("Accept username and password")
            # call functions in LoginManager
        case _:
            print("No such option, please enter a valid choice as shown in the Menu")


# Start: Main script
print(__name__)
if __name__ == '__main__':
    load_db()
    show_menu()
    navigate()
# End: Main script