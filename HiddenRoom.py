from Room import Room

class HiddenRoom(Room):

    def __init__(self,items,conditions):
        self.items = items
        self.conditions = conditions

    def move_rooms(self,room,room2):
        # Defines rooms you can move to
        self.COLLAPSED_ROOM = room
        self.VENT_ROOM = room2

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Look through the papers.', 'Leave the room.']

    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options = self.list_of_options

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options 

    def formatter(self):
        # Formats the room description based on factors
        if 'screwdriver' in self.items and 'computer_seen' in self.conditions:
            if 'Take replacement parts from the computer.' not in self.list_of_options:
                self.list_of_options.append('Take replacement parts from the computer.')
                

        self.room_description:str = (f"The room is dim and has tables covered in papers lining the walls. A computer sits dormant in one corner and refuses to turn on at all.")

    def paper_outcome(self,text,remove):
        print(text)
        self.list_of_options.append("Skim through the long technical paper.")
        self.list_of_options.append("Grab the note.")
        if remove:
            self.list_of_options.pop(self.chosen_option-1)

    def outcome(self,option):
        # Outcome handling of chosen action

        if 'Look through the papers.' in self.list_of_options[option-1]:
            self.paper_outcome(
                "You skim through the papers, finding most of them to be boring technical papers, you find an unlabled note with some numbers and a long technical paper that seems marginally interesting.",
                True
            )

        elif 'Leave the room.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.COLLAPSED_ROOM,
                "You reenter the hallway."
            )
        
        elif 'Grab the note.' in self.list_of_options[option-1]:
            self.item_outcome(
                'code_note',
                "You grab the note with the numbers.",
                True
            )

        elif 'Skim through the long technical paper.' in self.list_of_options[option-1]:
            self.flavor_outcome(
                "You start to skim through the paper, finding most of it uninteresting, eventually you find something that seems relevant, \"-it has become apparent that there are an infinite number of universes, hence there is an infinite amount of versions of our universe at all points along its course. This technology will allow the transfer of a consciousness to any of these universes along any point in its course-\" the rest doesn't seem relevant.",
                True
            )

        elif 'Take replacement parts from the computer' in self.list_of_options[option-1]:
            self.item_outcome(
                'replacement_part',
                "You open the computer with your screwdrier and find the replacement part.",
                True
            )