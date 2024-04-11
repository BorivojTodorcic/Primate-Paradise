"""
Zoo Administration Program

This program provides a lively and instructive environment for guests to engage with
virtual primates, while learning new and fascinating information about them.

Features:
- Virtual Enclosures: Explore various virtual enclosures housing different species of primates.
- Interactive Engagement: Guests can interact with the virtual primates by feeding, waving 
  or taking a picture with them.
- Educational Content: Learn interesting facts about each primate species, including their
  scientific name, habitat, population size and conservation status.
- Administration Tools: Staff can manage the virtual zoo by adding, updating or removing primates
  from the enclosures.

This program aims to simulate the experience of visiting a real zoo, providing entertainment,
education, and a deeper understanding of the diverse world of primates.
"""


from functools import reduce
from tabulate import tabulate
from primate_classes import Enclosure, Chimpanzee, Orangutan, Bonobo, Capuchin, Gorilla
from menu_options import staff_menu, update, menu, actions, enclosures, school, food


def create_table(item_list: list, header: str) -> str:
    """Returns a single column table given a list of items and a header"""
    header = ["", header]
    data = []
    for i, item in enumerate(item_list, start=1):
        data.append([i, item.capitalize()])

    return tabulate(data, header, tablefmt="rounded_grid")

def req_group() -> str:
    """Requests user input for a group name, returns a validated name."""
    while True:
        group = input("What group does the primate belong to?\n> ")
        # Handles group names not available in the zoo.
        if group.lower() not in ["chimpanzee", "orangutan", "bonobo", "capuchin", "gorilla"]:
            print("Invalid group.")
            continue
        else:
            return group

def req_name() -> str:
    """Requests user input for a primate name, returns a validated name."""
    while True:
        new_name = input("What is the name of the primate ?\n> ")
        # Handles non alphabetical input
        if reduce(lambda x, y: x and (y.isalpha() or y.isspace()), new_name, True):
            return new_name
        else:
            print("The name must only contain alphabetical characters.")
            continue

def req_age() -> int:
    """Requests user input for a primate age, returns a validated age."""
    while True:
        age = input("How old is the primate?\n> ")
        # Handles non-numerical input and negative numbers
        if age.isnumeric():
            age = int(age)
            # Handles ages over 60
            if age > 60:
                print("The age of the primate must be less than 60.")
                continue
            else:
                return age
        else:
            print("The age must be a valid number.")
            continue

def req_weight() -> int:
    """Requests user input for a primate weight, returns a validated weight."""
    while True:
        weight = input("How much does the primate weigh in kg?\n> ")
        # Handles non-numerical input and negative numbers
        if weight.isnumeric():
            weight = int(weight)
            # Handles weight less than 1kg and over 200kg
            if weight <=1 or weight > 200:
                print("The weight of the primate must be more than 1kg or less than 200kg.")
                continue
            else:
                return weight
        else:
            print("The weight must be a valid integer.")
            continue

def req_desc() -> str:
    """Requests user input for a primate description, returns a description string."""
    while True:
        description = input("Provide a brief description of the primate\n> ")
        desc_correct = input("Would you like to keep this description? (y/n)\n>")
        # Gives the option to amend the description
        if desc_correct.lower() == "y":
            return description
        else:
            continue

def req_number(total: int) -> int:
    """Returns a validated user selected primate number as per the primate group table."""
    while True:
        number = input("Enter a primate number (enter 0 to go back):\n> ")
        # Handles non-numerical input and negative numbers
        if number.isnumeric():
            number = int(number)
            # Ensures input is within range
            if number > total:
                print("Number out of range.\n")
                continue
            else:
                return number
        else:
            print("Invalid option.\n")
            continue

def request_member_details(get_group=req_group, get_name=req_name, get_age=req_age, get_weight=req_weight, get_desc=req_desc) -> list:
    """
    Requests user input in order to create an instance of the respective primate class.
    Returns the validated primate details as a list.
    """

    while True:
        group = get_group()
        name = get_name()
        age = get_age()
        weight = get_weight()
        description = get_desc()

        # Checks if user is satisfied that all the details are correct before returning the list
        table = [["NEW PRIMATE", ""],["Group:", group],["Name:", name],["Age:", age], ["Weight:", weight],["Description:", description]]
        print(tabulate(table, headers="firstrow", tablefmt="rounded_grid"))
        confirm = input("Are these details correct? (y/n)\n>")

        if confirm.lower() == "y":
            return [group, name, age, weight, description]
        elif confirm.lower() == "n":
            print("\n== Please enter the details again. ==\n")
            continue
        else:
            print("\n== Please select a valid option. ==\n")
            continue

