class Event:
    def __init__(self, name, date, time, location, theme):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.theme = theme 
        self.guest_list = []


    def get_event_details(self):
        print(f"Event: {self.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Location: {self.location}")
        print(f"Theme: {self.theme}")
        print("\nGuest List:")
        if self.guest_list:
            for guest in self.guest_list:
                print(f" - {guest}")
            else:
                print("No guests have been added yet.")
            print("--------------------")
              

    def update_location(self, new_location):
        self.location = new_location
        return f"Location updated to {self.location}"
    

    def add_guest(self, guest_name):
        self.guest_lost.append(guest_name)
        print(f"Guest '{guest_name}' has been added to the guest list.")
