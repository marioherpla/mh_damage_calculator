from mh_damage.calculator.build import Build
from mh_damage.calculator.skill import Skill
from mh_damage.calculator.weapon import Weapon


class BuildFactory:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def skill_from_spec(self, spec: Skill):
        return Skill(spec.name, spec.level, self.weapon.type, spec.uptime)

    def build_from_specs(self, specs: list[Skill]):
        skills = [self.skill_from_spec(s) for s in specs]
        return Build(self.weapon, *skills)