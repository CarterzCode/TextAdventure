from Room import Room

class ComputerRoom(Room):
    # Variables unique to the room

    def __init__(self,items,conditions):
        self.items = items
        self.conditions = conditions

    def move_rooms(self,room):
        # Defines rooms you can move to
        self.PIT_ROOM = room

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Put the clothes on.', 'Press the button.', 'Press buttons on the keypad.','Leave the room.']

    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options = self.list_of_options

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options 

    def formatter(self):
        # Formats the room description based on factors

        self.room_description:str = (f"")
    

    def outcome(self,option):
        # Outcome handling of chosen action

        if 'A' in self.list_of_options[option-1]:
            pass

        elif 'C' in self.list_of_options[option-1]:
            pass
        
        elif 'D' in self.list_of_options[option-1]:
            pass

        elif 'Leave the room.' in self.list_of_options[option-1]:
            pass