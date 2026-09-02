"""
This is a text adventure game about finding yourself in a mysterious facility and trying to escape.
Carter Quarles - September 2026
"""

def main() -> None:
    
    items: list[str] = []
    conditions: list[str] = ["waking"]
    
    class Room():
        # Base structure for rooms

        def room_print(self):
            # Runs formatter to format the printed info, and lists options

            self.formatter()
            print()
            print(self.room_description)
            counter:int = 1
            for option in self.list_of_options:
                print(f"{counter}: {option}")
                counter += 1

        def input(self):
            # Takes the option input and passes it to outcome

            print("What do you want to do? (enter \"1\" for option 1, \"2\" for option 2 etc.)")
            choosing = True
            while choosing:
                    try:
                        self.chosen_option = int(input())
                        if self.chosen_option <= len(self.list_of_options) and self.chosen_option >= 1:
                            choosing = False
                        else: 
                            print("Choose a valid option!")
                    except ValueError:
                        print("Invalid input! Try again.")
            self.outcome(self.chosen_option)

        def outcome(self,option):
            # Placeholder for children classes

            pass

        def item_outcome(self,item,text,remove):
            # Outcome handling for items

            items.append(item)
            print(text)
            if remove:
                self.list_of_options.pop(self.chosen_option-1)

        def location_outcome(self,location,text,remove):
            # Outcome handling for locations

            self.new_location = location
            print(text)
            if remove:                    
                self.list_of_options.pop(self.chosen_option-1)

        def death_outcome(self,text):
            # Outcome handling for death

            print(text)
            self.dead = True

        def flavor_outcome(self,text,remove):
            # Outcome handling for non-impactful outcomes

            print(text)
            if remove:
                self.list_of_options.pop(self.chosen_option-1)

        def formatter(self):
            # Placeholder for children classes

            pass

        # Variable defining to manage scope 
        new_location:"Room" = "PLACEHOLDER"
        chosen_option:int
        list_of_options:list[str]
        dead:bool = False

    class ChamberRoom(Room):
        # Variables unique to the room

        def initializer(self):
            self.button_press:int = 0
            self.waking:str = "ERROR"
            self.button_broken:str = ""
            self.button_react:str = "You press the button. Nothing happens."

        def death_storage(self):
            self.death_list_of_options = self.list_of_options
            self.death_button_broken = self.button_broken
            self.death_button_react = self.button_react

        def death_button(self):
            self.list_of_options = self.death_list_of_options
            self.button_broken = self.death_button_broken
            self.button_react = self.death_button_react


        def button_outcome(self,text):
            # Outcome for unique action in this room

            print(text)
            self.button_press += 1
            if self.button_press == 5:
                self.list_of_options.pop(self.chosen_option-1)

        def formatter(self):
            # Formats the room description based on factors
            
            if 'waking' in conditions:
                self.waking = "You wake up on a cold table in a dimly lit room, d"
                conditions.remove("waking")
            else:
                self.waking = "D"

            if self.button_press == 5:
                self.button_broken = "The button is broken, YOU broke it, are you happy now?"
            else:
                self.button_broken = ""

            if self.button_press == 4:
                self.button_react = "You press the button. Noth- Hey wait a second! Oh my god, you BROKE IT, the button is BROKEN."
            
            self.room_description:str = (f"{self.waking}ust coats the room except for the oddly placed clothes rack in the otherwise barren room, you notice the table has a green button and a keypad. {self.button_broken} A door opens into a destroyed looking room in front of your table.")
        
        list_of_options:list[str] = ['Put the clothes on.', 'Press the button.', 'Press buttons on the keypad.','Leave the room.']

        def outcome(self,option):
            # Outcome handling of chosen action

            if 'Put the clothes on.' in self.list_of_options[option-1]:
                self.item_outcome(
                    "clothes",
                    "While trying to get up from the table you realize there is something attached to the back of your head, you pull it out without much resistance but are alarmed to find it went into your head, it vaguely resembles a large audio jack. Moving to the clothes rack you put on some of the more intact looking clothes and an old pair of shoes. ",
                    True
                )

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
                    COLLAPSED_ROOM,
                    "Goobidy gab gab",
                    False
                )

    class CollapsedRoom(Room):
        pass

    COLLAPSED_ROOM = CollapsedRoom()
    CHAMBER_ROOM = ChamberRoom()

    current_location = CHAMBER_ROOM
    ROOMS:list[Room] = [CHAMBER_ROOM]

    for room in ROOMS: 
        

    # Game running logic
    gamerunning = True
    while gamerunning:
        current_location.room_print()
        current_location.input()
        if current_location.new_location != "PLACEHOLDER":
            current_location = current_location.new_location
        if current_location.dead:
            gamerunning = False

   

# main guard
if __name__ == "__main__":
    main()