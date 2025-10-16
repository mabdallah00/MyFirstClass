+-----------------------+
|        Controller     |
+-----------------------+
| - EventController     |
| + create_event()      |
| + list_events()       |
+-----------------------+

+-----------------------+
|        Model          |
+-----------------------+
| - Event               |
| - PartyEvent          |
+-----------------------+
| + display_summary()   |
| + print_properties()  |
+-----------------------+

+-----------------------+
|        View           |
+-----------------------+
| - HTML Templates      |
| - CLI Print Output    |
+-----------------------+
| + show_event_details()|
+-----------------------+
