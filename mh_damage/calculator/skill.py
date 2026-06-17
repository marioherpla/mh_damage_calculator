from mh_damage.static_data.skills import SKILL_EFFECTS
from mh_damage.static_data.weapons import ALL_WEAPONS


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
                    self.stats_dict[attr][op] = (self.stats_dict[attr][op] - 1) * self.uptime + 1
                elif op == "flat":
                    self.stats_dict[attr][op] *= self.uptime
                elif op == "replace":
                    pass

    def effects(self) -> dict:
        self.stats_dict = self.get_skill_stats()
        self._apply_uptime()
        return self.stats_dict