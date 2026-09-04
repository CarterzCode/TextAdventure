from Room import Room



class CollapsedRoom(Room):

    def __init__(self,items,conditions):
        # asigns pointers to variables in game.py
            self.items = items
            self.conditions = conditions

    def death_outcome(self,text,condition):
            # Outcome handling for death
            self.conditions.append(condition)
            print(text)
            self.dead = True

    def move_rooms(self,room,room2,room3):
            # Defines rooms you can move to
            self.CHAMBER_ROOM = room
            self.HIDDEN_ROOM = room2
            self.PIT_ROOM = room3
            


    def initializer(self):
        # Initial values for when the game is initially ran, and when you die
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Enter the room you woke up in.', 'Try to remove the rubble.', 'Go to the next room.']
    
    def death_storage(self):
        # Stores room conditions in case you use the death button
        self.death_list_of_options = self.list_of_options

    def death_button(self):
        # Writes death room conditions to current conditions
        self.list_of_options = self.death_list_of_options   
    
    def formatter(self):
    # Formats the room description based on factors
        if 'entering' in self.conditions:
            self.entering = "As you enter the room, the smell of sulfur hits your nose, the room is covered in burn marks, seemingly recent. "
            self.conditions.remove('entering')
        else:
            self.entering = ""

        if 'rubble_death' in self.conditions:
            self.rubble_status =  "you notice the pieces of rubble that fell on you while trying to move it, and think you could more safely remove the rubble."
        else:
             self.rubble_status = "you think you could remove the rubble if you tried."
    
        self.room_description:str = (f"{self.entering}The room seems to be a T-junction in a hallway, the path forward is clear, but the side path is blocked by rubble, {self.rubble_status}")
                
    def rubble_outcome(self,text,remove):
        print(text)
        self.list_of_options.append('Enter the door hidden behind the rubble.')
        if remove:
            self.list_of_options.pop(self.chosen_option-1)
    
    def outcome(self,option):
        # Outcome handling of chosen action
    
        if 'Enter the room you woke up in.' in self.list_of_options[option-1]:
            self.location_outcome(
                 self.CHAMBER_ROOM,
                 "You enter the room you woke up in"
                 )    
    
        elif 'Try to remove the rubble.' in self.list_of_options[option-1]:
            if 'clothes' not in self.items and 'glass_death' not in self.conditions:
                self.death_outcome(
                    "As you step into the room, glass lodges itself in your feet, causing you to slip on more glass.",
                    'glass_death'
                    )

            elif 'rubble_death' not in self.conditions:
                self.death_outcome(
                    "As you try to remove the rubble, pieces lodged higher up fall on you and hit your head.",
                    'rubble_death'
                    )

            else:
                self.rubble_outcome(
                    "Paying closer attention to the rubble, you manage to avoid sustaining any injuries while clearing it, revealing a door.",
                    True
                    )
                
        elif 'Go to the next room.' in self.list_of_options[option-1]:
            pass

        elif 'Enter the door hidden behind the rubble.' in self.list_of_options[option-1]:
            self.location_outcome(
                 self.HIDDEN_ROOM,
                 "You enter the room hidden behind the now removed rubble."
            )
