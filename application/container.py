from unit import BaseUnit
from base import Arena
from classes import unit_classes
from equipment import Equipment

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

arena = Arena()
equipment = Equipment()
armors = Equipment().get_armors_names()
weapons = Equipment().get_weapons_names()

creating_units = {
    "armors": armors,
    "weapons": weapons,
    "classes": unit_classes
}
