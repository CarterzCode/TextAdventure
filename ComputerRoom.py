from Room import Room

class ComputerRoom(Room):

    def move_rooms(self,room: "Room"):
        # Defines rooms you can move to
        self.PIT_ROOM = room

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Reenter the pit room.', 'Try to turn the computer on.']
        self.computer_working: bool = False


    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options: list[str] = self.list_of_options
        self.death_computer_working: bool = self.computer_working

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options 
        self.computer_working = self.death_computer_working

    def computer_outcome(self,text: str):
        # Handles fixing the computer
        print(text)
        self.computer_working = True
        self.list_of_options.pop(self.chosen_option-1)

    def formatter(self):
        # Formats the room description based on factors
        if 'blocking_rubble' not in self.conditions:
            self.conditions.append('blocking_rubble')

        if self.computer_working:
            self.computer_status: str = "whirring"
        else:
            self.computer_status: str = "dormant"

        if 'replacement_part' in self.items:
            if 'Replace the broken part.' not in self.list_of_options and not self.computer_working:
                self.list_of_options.append('Replace the broken part.')

        self.room_description:str = (f"The room is dominated by a large {self.computer_status} computer, the air is stagnant and full of dust.")
    

    def outcome(self,option: int):
        # Outcome handling of chosen action, option is for the chosen option

        if 'Reenter the pit room.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.PIT_ROOM,
                "You reenter the pit room and cross the beam."
            )

        elif 'Try to turn the computer on.' in self.list_of_options[option-1]:
            if self.computer_working:
                self.item_outcome(
                    'escape_coords',
                    "The computer whirs to life, you look through some of the documents and find a seemingly relevant one that outlines coordinates for what looks like the table you woke up on.",
                    True
                )
            else:

                self.flavor_outcome(
                    "You try to turn the computer on, it turns on for a few seconds, displaying an error about a certain part, and then turns off.",
                    False
                )
                if 'computer_seen' not in self.conditions:
                    self.conditions.append('computer_seen')

        elif 'Replace the broken part.' in self.list_of_options[option-1]:
            self.computer_outcome(
                "You open up the computer with your screwdriver and replace the broken part without too much difficulty."
            )

