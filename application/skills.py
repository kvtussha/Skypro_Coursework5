from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def endurance(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    def skill_effect(self):
        self.user.endurance -= self.endurance
        self.target.hp -= self.damage
        return f"У {self.user.name} применил {self.name}"

    def _is_endurance_enough(self) -> bool:
        return self.user.endurance > self.endurance

    def use_skill(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        if self._is_endurance_enough:
            return self.skill_effect()
        return f"{self.user.name} хотел использовать {self.name}, но у него недостаточно выносливости."


class OutburstRage(Skill):
    _name: str = "Вспышка ярости"
    _endurance: float = 7
    _damage: float = 18

    @property
    def name(self) -> str:
        return self._name

    @property
    def endurance(self) -> float:
        return self._endurance

    @property
    def damage(self) -> float:
        return self._damage


class WhirlwindPower(Skill):
    _name = "Вихрь силы"
    _endurance = 5
    _damage = 12

    @property
    def name(self) -> str:
        return self._name

    @property
    def endurance(self) -> float:
        return self._endurance

    @property
    def damage(self) -> float:
        return self._damage


class FrenziedSpeedPotion(Skill):
    _name = "Зелье бешеной скорости"
    _endurance = 3
    _damage = 14

    @property
    def name(self) -> str:
        return self._name

    @property
    def endurance(self) -> float:
        return self._endurance

    @property
    def damage(self) -> float:
        return self._damage


class AbsorbingDarkness(Skill):
    _name = "Поглощающая тьма"
    _endurance = 8
    _damage = 11

    @property
    def name(self) -> str:
        return self._name

    @property
    def endurance(self) -> float:
        return self._endurance

    @property
    def damage(self) -> float:
        return self._damage


class TornadoMadness(Skill):
    _name = "Торнадо безумия"
    _endurance = 4
    _damage = 10

    @property
    def name(self) -> str:
        return self._name

    @property
    def endurance(self) -> float:
        return self._endurance

    @property
    def damage(self) -> float:
        return self._damage
