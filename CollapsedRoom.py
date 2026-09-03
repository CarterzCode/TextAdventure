from Room import Room

class CollapsedRoom(Room):
    def initializer(self):
        self.new_location:"Room" = "PLACEHOLDER"
        self.dead:bool = False
    
    def death_storage(self):
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