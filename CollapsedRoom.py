from Room import Room



class CollapsedRoom(Room):

    def __init__(self,items,conditions,moveroom1):
        # asigns pointers to variables in game.py
            self.items = items
            self.conditions = conditions
            self.COLLAPSED_ROOM = moveroom1

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = "PLACEHOLDER"
        self.dead:bool = False
    
    def death_storage(self):
        # Stores room conditions in case you use the death button
        pass
                    
    
    def formatter(self):
    # Formats the room description based on factors
        
    
        self.room_description:str = (f"")
                
    list_of_options:list[str] = ['Enter the room you woke up in.', 'Try to remove the rubble', 'Go to the next room']
    
    def outcome(self,option):
        # Outcome handling of chosen action
    
        if 'Put the clothes on.' in self.list_of_options[option-1]:
            pass     
    
        elif 'Press the button.' in self.list_of_options[option-1]:
            pass
                
        elif 'Press buttons on the keypad.' in self.list_of_options[option-1]:
            pass
    
        elif 'Leave the room.' in self.list_of_options[option-1]:
            pass