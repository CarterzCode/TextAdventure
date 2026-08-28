"""
This is a text adventure game about finding yourself in a mysterious facility and trying to escape.
Carter Quarles - August 2026
"""

def main() -> None:
    #variable initializing/value assingment
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
    stored_values = {}
    gamerunning = True
    location: str = "Chamber"
    death_message: str = "ERROR"
    items: list[str] = []
    room_description:str = "You wake up on a cold table in a dimly lit room, dust coats the room except for the oddly placed clothes rack in the otherwise barren room, you notice the table has a green button and a keypad. A door opens into a destroyed looking room in front of your table."
    room_undescribed = True

    while gamerunning:
        #Room description printing
        if room_undescribed:
            print(room_description)
            print("")
            room_undescribed = False
    
        # Option printing
        for i in range(len(list_of_options)):
            print(f"{i+1}: {list_of_options[i]}")
        print("What do you want to do? (enter \"1\" for option 1, \"2\" for option 2 etc.)")
        choosing = True

        #Option logic/error catching
        while choosing:
            try:
                chosen_option:int = int(input())
                if chosen_option <= len(list_of_options) and chosen_option >= 1:
                    choosing = False
                else: 
                    print("Choose a valid option!")
            except ValueError:
                print("Invalid input! Try again.")


        # Outcome logic
        if 'loc' in outcomes[chosen_option-1]:
            location = outcomes[chosen_option-1][1]
        if 'item' in outcomes[chosen_option-1]:
            items.append(outcomes[chosen_option-1][1])
        
        
        # Outcome printing
        print("")
        print(outcomes[chosen_option-1][2])

        # Entry removal
        if 'remove' in outcomes[chosen_option-1]:
            list_of_options.pop(chosen_option-1)
            outcomes.pop(chosen_option-1)

        # Death logic
        if "Death" in location:
            print(death_message)
            old_location = location
            location = "Chamber"
            old_items = items
            items = []
            
        

# main guard
if __name__ == "__main__":
    main()