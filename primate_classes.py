"""Contains the Enclosure and various primate classes for the primate Paradise Program."""

from random import randint
from tabulate import tabulate
from playsound import playsound
from ascii import chimp_image


class Enclosure():
    """
    This class represents a parent object that contains lists of child objects as its attributes.
    The objects are stored in the respective list attribute defined as the group name of the primate.
    """

    def __init__(self):
        self.chimpanzee_list = []
        self.orangutan_list = []
        self.bonobo_list = []
        self.capuchin_list = []
        self.gorilla_list = []
        self.enclosure_list = []

    def __str__(self):
        """Returns all the members in the enclosure, in a table format."""
        header = ["Group", "Name"]
        data = []
        for primate in self.chimpanzee_list:
            data.append([primate.group, primate.name])
        for primate in self.orangutan_list:
            data.append([primate.group, primate.name])
        for primate in self.bonobo_list:
            data.append([primate.group, primate.name])
        for primate in self.capuchin_list:
            data.append([primate.group, primate.name])
        for primate in self.gorilla_list:
            data.append([primate.group, primate.name])

        return tabulate(data, header, tablefmt="rounded_grid")

    def update_enclosure_list(self):
        """Updates the enclosure list attribute with any changes made to any of the individual group list attributes"""
        self.enclosure_list = []
        self.enclosure_list += self.chimpanzee_list
        self.enclosure_list += self.orangutan_list
        self.enclosure_list += self.bonobo_list
        self.enclosure_list += self.capuchin_list
        self.enclosure_list += self.gorilla_list

    def add_primate(self, member):
        """Adds a primate to the respective primate list based on the group attribute of said primate."""
        if member.group == "Chimpanzee":
            self.chimpanzee_list.append(member)
        elif member.group == "Orangutan":
            self.orangutan_list.append(member)
        elif member.group == "Bonobo":
            self.bonobo_list.append(member)
        elif member.group == "Capuchin":
            self.capuchin_list.append(member)
        elif member.group == "Gorilla":
            self.gorilla_list.append(member)
        else:
            raise Exception("Check the group type of the member.")

    def remove_primate(self, group, primate_name):
        """Removes the primate object from its respective group list."""
        if group == "chimpanzee":
            for member in self.chimpanzee_list:
                if member.name.lower() == primate_name:
                    self.chimpanzee_list.remove(member)
        elif group == "orangutan":
            for member in self.orangutan_list:
                if member.name.lower() == primate_name:
                    self.orangutan_list.remove(member)
        elif group == "bonobo":
            for member in self.bonobo_list:
                if member.name.lower() == primate_name:
                    self.bonobo_list.remove(member)
        elif group == "capuchin":
            for member in self.capuchin_list:
                if member.name.lower() == primate_name:
                    self.capuchin_list.remove(member)
        elif group == "gorilla":
            for member in self.gorilla_list:
                if member.name.lower() == primate_name:
                    self.gorilla_list.remove(member)

    def save_members(self):
        """Writes all the members in the enclosure_list to the 'enclosure.txt' file"""
        with open("enclosure.txt", "w", encoding="UTF-8") as file:
            for primate in self.enclosure_list:
                file.write(f"{primate.group};{primate.name};{primate.age};{primate.weight};{primate.description};{primate.hungry}\n")

    def load_members(self):
        """Imports all the members in the enclosure.txt file and adds them to their respective group lists."""
        with open("enclosure.txt", "r", encoding="UTF-8") as file:
            for line in file:
                group, name, age, weight, description, hungry = line.strip().split(";")
                # For each member of the primate group this will add each object as per its group
                if group == "Chimpanzee":
                    self.add_primate(Chimpanzee(name, age, weight, description))
                elif group == "Orangutan":
                    self.add_primate(Orangutan(name, age, weight, description))
                elif group == "Bonobo":
                    self.add_primate(Bonobo(name, age, weight, description))
                elif group == "Capuchin":
                    self.add_primate(Capuchin(name, age, weight, description))
                elif group == "Gorilla":
                    self.add_primate(Gorilla(name, age, weight, description))
            self.enclosure_list = self.chimpanzee_list + self.orangutan_list + self.bonobo_list + self.capuchin_list + self.gorilla_list

    def get_group_list(self, group_name: str) -> str:
        """Returns all the members in the requested group, in a table format."""
        header = ["Group", "Name"]
        data = []
        group_name = group_name.lower()
        if group_name == "chimpanzee":
            for primate in self.chimpanzee_list:
                data.append([primate.group, primate.name])
        elif group_name == "orangutan":
            for primate in self.orangutan_list:
                data.append([primate.group, primate.name])
        elif group_name == "bonobo":
            for primate in self.bonobo_list:
                data.append([primate.group, primate.name])
        elif group_name == "capuchin":
            for primate in self.capuchin_list:
                data.append([primate.group, primate.name])
        elif group_name == "gorilla":
            for primate in self.gorilla_list:
                data.append([primate.group, primate.name])
        else:
            raise Exception("Invalid group type selected.")

        return tabulate(data, header, tablefmt="rounded_grid")

    def get_groups_in_enclosure(self) -> list:
        """Returns a list of all the groups in the enclosure."""
        groups_in_enclosure = []
        for primate in self.enclosure_list:
            if primate.group.lower() not in groups_in_enclosure:
                groups_in_enclosure.append(primate.group.lower())
        return groups_in_enclosure

    def get_names_in_group(self, group: str):
        """Returns a list of the primate names for a specified group."""
        if group == "all":
            # Returns all the primate names in the enclosure
            names_in_enclosure = []
            for primate in self.enclosure_list:
                names_in_enclosure.append(primate.name.lower())
            return names_in_enclosure
        else:
            # Returns all the primate names for a specified group
            names_in_group = []
            for primate in self.enclosure_list:
                if group == primate.group.lower():
                    names_in_group.append(primate.name.lower())

            if not names_in_group:
                raise Exception("Invalid group type selected.")
            else:
                return names_in_group

    def get_primate(self, group: str, name: str) -> object:
        """
        Returns primate object given the group name and primate name.
        Raises Exception error if invalid group is given.
        """
        if group == "chimpanzee":
            for primate in self.chimpanzee_list:
                if primate.name.lower() == name:
                    return primate
        elif group == "orangutan":
            for primate in self.orangutan_list:
                if primate.name.lower() == name:
                    return primate
        elif group == "bonobo":
            for primate in self.bonobo_list:
                if primate.name.lower() == name:
                    return primate
        elif group == "capuchin":
            for primate in self.capuchin_list:
                if primate.name.lower() == name:
                    return primate
        elif group == "gorilla":
            for primate in self.gorilla_list:
                if primate.name.lower() == name:
                    return primate
        else:
            raise Exception("Invalid group type selected.")

    def set_name(self, group: str, primate_name: str, new_name: str):
        """Changes the name of the primate given a new name"""
        if group == "chimpanzee":
            for member in self.chimpanzee_list:
                if member.name.lower() == primate_name:
                    member.name = new_name
        elif group == "orangutan":
            for member in self.orangutan_list:
                if member.name.lower() == primate_name:
                    member.name = new_name
        elif group == "bonobo":
            for member in self.bonobo_list:
                if member.name.lower() == primate_name:
                    member.name = new_name
        elif group == "capuchin":
            for member in self.capuchin_list:
                if member.name.lower() == primate_name:
                    member.name = new_name
        elif group == "gorilla":
            for member in self.gorilla_list:
                if member.name.lower() == primate_name:
                    member.name = new_name

    def set_age(self, group: str, primate_name: str, new_age: int):
        """Changes the name of the primate given a new name"""
        if group == "chimpanzee":
            for member in self.chimpanzee_list:
                if member.name.lower() == primate_name:
                    member.age = new_age
        elif group == "orangutan":
            for member in self.orangutan_list:
                if member.name.lower() == primate_name:
                    member.age = new_age
        elif group == "bonobo":
            for member in self.bonobo_list:
                if member.name.lower() == primate_name:
                    member.age = new_age
        elif group == "capuchin":
            for member in self.capuchin_list:
                if member.name.lower() == primate_name:
                    member.age = new_age
        elif group == "gorilla":
            for member in self.gorilla_list:
                if member.name.lower() == primate_name:
                    member.age = new_age

    def set_weight(self, group: str, primate_name: str, new_weight: int):
        """Changes the name of the primate given a new name"""
        if group == "chimpanzee":
            for member in self.chimpanzee_list:
                if member.name.lower() == primate_name:
                    member.weight = new_weight
        elif group == "orangutan":
            for member in self.orangutan_list:
                if member.name.lower() == primate_name:
                    member.weight = new_weight
        elif group == "bonobo":
            for member in self.bonobo_list:
                if member.name.lower() == primate_name:
                    member.weight = new_weight
        elif group == "capuchin":
            for member in self.capuchin_list:
                if member.name.lower() == primate_name:
                    member.weight = new_weight
        elif group == "gorilla":
            for member in self.gorilla_list:
                if member.name.lower() == primate_name:
                    member.weight = new_weight

    def set_desc(self, group: str, primate_name: str, new_desc: str):
        """Changes the name of the primate given a new name"""
        if group == "chimpanzee":
            for member in self.chimpanzee_list:
                if member.name.lower() == primate_name:
                    member.description = new_desc
        elif group == "orangutan":
            for member in self.orangutan_list:
                if member.name.lower() == primate_name:
                    member.description = new_desc
        elif group == "bonobo":
            for member in self.bonobo_list:
                if member.name.lower() == primate_name:
                    member.description = new_desc
        elif group == "capuchin":
            for member in self.capuchin_list:
                if member.name.lower() == primate_name:
                    member.description = new_desc
        elif group == "gorilla":
            for member in self.gorilla_list:
                if member.name.lower() == primate_name:
                    member.description = new_desc

