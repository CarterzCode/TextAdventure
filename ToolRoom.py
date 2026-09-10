from Room import Room

class ToolRoom(Room):

    def move_rooms(self,room: "Room"):
        # Defines rooms you can move to
        self.PIT_ROOM = room

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Reenter the pit room.', 'Take the screwdriver.']

    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options = self.list_of_options

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options 

    def formatter(self):
        # Formats the room description based on factors
        if 'screwdriver' in self.items:
            self.screwdriver_in_room = ""
        else:
            self.screwdriver_in_room = " You notice a screwdriver that could be useful."


        self.room_description:str = (f"The room smells of oil, and is filled with tables covered in tools whose purpose eludes you. {self.screwdriver_in_room}")
    

    def outcome(self,option: int):
        # Outcome handling of chosen action, option is for chosen option

        if 'Reenter the pit room.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.PIT_ROOM,
                "You reenter the pit room and cross the beam."
            )

        elif 'Take the screwdriver.' in self.list_of_options[option-1]:
            self.item_outcome(
                'screwdriver',
                "You pick up the screwdriver.",
                True
            )
