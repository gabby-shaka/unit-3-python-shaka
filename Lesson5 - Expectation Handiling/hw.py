# 3. 
def get_phone_number():
    contacts = {"Lisa": "555-6234", "Jess": "552-4465", "Harini": "432-9087"}
    print(get_phone_number(contacts, "Lisa")) # "555-6234"
    print(get_phone_number(contacts, "Boss")) # "Contact not found"
    print(get_phone_number(contacts, "Harini")) # "432-9087"
    
# 4.
def get_song():
    playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
    print(get_song(playlist,2)) # "Song C"
    print(get_song(playlist,20)) # "Position out of range"
    print(get_song(playlist, "first")) # "Position must be an integer."
    
# 5.
def calculate_test_average():
    print(calculate_test_average([88, 92, 76, 95, 84])) # 87
    print(calculate_test_average([78.5, 92.0, 85.5])) # 85.33
    print(calculate_test_average([])) # 0 
    