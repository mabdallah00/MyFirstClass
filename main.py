from event import Event 

def main():
    birthday_party = Event(
        name = "Omar's Birthday Party",
        date = "11/03/2022",
        time = "6:00 PM",
        location = "Omar Parents House",
        theme = "Motorcycle and Cars"
    )


    print("=== Event Details ===")
    print(f"Event Name = {birthday_party.event_name}")
    print(f"Event Date = {birthday_party.event_date}")
    print(f"Event Time = {birthday_party.event_time}")
    print(f"Event Location = {birthday_party.event_location}")
    print(f"Event Theme = {birthday_party.event_theme}")
    print(f"Guest List: {birthday_party.guest_list}")
    print("----------------------------\n")


    birthday_party.add_guest("Maysam Abdallah")
    birthday_party.add_guest("Mohammad Maged")
    birthday_party.add_guest("Maria Rodriguez")

    print("\n--- After adding guests ---")
    birthday_party.print_event_details()
