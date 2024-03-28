def hotel():
    menu = input("""
                 Welcome to the hotel!
                 
                 Menu:
                 
                 1. Book a room
                 2. Check out of a room
                 3. Display the status of all rooms
                 
                 Please enter a selection: """)
    
    if menu == "1":
        book_room()
    elif menu == "2":
        check_out()
    elif menu == "3":
        display_status()
    else:
        print("Sorry, that's not a valid selection. Please try again.")
        
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room():
    booking = input("Which room would you like to book? ")
    if booking == "101":
        if hotel_rooms[booking]["status"] == "booked":
            print(f"Sorry, Room {booking} is already booked by {hotel_rooms[booking]["customer"]}.")
        else:
            name = input("Please enter your name: ")
            hotel_rooms[booking]["customer"] = name
            print(f"Room {booking} has been successfully booked by {name}.")
    elif booking == "102":
        if hotel_rooms[booking]["status"] == "booked":
            print(f"Sorry, Room {booking} is already booked by {hotel_rooms[booking]["customer"]}.")
        else:
            name = input("Please enter your name: ")
            hotel_rooms[booking]["customer"] = name
            hotel_rooms[booking]["status"] = "booked"
            print(f"Room {booking} has been successfully booked by {name}.")
    else:
        print("Sorry, that's not a valid room number.")

def check_out():
    leave = input("Which room would you like to check out of? ")
    if leave == "101":
        if hotel_rooms[leave]["status"] == "available":
            print(f"Sorry, Room {leave} is already unoccupied.")
        else:
            hotel_rooms[leave]["customer"] = " "
            hotel_rooms[leave]["status"] = "available"
            print(f"Room {leave} is now unoccupied.")
    elif leave == "102":
        if hotel_rooms[leave]["status"] == "available":
            print(f"Sorry, Room {leave} is already unoccupied.")
        else:
            hotel_rooms[leave]["customer"] = " "
            hotel_rooms[leave]["status"] = "available"
            print(f"Room {leave} is now unoccupied.")
    else:
        print("Sorry, that's not a valid room number.")

def display_status():
    print(f"Room 101 is {hotel_rooms["101"]["status"]}")
    print(f"Room 102 is {hotel_rooms["102"]["status"]}")

hotel()