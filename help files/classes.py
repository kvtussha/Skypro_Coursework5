from dataclasses import dataclass
from skills import Skill

@dataclass
class UnitClass:
    name: str
    max_health: float
    max_endurance: float
    attack: float
    endurance: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=60,
    max_endurance=30,
    attack=0.8,
    endurance=0.9,
    armor=1.2,
    skill="Outburst of rage"
)

ThiefClass = UnitClass()

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}