class Primate():

    def __init__(self, name: str, age: int, weight: int, description: str, group: str, hungry=True):
        self.group = group
        self.name = name
        self.age = age
        self.weight = weight
        self.description = description
        self.hungry = hungry

    def __str__(self):
        return f"Group: \t\t{self.group}\nName: \t\t{self.name}\nAge: \t\t{self.age}\nWeight: \t{self.weight}\nDescription: \t{self.description}\nHungry: \t{self.hungry}\n"

    def get_description(self) -> str:
        """Returns a description of the primate."""
        return(f"\n{self.name} is a {self.age} year old, {self.weight}kg {self.group}. \n{self.description}\n")

    def feed_primate(self, food) -> str:
        """Sets the 'hungry' attribute to false and returns a string response."""
        food = food.lower()
        self.hungry = False
        return f"{self.name} ate the {food}.\n"

    def wave(self) -> str:
        """Returns a string response."""
        return f"You waved at {self.name}.\n{self.name} waved back!\n"

    def take_photo(self) -> str:
        """Returns a string response."""
        return f"You took a photo of {self.name}.\n"

class Chimpanzee(Primate):

    scientific_name = "Pan troglodytes"
    population = "172,700 to 299,700"
    endangered_level = "Endangered"
    habitat = "Forests (moist and dry forests), Savannah Woodlands, and Grassland-Forest mosaics"
    fact = "Chimpanzees can live to be 50 years old in the wild."
    easter_egg = "Saves the photo to a zoo_photo.txt file"

    def __init__(self, name, age, weight, description, group="Chimpanzee", hungry=True):
        super().__init__(name, age, weight, description, hungry)
        self.group = group

    def display_group_info(self) -> str:
        """Returns a description of the primate."""
        return f"Scientific Name: \t{self.scientific_name}\nPopulation: \t\t{self.population}\nEndangered Level: \t{self.endangered_level}\nHabitat: \t\t{self.habitat}\nFun Fact: \t\t{self.fact}\n"

    def take_photo(self) -> str:
        """Writes a picture fo the zoo_photo.txt file and returns a string response."""
        with open("zoo_photo.txt", "w", encoding="utf-8") as file:
            file.write(f"Here is your photo of {self.name} at primate Paradise:\n")
            file.write(chimp_image)
        return "You took a photo! Take a look at it in the zoo_photo.txt file.\n"

