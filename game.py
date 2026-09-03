"""
This is a text adventure game about finding yourself in a mysterious facility and trying to escape.
Carter Quarles - September 2026
"""
from ChamberRoom import ChamberRoom
from CollapsedRoom import CollapsedRoom
 

def main() -> None:
    
    items: list[str] = []
    conditions: list[str] = ['waking','plug']
    
    COLLAPSED_ROOM = CollapsedRoom(items,conditions,"OBAMA")
    CHAMBER_ROOM = ChamberRoom(items,conditions,COLLAPSED_ROOM)

    current_location = CHAMBER_ROOM
    ROOMS:list = [CHAMBER_ROOM]

    for room in ROOMS: 
        # Initializes the rooms
        room.initializer()

    def magic_button():
        # Puts death values on all rooms
        for room in ROOMS:
            room.death_button()

    # Game running logic
    gamerunning = True
    while gamerunning:
        # Runs the game with function calls

        current_location.room_print()
        current_location.input()

        if current_location.new_location != "PLACEHOLDER":
            current_location = current_location.new_location

        if current_location.dead:
            # Handles death
            conditions.append('waking')
            if 'died' not in conditions:
                conditions.append('died')
            for room in ROOMS:
                room.death_storage()
                room.initializer()
            death_location = current_location
            death_items:list[str] = items
            current_location = CHAMBER_ROOM

        if 'death_button' in conditions:
            # Runs magic button and does some other death related stuff
            magic_button()
            current_location = death_location
            items = death_items
            conditions.remove('death_button')
   

# main guard
if __name__ == "__main__":
    main()