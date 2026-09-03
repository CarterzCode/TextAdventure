class Room():


    # Base structure for rooms
    new_location:"Room" = "PLACEHOLDER"
    chosen_option:int
    list_of_options:list[str]
    dead:bool = False

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

        self.items.append(item)
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