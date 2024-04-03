from datetime import datetime

events = []

def main():
    print("\n=============== Event Scheduler App ===============")
    while True:
        print("\nSelect an option: \n")

        print("1. Create Event.")
        print("2. View Events.")
        print("3. Delete Event.")
        print("4. Search Event.")
        print("5. Edit Event.")
        print("6. Exit.")

        choice = input("Option: ")

        if choice == "1":
            create_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            search_event()
        elif choice == "5":
            edit_event()
        elif choice == "6":
            print("\nExiting Event Scheduler. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter a valid option")

        
def create_event():
    title = input("\nEnter event title: ").title()
    description = input("Enter event description: ")

    while True:
        try:
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
            print(f'\n--- Event "{title}" created successfully! ---')
            break
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            continue

    event = {
        "title": title,
        "description": description,
        "date": date,
        "time": time
    }

    events.append(event)



def view_events():
    print("-------------------- Events --------------------\n")

    if not events:
        print("No Events Available.\n")
    else:
        sorted_events = sorted(events, key=lambda x: (x["date"], x["time"]), reverse=True)

        for event in sorted_events:
     
            print(f"Title: {event['title']}")
            print(f"Description: {event['description']}")
            print(f"Date: {event['date']}")
            print(f"Time: {event['time']}\n")

    print("------------------------------------------------")


def delete_event():
    title = input("\nEnter the name of the event you want to delete: ").title()
    event_found = False

    for event in events:
        if event["title"] == title:
            events.remove(event)
            event_found = True
            print(f'\n--- Event "{title}" deleted succefully! ---')
            break
    if not event_found:
        print(f'\nEvent "{title}" Not Found')



def search_event():
    matching_events = []
    query = input("\nEnter search keyword or date (YYYY-MM-DD): ")

    for event in events:
        if query.lower() in event["title"].lower() or query.lower() in event["description"].lower() or query == event["date"]:
            matching_events.append(event)
    
    print("\n---------------- Matching Events ----------------\n")

    if not matching_events:
        print("No Matching Event Found")
    else:
        for event in matching_events:
            print_event_details(event)

    print("\n-------------------------------------------------")



def edit_event():
    title = input("\nEnter the title of the event you want to edit: ").title()
    event_found = False

    for event in events:
        if event["title"] == title:
            print("\n---------- Current Event Details ----------\n")
            print_event_details(event)
            print("--------- Enter New Event Details ---------\n")
            event["title"] = input("New title: ").title()
            event["description"] = input("New description: ")

            while True:
                try:
                    event["date"] = input("New date (YYYY-MM-DD): ")
                    event["time"] = input("New time (HH:MM): ")
                    
                    datetime.strptime(event["date"], "%Y-%m-%d")
                    datetime.strptime(event["time"], "%H:%M")
                    break
                except ValueError:
                    print("\nInvalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.\n")
                    continue

            print(f'\n---- Event "{event["title"]}" updated succefully! ----')
            event_found = True
            break
    if not event_found:
        print(f'\nEvent "{title}" Not Found')


def print_event_details(event):
    print(f"Title: {event['title']}")
    print(f"Description: {event['description']}")
    print(f"Date: {event['date']}")
    print(f"Time: {event['time']}\n")



if __name__ == "__main__":
    main()

