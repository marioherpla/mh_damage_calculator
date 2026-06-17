from mh_damage.calculator.skill import Skill
from mh_damage.calculator.skill_engine import SkillEngine
from mh_damage.calculator.weapon import Weapon


class Build:
    def __init__(self, weapon: Weapon, *skills: Skill):
        self.weapon_base = weapon
        self.stats_dict = SkillEngine().merge_effects(*skills)

        self.weapon_final = self.weapon_base.copy_weapon()
        self.weapon_final.apply_skill(**self.stats_dict)

        self.check_affinity()

    def check_affinity(self):
        if self.weapon_final.stats.affinity > 1:
            self.weapon_final.stats.affinity = 1
        else:
            pass