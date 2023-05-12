from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Equipment, Weapon, Armor
from classes import UnitClass
from typing import Optional


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.endurance = unit_class.endurance
        self.weapon = Equipment().get_weapon("")
        self.armor = Equipment().get_armor("")
        self._is_skill_used = False

    @property
    def health_points(self) -> float:
        return round(self.hp, 1)

    @property
    def endurance_points(self) -> float:
        return round(self.endurance, 1)

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit) -> int | float:
        self.endurance -= self.weapon.endurance_per_hit * self.unit_class.endurance
        damage = self.weapon.damage * self.unit_class.attack
        if target.endurance > target.armor.endurance_per_turn * target.unit_class.endurance:
            target.endurance -= target.armor.endurance_per_turn * target.unit_class.endurance
            damage -= target.armor.defence * target.unit_class.armor
        return target.get_damage(damage)

    def get_damage(self, damage: int) -> Optional[int | float]:
        if damage > 0:
            self.hp -= damage
            return round(damage, 1)
    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """
        Этот метод будет переопределен ниже
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        if self._is_skill_used:
            return "Навык уже использован."
        self._is_skill_used = True
        return self.unit_class.skill.use_skill(user=self, target=target)


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        if self.endurance > self.weapon.endurance_per_hit * self.unit_class.endurance:
            damage = self._count_damage(target)
            if damage:
                return f"{self.name}, используя {self.weapon.name} пробивает {target.armor.name} соперника " \
                       f"и наносит {damage} урона."
            return f"{self.name}, используя {self.weapon.name} наносит удар, но {target.armor.name} " \
                   f"соперника его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        if self.endurance > self.weapon.endurance_per_hit * self.unit_class.endurance:
            damage = self._count_damage(target)
            if damage:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника " \
                       f"и наносит {damage} урона."
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} " \
                   f"соперника его останавливает."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
