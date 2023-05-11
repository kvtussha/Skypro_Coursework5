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

    def skill_effect(self, skill):
        if skill.use_skill(self):
            self.target.endurance -= self.user.hp
            self.target.hp -= self.user.hp
            self.user.endurance += self.user.hp
            return "<Имя персонажа>, используя <название умения>, пробивает <название брони> " \
                   "соперника и наносит 18 очков урона."
        return skill.use_skill()

    def _is_endurance_enough(self) -> bool:
        return self.user.endurance > self.endurance

    def use_skill(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        if self._is_endurance_enough:
            return self.skill_effect(self)
        return f"{self.user.name} хотел использовать {self.name}, но у него недостаточно выносливости."


class OutburstRage(Skill):
    _name: str = "Outburst of rage: Вспышка ярости"
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
    _name = "A whirlwind of power: Вихрь силы"
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
    _name = "The Frenzied Speed Potion: Зелье бешеной скорости"
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
    _name = "Absorbing Darkness: Поглощающая тьма"
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
    _name = "Tornado Madness: Торнадо безумия"
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
