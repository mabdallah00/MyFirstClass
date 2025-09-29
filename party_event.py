from event import Event
from interfaces import Printable

class PartyEvent(Event, Printable):
    def __init__(self, name, date, time, location, theme, guest_list):
        super().__init__(name, date, time, location, theme, guest_list)
        self.guest_list = guest_list

    def printProperties(self):
        print("=== Party Event Properties ===")
        for prop, value in vars(self).items():
            print(f"{prop}: {value}")
