from dataclasses import dataclass
from skills import Skill, AbsorbingDarkness, WhirlwindPower, OutburstRage, TornadoMadness, FrenziedSpeedPotion

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
    skill=OutburstRage()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=50,
    max_endurance=27,
    attack=0.6,
    endurance=0.9,
    armor=1.6,
    skill=AbsorbingDarkness()
)

NinjaClass = UnitClass(
    name="Ниндзя",
    max_health=65,
    max_endurance=33,
    attack=0.8,
    endurance=1.0,
    armor=1.9,
    skill=TornadoMadness()
)

BullyClass = UnitClass(
    name="Громила",
    max_health=58,
    max_endurance=40,
    attack=0.5,
    endurance=0.65,
    armor=1.4,
    skill=WhirlwindPower()
)

FleshClass = UnitClass(
    name="Флеш",
    max_health=45,
    max_endurance=30,
    attack=0.8,
    endurance=0.7,
    armor=1.5,
    skill=FrenziedSpeedPotion()
)


unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    NinjaClass.name: NinjaClass,
    BullyClass.name: BullyClass,
    FleshClass.name: FleshClass
}
