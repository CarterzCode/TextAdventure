from Room import Room

class VentRoom(Room):

    def move_rooms(self,room,room2):
        # Defines rooms you can move to
        self.HIDDEN_ROOM = room
        self.CHAMBER_ROOM = room2

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Reenter the hidden room.', 'Exit where you feel the vent blowing.']

    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options = self.list_of_options

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options 

    def formatter(self):
        # Formats the room description based on factors
        if 'escape_coords' in self.items:
            if 'Enter the room you woke up in.' not in self.list_of_options:
                self.list_of_options.append('Enter the room you woke up in.')


        self.room_description:str = (f"The vent is dark and you have to feel your way around, exploring the vent you find a vent leading to the room you woke up in, and a cover that air appears to be flowing to from the vent network.")

    def win_outcome(self):
        print("You kick the covering off and climb out of the vent, the smell of the outdoors hits you as you look around at the rich greens of a forest.")
        self.win = True

    def outcome(self,option):
        # Outcome handling of chosen action

        if 'Reenter the hidden room.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.HIDDEN_ROOM,
                "You crawl out of the vent back into the hidden room."
            )

        elif 'Exit where you feel the vent blowing.' in self.list_of_options[option-1]:
            self.win_outcome()
        
        elif 'Enter the room you woke up in.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.CHAMBER_ROOM,
                "You kick the vent off and climb in, the vent is too high up for you to climb back in."
            )

        