def add_new_member(member_details: list):
    """
    Enter validated primate details as a list to create a new instance of the respective primate group.
    Updates the self.enclosure_list and saves the members to the enclosure.txt file.
    """
    # Identifies the primate group from the validated list
    group = member_details[0].lower()

    # Generates a new instance of the primate based on its group identification
    if group == "chimpanzee":
        new_member = Chimpanzee(member_details[1], member_details[2], member_details[3], member_details[4])
    elif group == "orangutan":
        new_member = Orangutan(member_details[1], member_details[2], member_details[3], member_details[4])
    elif group == "bonobo":
        new_member = Bonobo(member_details[1], member_details[2], member_details[3], member_details[4])
    elif group == "capuchin":
        new_member = Capuchin(member_details[1], member_details[2], member_details[3], member_details[4])
    elif group == "gorilla":
        new_member = Gorilla(member_details[1], member_details[2], member_details[3], member_details[4])

    # Adds the new member to the enclosure and saves to the enclosure.txt file
    enclosure.add_primate(new_member)
    enclosure.update_enclosure_list()
    enclosure.save_members()
    print(f"{new_member.name.capitalize()} has been added to the {new_member.group} enclosure!")

def select_primate(get_group, get_names, make_table) -> list:
    """Selects a primate object from the enclosure and returns a validated group_name and primate_name."""
    while True:
        # Generates a table of the primates in the enclosure
        group_list = get_group()
        print(enclosure)

        # Requests user input for the primate group
        group_name = input("\nTo select a primate, enter their group name ('b' to go back).\n> ")
        group_name = group_name.lower()

        # Checks if the user has entered a valid group option
        if group_name in group_list:
            while True:
                # Generates a table of the names of primates in the selected group at the enclosure
                names_list = get_names(group_name)
                print()
                print(make_table(names_list, f"{group_name.capitalize()}s in the enclosure:"), end="\n")

                primate_name = input("\nEnter the name of the primate ('b' to go back).\n> ")
                primate_name = primate_name.lower()

                # Checks if the user has entered a valid name option
                if primate_name in names_list:
                    return [group_name, primate_name]
                elif primate_name == "b":
                    break
                else:
                    print("Please enter a valid name.\n")
                    continue
        elif group_name == "b":
            break
        else:
            print("Please enter a valid group.\n")
            continue

def remove_primate(chosen_group: str, chosen_name: str):
    """Removes a primate from its respective enclosure list and updates the enclosure_list instance and enclosure.txt"""
    while True:
        confirm = input(f"Are you sure you want to remove {chosen_name}? (y/n)\n >")
        if confirm.lower() == "y":
            enclosure.remove_primate(chosen_group, chosen_name)
            print(f"{chosen_name} has been removed from the enclosure.")
            # Removes the primate from self.enclosure_list and updates enclosure.txt
            enclosure.update_enclosure_list()
            enclosure.save_members()
            break
        elif confirm.lower() == "n":
            break
        else:
            print("Please enter a valid option.\n")
            continue

def login() -> str:
    """Asks the user to confirm login details (Staff or visitor) and returns 's' or 'v'."""
    while True:
        # Asks the user for a password if they log in as a member of staff
        selection = input("Are you staff or a visitor? (s/v): \n> ")
        if selection.lower() == "s":
            password = input("What is the password?: ")
            if password == "banana":
                print("Welcome back!")
                return "s"
            else:
                print("Incorrect password.\n")
                continue
        elif selection == "v":
            print("Welcome to the primate Paradise")
            return "v"
        else:
            print("Please select a valid option.")
            continue

def enter_enclosure(current_group: str, get_number):
    """Displays a menu for the user to allow them to interact with the selected primate group"""
    while True:
        # Prints a list of primate names in the current primate group as a table
        names_list = enclosure.get_names_in_group(current_group)
        print(create_table(names_list, f"{current_group.capitalize()}s"))

        # Counts the number of members in the group
        total_primates = len(names_list)

        # Requests a number from the user from the primate table
        primate_number = get_number(total_primates)

        if primate_number == 0:
            break

        else:
            # Gets the primate name from the table as per the selected number
            primate_name = names_list[primate_number-1]
            # Retrieves the primate object from the respective primate group list
            active_primate = enclosure.get_primate(current_group, primate_name)
            interact_with_primate(actions, food, active_primate)

def interact_with_primate(action_list: str, food_list: str, primate: object):
    """Allows the user to interact with the primate object given the available menu items"""
    
    # Displays information about the active primate
    print(primate.get_description())

    while True:

        # Displays action list and requests user input
        action = input(action_list)

        # Calls to the wave behaviour
        if action == "1":
            print(f"\n{primate.wave()}")
        # Calls to the feed_primate behaviour
        elif action == "2":
            food_letter = input(food_list)
            print()
            if food_letter.lower() == "a":
                print(primate.feed_primate("apple"))
            elif food_letter.lower() == "b":
                print(primate.feed_primate("banana"))
            elif food_letter.lower() == "c":
                print(primate.feed_primate("cucumber"))
            elif food_letter.lower() == "d":
                print(primate.feed_primate("date"))
            elif food_letter.lower() == "0":
                continue
            else:
                print("Invalid option.")
        # Calls the the take_photo behaviour
        elif action == "3":
            print(f"\n{primate.take_photo()}")
        elif action == "0":
            break
        else:
            print("Invalid Option.")

