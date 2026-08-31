"""
This is a text adventure game about finding yourself in a mysterious facility and trying to escape.
Carter Quarles - August 2026
"""

def main() -> None:
    '''
    # old garbo
    list_of_options: list[str] = ['Put the clothes on.', 'Press the button.', 'Press buttons on the keypad.','Leave the room.']
    outcomes: list[list[str]] = [
         ["item",
          "clothes",
          "While trying to get up from the table you realize there is something attached to the back of your head, you pull it out without much resistance but are alarmed to find it went into your head, it vaguely resembles a large audio jack. Moving to the clothes rack you put on some of the more intact looking clothes and an old pair of shoes. ",
          "remove"],

          ["N/A","N/A","You press the button. Nothing happens.",],

          ["N/a","N/A","You press some random buttons on the keypad. Nothing happens.","remove"],

          ["loc","Collapsed Room",""]
    ]
    
    
    death_message: str = "ERROR"
    room_description:str = "You wake up on a cold table in a dimly lit room, dust coats the room except for the oddly placed clothes rack in the otherwise barren room, you notice the table has a green button and a keypad. A door opens into a destroyed looking room in front of your table."
    '''

    location: str = "chamber_room"
    conditions: list[str] = []
    items: list[str] = []


    def chamber_room() :
        while location == "chamber_room":
            room_options: list = []
            room_description: list = []

            if "button_broken" in conditions:
                button_status = "The button is broken, YOU broke it, are you happy now?"

            if "standing" in conditions:
                standing = "D"
            else:
                standing = "You wake up on a cold table in a dimly lit room, d"

            if 'clothes' not in items:
                room_options.append('Put the clothes on.')

            if "button_broken" not in conditions:
                room_options.append('Press the button.')

            if 'chamber_room3' not in conditions:
                room_options.append('Press buttons on the keypad.')

            room_options.append('Leave the room.')

            room_description = (f"{standing}ust coats the room and the room is empty besides the table and a clothes rack, the table has a green button and a keypad. {button_status} A door opens into a destroyed looking room in front of your table.")

            room(
                room_description,

                room_options,

                [
                ["item",
                "clothes",
                "While trying to get up from the table you realize there is something attached to the back of your head, you pull it out without much resistance but are alarmed to find it went into your head, it vaguely resembles a large audio jack. Moving to the clothes rack you put on some of the more intact looking clothes and an old pair of shoes. ",
                "remove",
                "condition",
                "plugfalse"],
                
                ["flavor",
                 "You press the button. Nothing happens.",
                 "buttoncount"],
                
                ["flavor",
                 "You press some random buttons on the keypad. Nothing happens.",
                 "condition",
                 "keypadpressed"],
                
                ["location",
                 "Collapsed Room",
                 "",
                 "condition",
                 "standing"]
                ]

                )

    def collapsed_room() :
        pass
    
    def hidden_room() :
        pass
    
    def pit_room() :
        pass
    
    def tool_room() :
        pass

    def computer_room() :
        pass

    # Room Logic
    def room(Roomdesc,Options) :
        # Description and options
        print(Roomdesc)
        print()
        for i in range(len(Options)):
            print(f"{i+1}: {Options[i]}")
        print("What do you want to do? (enter \"1\" for option 1, \"2\" for option 2 etc.)")

        # Choosing logic
        choosing = True
        while choosing:
            try:
                chosen_option:int = int(input())
                if chosen_option <= len(Options) and chosen_option >= 1:
                    choosing = False
                else: 
                    print("Choose a valid option!")
            except ValueError:
                print("Invalid input! Try again.")

        # Outcome logic


    chamber_room()

# main guard
if __name__ == "__main__":
    main()