class Orangutan(Primate):

    scientific_name = "Pongo abelii, Pongo pygmaeus"
    population = "About 104,700 (Bornean), 13,846 (Sumatran), 800 (Tapanuli)"
    endangered_level = "Critically Endangered"
    habitat = "Orangutans are found only in the rain forests of the Southeast Asian islands of Borneo and Sumatra."
    fact = "Orangutans are the heaviest tree-dwelling animal. They can weigh up to 200 pounds (~90kg)."
    easter_egg = "If they are hungry, they'll steals your phone when you try to take a picture. They will return it for a banana."

    def __init__(self, name, age, weight, description, group="Orangutan", hungry=True, has_camera=False):
        super().__init__(name, age, weight, description, hungry)
        self.group = group
        self.has_camera = has_camera

    
    def display_group_info(self) -> str:
        """Returns a description of the primate."""
        return f"Scientific Name: \t{self.scientific_name}\nPopulation: \t\t{self.population}\nEndangered Level: \t{self.endangered_level}\nHabitat: \t\t{self.habitat}\nFun Fact: \t\t{self.fact}\n"

    def take_photo(self) -> str:
        """Returns a string response depending on the value of self.hungry."""
        if self.hungry:
            if not self.has_camera:
                self.has_camera = True
                return f"OH NO! {self.name} grabbed your camera!\nTry feeding {self.name} a banana in exchange for your phone.\n"
            else:
                return f"You can't take a photo because {self.name} has your camera.\nTry feeding {self.name} a banana in exchange for your phone.\n"
        else:
            return super().take_photo()

    def feed_primate(self, food) -> str:
        """Returns a string response depending on the item of food given."""
        food = food.lower()
        if self.has_camera:
            if food == "banana":
                self.has_camera = False
                self.hungry = False
                return f"{self.name} loves {food}s.\n{self.name} gave back your camera.\n"
            else:
                return f"{self.name} ate the {food} but didn't give your phone back.\nTry feeding {self.name} something else."
        else:
            return super().feed_primate(food)

