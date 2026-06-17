from typing import Iterable
from dataclasses import dataclass, replace
from all_dicts import SHARPNESS_MODIFIERS, SKILL_EFFECTS, ALL_WEAPONS, ALL_STATS

@dataclass
class Statistics:
    attack: int = 0
    elemental: int = 0
    affinity: float = 0.0             
    critical: float = 1.25             
    critical_elemental: float = 1.0    

class Weapon:
    def __init__(self, type:str, sharpness: str='white', attack: int = 0, elemental: int = 0, affinity: float = 0.0, critical: float = 1.25, critical_elemental: float = 1.0):
        self.type = type
        self.sharpness = sharpness
        self.stats = Statistics(
            attack=attack,
            elemental=elemental,
            affinity=affinity,
            critical=critical,
            critical_elemental=critical_elemental
        )

    def copy_weapon(self):
            return Weapon(
                type=self.type,
                sharpness=self.sharpness,
                attack=self.stats.attack,
                elemental=self.stats.elemental,
                affinity=self.stats.affinity,
                critical=self.stats.critical,
                critical_elemental=self.stats.critical_elemental
                )

    def apply_skill(self, **stats_dict: dict):

        OPERATION_ORDER = ("percentage", "flat", "replace")

        for attr, operations in stats_dict.items():
            stat_value = getattr(self.stats, attr, None)

            for operation in OPERATION_ORDER:
                if operation not in operations:
                    continue

                value = operations[operation]

                stat_value = SkillEngine().apply_to_value(stat_value, value, operation)
            setattr(self.stats, attr, stat_value)

class SkillEngine:

    def merge_effects(self, *skills):
        merged = {}
        list_skills = self.sum_same_skills(*skills)
        for eff in list_skills:
            for attr, ops in eff.effects().items():
                if attr in merged:
                    pass
                else:
                    merged[attr] = {}

                for op, value in ops.items():
                    if op not in merged[attr]:
                        merged[attr][op] = value
                    else:
                        merged[attr][op] = self.apply_to_value(merged[attr][op], value, op)
        return merged

    def apply_to_value(self, base: float, value: float, op):
        x = base
        if op == "percentage":
            x *= value
        elif op == "flat":
            x += value
        elif op == "replace":
            x = value
        return x

    def sum_same_skills(self, *skills):
        dict_skills = {}
        for skill in skills:
            if skill.name in dict_skills:
                dict_skills[skill.name]['level'] += skill.level
            else:
                dict_skills[skill.name] = {}
                dict_skills[skill.name]['level'] = skill.level
                dict_skills[skill.name]['uptime'] = skill.uptime
                dict_skills[skill.name]['weapon'] = skill.weapon_type

        return [Skill(name, dict_skills[name]['level'], dict_skills[name]['weapon'], dict_skills[name]['uptime']) for name in dict_skills.keys()]

class Skill:
    def __init__(self, name: str, level: float, weapon: str = None, uptime: float = 1.0):
        self.name = name
        self.level = level
        self.uptime = uptime
        self.weapon_type = weapon
    
    def get_skill_stats(self):
        skill_level_dict = SKILL_EFFECTS.get(self.name, {}).get(self.level, {})
        if any(k in ALL_WEAPONS for k in skill_level_dict.keys()):
            stats_dict = skill_level_dict.get(self.weapon_type, skill_level_dict.get("rest", {}))
        else:
            stats_dict = skill_level_dict
        return stats_dict

    def _apply_uptime(self):
        for attr, operations in self.stats_dict.items():
            for op, value in operations.items():
                if op == "percentage":
                    self.stats_dict[attr][op] = (self.stats_dict[attr][op] - 1)*self.uptime + 1
                elif op == "flat":
                    self.stats_dict[attr][op] *= self.uptime
                elif op == "replace":
                    pass

    def effects(self) -> dict:
        self.stats_dict = self.get_skill_stats()
        self._apply_uptime()
        return self.stats_dict

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

class Damage:
    def __init__(self, build: Build, raw_hitzone: float = 0.6, elemental_hitzone: float = 0.15, raw_motion_value: float = 0.12, elemental_motion_value: float = 0.7):
        self.build = build
        self.stats = self.build.weapon_final.stats

        self.raw_hitzone = raw_hitzone
        self.elemental_hitzone = elemental_hitzone
        self.raw_motion_value = raw_motion_value
        self.elemental_motion_value = elemental_motion_value
        
    def calc_physical_damage_crit(self):
        s = self.stats
        return self.raw_motion_value*self.raw_hitzone*SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['raw']*s.attack*s.critical
    
    def calc_physical_damage_no_crit(self):
        s = self.stats
        return self.raw_motion_value*self.raw_hitzone*SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['raw']*s.attack

    def calc_mean_physical_damage(self):
        s = self.stats
        return self.calc_physical_damage_no_crit()*(1-s.affinity) + self.calc_physical_damage_crit()*s.affinity
    
    def calc_elemental_damage_crit(self):
        s = self.stats
        return self.elemental_motion_value*self.elemental_hitzone*SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['elemental']*s.elemental*s.critical_elemental
    
    def calc_elemental_damage_no_crit(self):
        s = self.stats
        return self.elemental_motion_value*self.elemental_hitzone*SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['elemental']*s.elemental
    
    def calc_mean_elemental_damage(self):
        s = self.stats
        return self.calc_elemental_damage_no_crit()*(1-s.affinity) + self.calc_elemental_damage_crit()*s.affinity

    def total_damage(self):
        return self.calc_mean_physical_damage() + self.calc_mean_elemental_damage()

class BuildFactory:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def skill_from_spec(self, spec: Skill):
        return Skill(spec.name, spec.level, self.weapon.type, spec.uptime)

    def build_from_specs(self, specs: list[Skill]):
        skills = [self.skill_from_spec(s) for s in specs]
        return Build(self.weapon, *skills)

# weapon = Weapon("dual_blades", attack=216, elemental=46)

# build_specs = [
#     Skill('elemental_boost', 3),
#     Skill('weakness_exploit', 4),
#     Skill('maximum_might', 3),
#     Skill('latent_power', 5),
#     Skill('guts', 1),
#     Skill('crit_boost', 3),
#     Skill('critical_element', 1)
# ]

# factory = BuildFactory(weapon)
# build = factory.build_from_specs(build_specs)

# print(weapon.stats)
# print(build.weapon_final.stats)

# damage = Damage(build, raw_hitzone= 0.8, elemental_hitzone = 0.3, raw_motion_value = 0.08, elemental_motion_value = 0.6)
# print(damage.total_damage())
