import unittest

from mh_damage.calculator.build_factory import BuildFactory
from mh_damage.calculator.damage import Damage
from mh_damage.calculator.skill import Skill
from mh_damage.calculator.weapon import Weapon


class DamageCalculationTest(unittest.TestCase):
    def test_damage_for_reference_dual_blades_build(self):
        weapon = Weapon("dual_blades", attack=216, elemental=46)

        build_specs = [
            Skill("elemental_boost", 3),
            Skill("weakness_exploit", 4),
            Skill("maximum_might", 3),
            Skill("latent_power", 5),
            Skill("guts", 1),
            Skill("crit_boost", 3),
            Skill("critical_element", 1),
        ]

        factory = BuildFactory(weapon)
        build = factory.build_from_specs(build_specs)

        damage = Damage(
            build,
            raw_hitzone=0.8,
            elemental_hitzone=0.3,
            raw_motion_value=0.08,
            elemental_motion_value=0.6,
        )

        self.assertAlmostEqual(damage.total_damage(), 38.9763058)


if __name__ == "__main__":
    unittest.main()