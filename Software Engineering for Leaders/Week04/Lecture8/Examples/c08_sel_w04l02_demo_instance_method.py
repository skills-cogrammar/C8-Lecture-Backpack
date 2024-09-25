# What makes up classes? Our Pseudocode
"""
# Attributes
size - small, medium or large
colour - white, blue, red 
number of rooms - 2 - 10
type of flooring - hardwood, carpet or tile
"""

"""
# Methods
opening doors - open a door in house
turning on lights - this will turn on lights in house
cleaning - clean the house
"""

"""
Objects will be referred to as instances, these would be the different houses 
of the blueprints provided.
"""


class HousePlan:
    """
    This Python class initialises a house object with specified attributes and 
    includes methods for opening the door, turning on the light, and cleaning 
    with a robotic vacuum.
    
    :param unit_size: The size of the house. This could be the total 
    area of the house, the number of square feet/meters, or any other measurement 
    that indicates the physical size of the house.
    
    :param u_colour: The colour of the house. It is used to initialise
    the `colour` attribute of an instance of this class.
    
    :param u_num_rooms: The number of rooms in a house or a building. 
    It is used to initialise the `num_rooms` attribute of an object of this class
    
    :param u_floor: The floor type of a building or house where the object 
    is located. It is used to initialise the `floor` attribute of the object 
    with the value passed to it when an instance of the class is declared.
    """
    def __init__(self, unit_size, unit_colour, unit_num_rooms, unit_floor):
        # Below we find instance attributes since each instance will have its 
        # own set of values.
        self.size = unit_size
        self.colour = unit_colour
        self.num_rooms = unit_num_rooms
        self.floor = unit_floor

    # The methods open_door, light_switch, and rumba_clean are all instance methods 
    # because they are associated with a specific object (house instance) and 
    # can be called to perform actions related to that object.
    def open_door(self):
        """
        The function `openDoor` prints a message indicating that the door has been opened.
        """
        print("The door has been opened.")

    def light_switch(self):
        """
        The function `lightSwitch` prints a message indicating that the light has been turned on.
        """
        # NOTE: we can add conditional to check light status
        print("Light has been turned on.")

    def rumba_clean(self):
        """
        The function `RumbaClean` prints a message indicating that the house has been cleaned by
        Eufy-chan.
        """
        print("Eufy-chan has claimed that the house has been cleaned.")


# Gather preferences for a house. Each `input` function prompts the user with 
# a question and waits for the user to enter a response. 
house_size = input("What size house would you prefer (small, medium, large): ")
house_colour = input("What colour would you like the house in ? (blue, red, white): ")
house_num_rooms = int(input("How many rooms would you prefer (enter an integer value) : "))
house_flooring = input("What type of flooring would you like ? (wood, tile, carpet): ")

#Create instance kitt_house of the `HousePlan` class.
kitt_house = HousePlan(house_size, house_colour, house_num_rooms, house_flooring)
#Create instance kola_house of the `HousePlan` class.
kola_house = HousePlan("large", "green", 4, "tile")

# Format and display information about the `kitt_house` instance of the `HousePlan` class. Here's a breakdown of what it does:
print("\n=========== Specification for the Kitt House ===========")
line = "=" * 25
print(f"""
    Size: {kitt_house.size}
    Colour: {kitt_house.colour}
    Number of rooms: {kitt_house.num_rooms}
    Type of flooring: {kitt_house.floor}
    \n{line}""")

kitt_house.open_door()
print(f"\n{line}")
kitt_house.light_switch()
print(f"\n{line}")
kitt_house.rumba_clean()
print(f"\n{line}")
