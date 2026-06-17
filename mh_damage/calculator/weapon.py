from mh_damage.calculator.skill_engine import SkillEngine
from mh_damage.calculator.statistics import Statistics


class Weapon:
    def __init__(self, type: str, sharpness: str = 'white', attack: int = 0, elemental: int = 0, affinity: float = 0.0, critical: float = 1.25, critical_elemental: float = 1.0):
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