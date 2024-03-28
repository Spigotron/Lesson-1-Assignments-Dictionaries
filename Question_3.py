service_tickets = {
    "1": {"Customer": "Alice", "Issue": "Login problem", "Status": "Open"},
    "2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "Closed"}
}

def service_ticket_program():
    menu = input("""
                 Welcome to the customer service ticket program!
                 
                 Menu:
                 
                 1. Open a new ticket
                 2. Update the status of an existing ticket
                 3. Display all tickets (or filter by status)
                 
                 Please enter a selection: """)
    
    if menu == "1":
        open_new_ticket()
    elif menu == "2":
        update_ticket()
    elif menu == "3":
        display_tickets()
    else:
        print("Sorry, that's not a valid selection. Please try again.")

def open_new_ticket():
    name_input = input("Please enter the customer's first name. ")
    issue_input = input("Please briefly describe the issue. ")
    ticket_id = str(len(service_tickets) + 1)
    service_tickets[ticket_id] = {"Customer": name_input, "Issue": issue_input, "Status": "Open"}
    print("You have successfully opened a new ticket.")

def update_ticket():
    keys = service_tickets.keys()
    update_input = input("Which ticket's status would you like to update? ")
    if update_input in keys:
        status_input = input("Would you like to open the ticket or close the ticket? ")
        if status_input == "open":
            service_tickets[update_input]["Status"] = "Open"
            print(f"You have successfully opened Ticket {update_input}.")
        elif status_input == "close":
            service_tickets[update_input]["Status"] = "Closed"
            print(f"You have successfully closed Ticket {update_input}.")
        else:
            print("Sorry, that's not a valid option. Please try again.")
    else:
        print("Sorry, that's not a valid ticket number. Please try again.")

def display_tickets():
    display_input = input("Press 1 to view all tickets. Press 2 to filter by status. ")
    if display_input == "1":
        print(service_tickets)
    elif display_input == "2":
        choice_input = input("Press 1 to view all open tickets. Press 2 to view all closed tickets. ")
        if choice_input == "1":
            for key in service_tickets.keys():
                if service_tickets[key]["Status"] == "Open":
                    print(service_tickets[key])
        elif choice_input == "2":
            for key in service_tickets.keys():
                if service_tickets[key]["Status"] == "Closed":
                    print(service_tickets[key])
    else:
        print("Sorry, that's not a valid input. Please try again.")

service_ticket_program()