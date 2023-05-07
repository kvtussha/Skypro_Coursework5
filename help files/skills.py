from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit

#ПОМЕНЯТЬ skill_effect
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

    @abstractmethod
    def skill_effect(self, skill: Skill()) -> str:
        pass

    def _is_endurance_enough(self) -> bool:
        return self.user.endurance > self.endurance

    def use_skill(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Для вызова скилла везде используем просто use_skill
        """
        self.user = user
        self.target = target
        if self._is_endurance_enough:
            return self.skill_effect()
        return f"{self.user.name} хотел использовать {self.name}, но у него недостаточно выносливости."


class Outburst_of_rage(Skill):
    name = "Outburst of rage: Вспышка ярости"
    endurance = 7
    damage = 18
    skill = Skill()
    def skill_effect(self, skill):
        if skill.use_skill(self):
            self.target.endurance -= self.user.hp
            self.target.hp -= self.user.hp
            self.user.endurance += self.user.hp
            return "<Имя персонажа>, используя <название скилла>, пробивает <название брони> " \
                   "соперника и наносит 18 очков урона."
        return skill.use_skill()


class Whirlwind_of_power(Skill):
    name = "A whirlwind of power: Вихрь силы"
    endurance = 5
    damage = 12

    def skill_effect(self, skill):
        if skill.use_skill(self):
            self.target.endurance -= self.user.hp
            self.target.hp -= self.user.hp
            self.user.endurance += self.user.hp
            return "<Имя персонажа>, используя <название скилла>, пробивает <название брони> " \
                   "соперника и наносит 18 очков урона."
        return skill.use_skill()


class Frenzied_Speed_Potion(Skill):
    name = "The Frenzied Speed Potion: Зелье бешеной скорости"
    endurance = 3
    damage = 14

    def skill_effect(self, skill):
        if skill.use_skill(self):
            self.target.endurance -= self.user.hp
            self.target.hp -= self.user.hp
            self.user.endurance += self.user.hp
            return "<Имя персонажа>, используя <название скилла>, пробивает <название брони> " \
                   "соперника и наносит 18 очков урона."
        return skill.use_skill()


class Absorbing_Darkness(Skill):
    name = "Absorbing Darkness: Поглощающая тьма"
    endurance = 8
    damage = 11

    def skill_effect(self, skill):
        if skill.use_skill(self):
            self.target.endurance -= self.user.hp
            self.target.hp -= self.user.hp
            self.user.endurance += self.user.hp
            return "<Имя персонажа>, используя <название скилла>, пробивает <название брони> " \
                   "соперника и наносит 18 очков урона."
        return skill.use_skill()


class Tornado_Madness(Skill):
    name = "Tornado Madness: Торнадо безумия"
    endurance = 4
    damage = 10

    def skill_effect(self, skill):
        if skill.use_skill(self):
            self.target.endurance -= self.user.hp
            self.target.hp -= self.user.hp
            self.user.endurance += self.user.hp
            return "<Имя персонажа>, используя <название скилла>, пробивает <название брони> " \
                   "соперника и наносит 18 очков урона."
        return skill.use_skill()

