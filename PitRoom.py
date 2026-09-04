from Room import Room


class PitRoom(Room):
    # WELCOME TO SHOE CENTRAL!!!

    def __init__(self,items,conditions):
        self.items = items
        self.conditions = conditions

    def move_rooms(self,room,room2,room3):
        # Defines rooms you can move to
        self.COLLAPSED_ROOM = room
        self.COMPUTER_ROOM = room2
        self.TOOL_ROOM = room3

    def death_condition_outcome(self,text,condition):
        # Outcome handling for death
        self.conditions.append(condition)
        print(text)
        self.dead = True

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Cross the pit and put some random numbers into the locked door\'s keypad.', 'Cross the pit and go to the open room.','Jump into the pit.','Leave the room.']
        self.shoes_in_room:bool = False

    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options = self.list_of_options
        self.death_shoes_in_room = self.shoes_in_room

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options 
        self.shoes_in_room = self.death_shoes_in_room

    def shoe_outcome(self,text,shoe_status):
        print(text)
        self.death_shoes_in_room = shoe_status
        if shoe_status:
            self.items.remove('clothes')
        else:
            self.items.append('clothes')

    def formatter(self):
        # Formats the room description based on factors

        if 'shoe_death' in self.conditions:
             if "Take your shoes off." not in self.list_of_options:
                if not self.shoes_in_room:
                    self.list_of_options.append("Take your shoes off.")

        if self.shoes_in_room:
            if "Put your shoes on." not in self.list_of_options:
                self.list_of_options.append("Put your shoes on.")

        if self.shoes_in_room:
            self.shoes = " Your shoes are on the floor before the beam."
        else:
            self.shoes = ""

        self.room_description:str = (f"The room has a large pit in the middle of it where the floor has fallen out, you can't tell how deep the pit is. A beam precariously crosses the pit.{self.shoes}")
    

    def outcome(self,option):
        # Outcome handling of chosen action

        if 'Cross the pit and put some random numbers into the locked door\'s keypad.' in self.list_of_options[option-1]:
            if 'clothes' in self.items:
                self.death_condition_outcome(
                    "As you try to cross the pit, your worn out shoes lose grip and you slip."
                    'shoe_death'
                )
            else:
                self.death_outcome(
                    "As you smash random numbers into the keypad like a fiend, the victory of crossing that pit inflating your ego, you hear some quick mechanical whirring."
                )

        elif 'Cross the pit and go to the open room.' in self.list_of_options[option-1]:
            if 'clothes' in self.items:
                self.death_condition_outcome(
                    "As you try to cross the pit, your worn out shoes lose grip and you slip."
                    'shoe_death'
                )
            else:
                self.location_outcome(
                    self.TOOL_ROOM,
                    "You cross the pit safely and enter the open room on the other side of the room."
                )
        
        elif 'Jump into the pit.' in self.list_of_options[option-1]:
            self.death_outcome(
                "As the seconds of your fall continue, you start to reconsider that this was a good idea."
            )

        elif 'Leave the room.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.COLLAPSED_ROOM,
                "You reenter the hallway."
            )

        elif 'Put your shoes on.' in self.list_of_options[option-1]:
            self.shoe_outcome(
                "You put your shoes on.",
                False
            )
        
        elif 'Take your shoes off.' in self.list_of_options[option-1]:
            self.shoe_outcome(
                "You take your shoes off.",
                True
            )

        elif 'Cross the pit and put the note\'s numbers into the locked door\'s keypad.' in self.list_of_options[option-1]:
            if 'clothes' in self.items:
                self.death_condition_outcome(
                    "As you try to cross the pit, your worn out shoes lose grip and you slip."
                    'shoe_death'
                )
            else:
                self.location_outcome(
                    self.COMPUTER_ROOM,
                    "You cross the pit and put the paper\'s numbers into the door, causing it to open. You walk in"
                )