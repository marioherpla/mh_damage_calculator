from mh_damage.calculator.build import Build
from mh_damage.static_data.modifiers import SHARPNESS_MODIFIERS


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
        return self.raw_motion_value * self.raw_hitzone * SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['raw'] * s.attack * s.critical

    def calc_physical_damage_no_crit(self):
        s = self.stats
        return self.raw_motion_value * self.raw_hitzone * SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['raw'] * s.attack

    def calc_mean_physical_damage(self):
        s = self.stats
        return self.calc_physical_damage_no_crit() * (1 - s.affinity) + self.calc_physical_damage_crit() * s.affinity

    def calc_elemental_damage_crit(self):
        s = self.stats
        return self.elemental_motion_value * self.elemental_hitzone * SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['elemental'] * s.elemental * s.critical_elemental

    def calc_elemental_damage_no_crit(self):
        s = self.stats
        return self.elemental_motion_value * self.elemental_hitzone * SHARPNESS_MODIFIERS[self.build.weapon_final.sharpness]['elemental'] * s.elemental

    def calc_mean_elemental_damage(self):
        s = self.stats
        return self.calc_elemental_damage_no_crit() * (1 - s.affinity) + self.calc_elemental_damage_crit() * s.affinity

    def total_damage(self):
        return self.calc_mean_physical_damage() + self.calc_mean_elemental_damage()