class Bonobo(Primate):

    scientific_name = "Pan paniscus"
    population = "10,000 to 50,000"
    endangered_level = "Endangered"
    habitat = "Bonobos live in the rainforests of the Congo Basin in Africa."
    fact = "Bonobos and chimpanzees both share 98.7% of their DNA with humans—making the two species our closest living relatives."
    easter_egg = "Displays a random reaction when you wave at them."

    def __init__(self, name, age, weight, description, group="Bonobo", hungry=True):
        super().__init__(name, age, weight, description, hungry)
        self.group = group

    def display_group_info(self) -> str:
        """Returns a description of the primate."""
        return f"Scientific Name: \t{self.scientific_name}\nPopulation: \t\t{self.population}\nEndangered Level: \t{self.endangered_level}\nHabitat: \t\t{self.habitat}\nFun Fact: \t\t{self.fact}\n"

    def wave(self) -> str:
        """Returns a random string response."""
        action = ["smiled back", "waved back", "did a happy dance", "tapped on the glass",  "walked away"]
        index = randint(0,(len(action)-1))
        return f"You waved at {self.name}.\n{self.name} {action[index]}.\n"

class Capuchin(Primate):

    scientific_name = "Cebus Capucinus"
    population = "Last estimate was 54,000 in 2007"
    endangered_level = "Vulnreable"
    habitat = "The White Faced Capuchins live in forest and rainforests of Central America and Northern South America"
    fact = "The White Faced Capuchin lives between 15-20 years in the wild, but can live up to 45 years in captivity."
    easter_egg = "Picky with their food - they really like dates."

    def __init__(self, name, age, weight, description, group="Capuchin", hungry=True):
        super().__init__(name, age, weight, description, hungry)
        self.group = group

    def display_group_info(self) -> str:
        """Returns a description of the primate."""
        return f"Scientific Name: \t{self.scientific_name}\nPopulation: \t\t{self.population}\nEndangered Level: \t{self.endangered_level}\nHabitat: \t\t{self.habitat}\nFun Fact: \t\t{self.fact}\n"

    def feed_primate(self, food) -> str:
        """Returns a string response depending on the item of food given."""
        food = food.lower()
        if food == "date":
            self.hungry = False
            return f"You fed {self.name} a {food}.\n{self.name} loves {food}s.\n"
        else:
            return f"{self.name} doesn't like {food}s.\n{self.name} threw the {food} back at you!\n"

class Gorilla(Primate):

    scientific_name = "Gorilla gorilla and Gorilla beringei"
    population = "250,000 - 300,000"
    endangered_level = "Endangered"
    habitat = "Gorillas typically live in the lowland tropical rainforests of Central Africa."
    fact = "To intimidate rivals, male gorillas strut with stiff legs, beat their chests, and use vocalisations like roars or hoots."
    easter_egg = "Beats their chest or lets out a roar when you wave at them."

    def __init__(self, name, age, weight, description, group="Gorilla", hungry=True):
        super().__init__(name, age, weight, description, hungry)
        self.group = group

    def display_group_info(self) -> str:
        """Returns a description of the primate."""
        return f"Scientific Name: \t{self.scientific_name}\nPopulation: \t\t{self.population}\nEndangered Level: \t{self.endangered_level}\nHabitat: \t\t{self.habitat}\nFun Fact: \t\t{self.fact}\n"

    def wave(self) -> str:
        """Returns, at random, a string response and/or plays a sound."""
        action = ["let out a ROAR!", "beat his chest!", "waved back.", "tapped on the glass.",  "walked away."]
        index = randint(0,(len(action)-1))
        print(f"You waved at {self.name}.")
        if index == 0:
            playsound("sound_effects/gorilla_roar.mp3")
        elif index == 1:
            playsound("sound_effects/beating_chest.wav")
        else:
            pass
        return f"{self.name} {action[index]}\n"
