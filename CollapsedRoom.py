from Room import Room



class CollapsedRoom(Room):

    def __init__(self,items,conditions):
        # asigns pointers to variables in game.py
            self.items = items
            self.conditions = conditions

    def move_rooms(self,room):
            # Defines rooms you can move to
            self.CHAMBER_ROOM = room

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Enter the room you woke up in.', 'Try to remove the rubble', 'Go to the next room']
    
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
    
        if 'Enter the room you woke up in.' in self.list_of_options[option-1]:
            self.location_outcome(
                 self.CHAMBER_ROOM,
                 "You enter the room you woke up in"
                 )    
    
        elif 'Try to remove the rubble' in self.list_of_options[option-1]:
            self.death_outcome(
                 "You died like a chump"
                 )
                
        elif 'Go to the next room' in self.list_of_options[option-1]:
            pass
    
