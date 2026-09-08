from Room import Room

class ChamberRoom(Room):

    def move_rooms(self,room):
        # Defines rooms you can move to
        self.COLLAPSED_ROOM = room

    def initializer(self):
        # Initial values for when the game is initially ran, and when you die

        self.button_press:int = 0
        self.waking:str = None
        self.button_broken:str = ""
        self.button_react:str = "You press the button. Nothing happens."
        self.new_location:"Room" = None
        self.dead:bool = False
        self.list_of_options:list[str] = ['Put the clothes on.', 'Press the button.', 'Press buttons on the keypad.','Leave the room.']

    def death_storage(self):
        # Stores room conditions in case you use the death button

        self.death_list_of_options = self.list_of_options
        self.death_button_broken = self.button_broken
        self.death_button_react = self.button_react
        self.death_button_press = self.button_press

    def death_button(self):
        # Writes death room conditions to current conditions
    
        self.list_of_options = self.death_list_of_options
        self.button_broken = self.death_button_broken
        self.button_react = self.death_button_react
        self.button_press = self.death_button_press

    def button_outcome(self,text):
        # Outcome for unique action in this room

        print(text)
        if 'died' in self.conditions:
            self.conditions.append('death_button')

        else:
            self.button_press += 1
            if self.button_press == 5:
                self.list_of_options.pop(self.chosen_option-1)

    def formatter(self):
        # Formats the room description based on factors
        
        if 'waking' in self.conditions and 'died' not in self.conditions:
            self.waking = "You wake up on a cold table in a dimly lit room, d"
            self.conditions.remove('waking')
        else:
            if 'died' and 'waking' in self.conditions:
                self.waking = "You suddenly jolt awake on the same cold table you initially woke up on, the room seems the same as before you woke up, you remove the plug in the back of your head. D"
                self.conditions.remove('waking')
            else:
                self.waking = "D"

        if self.button_press == 5:
            self.button_broken = "The button is broken, YOU broke it, are you happy now? "
        else:
            self.button_broken = ""

        if self.button_press == 4:
            self.button_react = "You press the button. Noth- Hey wait a second! Oh my god, you BROKE IT, the button is BROKEN."

        if 'died' in self.conditions:
            self.button_status = "that appears to be glowing now "
            self.button_react = "You press the button, and in an instant without even blinking you find yourself placed moments before you died, with everything you had in that moment..."
        else:
            self.button_status = ""

        if 'plug' in self.conditions:
            self.plug = "While trying to get up from the table you realize there is something attached to the back of your head, you pull it out without much resistance but are alarmed to find it went into your head, " \
            "it vaguely resembles a large audio jack. "
        else: 
            self.plug = ""

        if 'blocking_rubble' in self.conditions:
            self.door_open = "Rubble blocks the exit to the room"
            self.list_of_options.append("Put in the coordinates the computer listed.")
        else:
            self.door_open = "A door opens into a destroyed looking room in front of your table."

        self.room_description:str = (f"{self.waking}ust coats the room except for the oddly placed clothes rack in the otherwise barren room, you notice the table has a green button {self.button_status}and a keypad. {self.button_broken}{self.door_open}")

    def win_outcome(self):
        print("You plug yourself back into the machine and put the coordinates in, in an instant you find yourself on top of a hill, the horizon nothing but endless rolling fields of verdant grass, you feel peaceful.")
        self.win = True

    def outcome(self,option):
        # Outcome handling of chosen action

        if 'Put the clothes on.' in self.list_of_options[option-1]:
            self.item_outcome(
                "clothes",
                (f"{self.plug}Moving to the clothes rack you put on some of the more intact looking clothes and an old pair of shoes. "),
                True
            )
            if 'plug' in self.conditions:
                self.conditions.remove('plug')

        elif 'Press the button.' in self.list_of_options[option-1]:
            self.button_outcome(
                (f"{self.button_react}")
            )
        
        elif 'Press buttons on the keypad.' in self.list_of_options[option-1]:
            self.flavor_outcome(
                "You press some random buttons on the keypad. Nothing happens.", 
                True
            )

        elif 'Leave the room.' in self.list_of_options[option-1]:
            self.location_outcome(
                self.COLLAPSED_ROOM,
                (f"{self.plug}You walk out of the door into the next room.")
            )
            if 'plug' in self.conditions:
                self.conditions.remove('plug')

        elif 'Press buttons on the keypad.' in self.list_of_options[option-1]:
            self.win_outcome()