def display_group_attr(group):
    """Prints the group attributes for the respective group by taking in the group class"""
    print(f"Scientific name: {group.scientific_name}")
    print(f"Population: {group.population}")
    print(f"Status: {group.endangered_level}")
    print(f"Fun fact: {group.fact}")
    print(f"Easter Egg: {group.easter_egg}\n")

def main():

    if current_user == "s":
        # === Loops through the staff menu === #
        while True:
            menu_selection = input(staff_menu)
            if menu_selection == "1":
                print("=== View primates in the enclosure ===\n")
                print(enclosure)

            elif menu_selection == "2":
                print("=== Add a primates to the enclosure ===\n")
                new_primate = request_member_details()
                add_new_member(new_primate)

            elif menu_selection == "3":
                print("=== Remove a primates from the enclosure ===\n")
                primate = select_primate(enclosure.get_groups_in_enclosure, enclosure.get_names_in_group, create_table)

                if primate is not None:
                    group = primate[0]
                    name = primate[1]
                    remove_primate(group, name)

            elif menu_selection == "4":
                print("=== Update primate details ===\n")

                # Loops through the update menu
                while True:
                    print("Please select the primate you would like to update:\n")
                    primate = select_primate(enclosure.get_groups_in_enclosure, enclosure.get_names_in_group, create_table)

                    if primate is not None:
                        group = primate[0]
                        name = primate[1]

                        update_selection = input(update)

                        if update_selection == "1":
                            new_name = req_name()
                            enclosure.set_name(group, name, new_name)

                        elif update_selection == "2":
                            new_age = req_age()
                            enclosure.set_age(group, name, new_age)

                        elif update_selection == "3":
                            new_weight = req_weight()
                            enclosure.set_weight(group, name, new_weight)

                        elif update_selection == "4":
                            new_desc = req_desc()
                            enclosure.set_desc(group, name, new_desc)

                        elif update_selection == "0":
                            break

                        else:
                            print("Please select a valid option\n")

                        enclosure.update_enclosure_list()
                        enclosure.save_members()

                    else:
                        break

            elif menu_selection == "0":
                print("Thank you for visiting primate Paradise!")
                break
            else:
                print("Please select a valid option\n")

    elif current_user == "v":
        # === Loops through the visitor menu === #
        while True:
            menu_selection = input(menu)
            if menu_selection == "1":

                # Allows the user to enter the enclosure and interact with the selected primate objects
                while True:

                    enclosure_selection = input(enclosures)

                    if enclosure_selection == "1":
                        print("\n=== Visiting Crafty Chimpanzees ===\n")
                        active_group = "chimpanzee"
                        enter_enclosure(current_group=active_group, get_number=req_number)

                    elif enclosure_selection == "2":
                        print("\n=== Visiting Outrageous Orangutans ===\n")
                        active_group = "orangutan"
                        enter_enclosure(current_group=active_group, get_number=req_number)

                    elif enclosure_selection == "3":
                        print("\n=== Visiting Beautiful Bonobos ===\n")
                        active_group = "bonobo"
                        enter_enclosure(current_group=active_group, get_number=req_number)

                    elif enclosure_selection == "4":
                        print("\n=== Visiting Cheeky Capuchins ===\n")
                        active_group = "capuchin"
                        enter_enclosure(current_group=active_group, get_number=req_number)

                    elif enclosure_selection == "5":
                        print("\n=== Visiting Grizzly Gorillas ===\n")
                        active_group = "gorilla"
                        enter_enclosure(current_group=active_group, get_number=req_number)

                    elif enclosure_selection == "0":
                        break

                    else:
                        print("Please select a valid option")

            elif menu_selection == "2":

                # Displays the class attributes for the respective primate classes
                while True:

                    school_selection = input(school)

                    if school_selection == "1":
                        print("\n=== Chimpanzees ===\n")
                        display_group_attr(Chimpanzee)

                    elif school_selection == "2":
                        print("\n=== Orangutans ===\n")
                        display_group_attr(Orangutan)

                    elif school_selection == "3":
                        print("\n=== Bonobos ===\n")
                        display_group_attr(Bonobo)

                    elif school_selection == "4":
                        print("\n=== Capuchins ===\n")
                        display_group_attr(Capuchin)

                    elif school_selection == "5":
                        print("\n=== Gorillas ===\n")
                        display_group_attr(Gorilla)

                    elif school_selection == "0":
                        break

                    else:
                        print("Please select a valid option")

            elif menu_selection == "0":
                print("Thank you for visiting primate Paradise!")
                break
            else:
                print("Please select a valid option")

current_user = login()
enclosure = Enclosure()
enclosure.load_members()

if __name__ == "__main__":
    main()
