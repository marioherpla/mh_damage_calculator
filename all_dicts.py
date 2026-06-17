ALL_STATS = [
    "attack",
    "affinity",
    "critical",
    "elemental",
    "critical_elemental"
]

ALL_WEAPONS = [
    "great_sword",
    "long_sword",
    "sword_and_shield",
    "dual_blades",
    "hammer",
    "hh",
    "lance",
    "gunlance",
    "switch_axe",
    "charge_blade",
    "insect_glaive",
    "light_bowgun",
    "heavy_bowgun",
    "bow"
]

SKILL_EFFECTS = {
    "attack_boost": {
        1: {"attack": {"flat": 3}},
        2: {"attack": {"flat": 5}},
        3: {"attack": {"flat": 7}},
        4: {"attack": {"percentage": 1.02, "flat": 8}},
        5: {"attack": {"percentage": 1.04, "flat": 9}},
    },
    "elemental_boost": {
        1: {"elemental": {"flat": 4}},
        2: {"elemental": {"percentage": 1.10, "flat": 5}},
        3: {"elemental": {"percentage": 1.20, "flat": 6}},
    },
    "crit_boost": {
        1: {"critical": {"replace": 1.28}},
        2: {"critical": {"replace": 1.31}},
        3: {"critical": {"replace": 1.34}},
        4: {"critical": {"replace": 1.37}},
        5: {"critical": {"replace": 1.40}},
    },
    "adrenaline_rush": {
        1: {"attack": {"flat": 10}},
        2: {"attack": {"flat": 15}},
        3: {"attack": {"flat": 20}},
        4: {"attack": {"flat": 25}},
        5: {"attack": {"flat": 30}},
    },
    "agitator": {
        1: {"attack": {"flat": 4}, "affinity": {"flat": 0.03}},
        2: {"attack": {"flat": 8}, "affinity": {"flat": 0.05}},
        3: {"attack": {"flat": 12}, "affinity": {"flat": 0.07}},
        4: {"attack": {"flat": 16}, "affinity": {"flat": 0.10}},
        5: {"attack": {"flat": 20}, "affinity": {"flat": 0.15}},
    },
    "counterstrike": {
        1: {"attack": {"flat": 10}},
        2: {"attack": {"flat": 15}},
        3: {"attack": {"flat": 25}},
    },
    "peak_performance": {
        1: {"attack": {"flat": 3}},
        2: {"attack": {"flat": 6}},
        3: {"attack": {"flat": 10}},
        4: {"attack": {"flat": 15}},
        5: {"attack": {"flat": 20}}, 
    },
    "weakness_exploit": {
        1: {"affinity": {"flat": 0.05}},
        2: {"affinity": {"flat": 0.10}},
        3: {"affinity": {"flat": 0.15}},
        4: {"affinity": {"flat": 0.20}},
        5: {"affinity": {"flat": 0.30}},
    },
    "latent_power": {
        1: {"affinity": {"flat": 0.10}},
        2: {"affinity": {"flat": 0.20}},
        3: {"affinity": {"flat": 0.30}},
        4: {"affinity": {"flat": 0.40}},
        5: {"affinity": {"flat": 0.50}},
    },
    "maximum_might": {
        1: {"affinity": {"flat": 0.10}},
        2: {"affinity": {"flat": 0.20}},
        3: {"affinity": {"flat": 0.30}},
    },
    "mutual_hostility": {
        1: {"elemental": {"percentage": 1.20, "flat": 2}},
        2: {"elemental": {"percentage": 1.30, "flat": 4}}
    },
    "guts": {
        1: {"attack": {"percentage": 1.05}}
    },
    "black_eclipse": {
        1: {"affinity": {"flat": 0.15}},
        2: {"affinity": {"flat": 0.15}, "attack": {"flat": 15}}
    },
    "antivirus": {
        1: {"affinity": {"flat": 0.03}},
        2: {"affinity": {"flat": 0.06}},
        3: {"affinity": {"flat": 0.10}}
    },
    "burst_boost": {
        1: {"attack": {"flat": 8}},
        2: {"attack": {"flat": 18}}
    },
    "coalescence": {
        1: {
            "great_sword": {"elemental": {"percentage": 1.10}},
            "long_sword": {"elemental": {"percentage": 1.05}},
            "sword_and_shield": {"elemental": {"percentage": 1.05}},
            "dual_blades": {"elemental": {"percentage": 1.05}},
            "hammer": {"elemental": {"percentage": 1.10}},
            "hh": {"elemental": {"percentage": 1.10}},
            "lance": {"elemental": {"percentage": 1.05}},
            "gunlance": {"elemental": {"percentage": 1.10}},
            "switch_axe": {"elemental": {"percentage": 1.10}},
            "charge_blade": {"elemental": {"percentage": 1.10}},
            "insect_glaive": {"elemental": {"percentage": 1.05}},
            "light_bowgun": {"elemental": {"percentage": 1.05}},
            "heavy_bowgun": {"elemental": {"percentage": 1.05}},
            "bow": {"elemental": {"percentage": 1.05}}
            },
        2: {
            "great_sword": {"elemental": {"percentage": 1.20}},
            "long_sword": {"elemental": {"percentage": 1.10}},
            "sword_and_shield": {"elemental": {"percentage": 1.10}},
            "dual_blades": {"elemental": {"percentage": 1.10}},
            "hammer": {"elemental": {"percentage": 1.20}},
            "hh": {"elemental": {"percentage": 1.20}},
            "lance": {"elemental": {"percentage": 1.10}},
            "gunlance": {"elemental": {"percentage": 1.20}},
            "switch_axe": {"elemental": {"percentage": 1.20}},
            "charge_blade": {"elemental": {"percentage": 1.20}},
            "insect_glaive": {"elemental": {"percentage": 1.10}},
            "light_bowgun": {"elemental": {"percentage": 1.10}},
            "heavy_bowgun": {"elemental": {"percentage": 1.10}},
            "bow": {"elemental": {"percentage": 1.10}}
            },
        3: {
            "great_sword": {"elemental": {"percentage": 1.30}},
            "long_sword": {"elemental": {"percentage": 1.15}},
            "sword_and_shield": {"elemental": {"percentage": 1.15}},
            "dual_blades": {"elemental": {"percentage": 1.15}},
            "hammer": {"elemental": {"percentage": 1.30}},
            "hh": {"elemental": {"percentage": 1.30}},
            "lance": {"elemental": {"percentage": 1.15}},
            "gunlance": {"elemental": {"percentage": 1.30}},
            "switch_axe": {"elemental": {"percentage": 1.30}},
            "charge_blade": {"elemental": {"percentage": 1.30}},
            "insect_glaive": {"elemental": {"percentage": 1.15}},
            "light_bowgun": {"elemental": {"percentage": 1.15}},
            "heavy_bowgun": {"elemental": {"percentage": 1.15}},
            "bow": {"elemental": {"percentage": 1.15}}
            }
    },
    "burst": {
        1: {
            "great_sword": {"attack": {"flat": 10}, "elemental": {"flat": 8}},
            "hh": {"attack": {"flat": 10}, "elemental": {"flat": 8}},
            "dual_blades": {"attack": {"flat": 8}, "elemental": {"flat": 4}},
            "bow": {"attack": {"flat": 6}, "elemental": {"flat": 4}},
            "rest": {"attack": {"flat": 8}, "elemental": {"flat": 6}},
        },
        2: {
            "great_sword": {"attack": {"flat": 12}, "elemental": {"flat": 10}},
            "hh": {"attack": {"flat": 12}, "elemental": {"flat": 10}},
            "dual_blades": {"attack": {"flat": 10}, "elemental": {"flat": 6}},
            "bow": {"attack": {"flat": 7}, "elemental": {"flat": 6}},
            "rest": {"attack": {"flat": 10}, "elemental": {"flat": 8}},
        },
        3: {
            "great_sword": {"attack": {"flat": 14}, "elemental": {"flat": 12}},
            "hh": {"attack": {"flat": 14}, "elemental": {"flat": 12}},
            "dual_blades": {"attack": {"flat": 12}, "elemental": {"flat": 8}},
            "bow": {"attack": {"flat": 8}, "elemental": {"flat": 8}},
            "rest": {"attack": {"flat": 12}, "elemental": {"flat": 10}},
        },
        4: {
            "great_sword": {"attack": {"flat": 16}, "elemental": {"flat": 16}},
            "hh": {"attack": {"flat": 16}, "elemental": {"flat": 16}},
            "dual_blades": {"attack": {"flat": 15}, "elemental": {"flat": 10}},
            "bow": {"attack": {"flat": 9}, "elemental": {"flat": 10}},
            "rest": {"attack": {"flat": 15}, "elemental": {"flat": 12}},
        },
        5: {
            "great_sword": {"attack": {"flat": 18}, "elemental": {"flat": 20}},
            "hh": {"attack": {"flat": 18}, "elemental": {"flat": 20}},
            "dual_blades": {"attack": {"flat": 18}, "elemental": {"flat": 12}},
            "bow": {"attack": {"flat": 10}, "elemental": {"flat": 12}},
            "rest": {"attack": {"flat": 18}, "elemental": {"flat": 14}},
        },
    },
    "critical_element":{
        1: {
            "great_sword": {"critical_elemental": {"replace": 1.07}},
            "long_sword": {"critical_elemental": {"replace": 1.05}},
            "sword_and_shield": {"critical_elemental": {"replace": 1.05}},
            "dual_blades": {"critical_elemental": {"replace": 1.05}},
            "hammer": {"critical_elemental": {"replace": 1.07}},
            "hh": {"critical_elemental": {"replace": 1.07}},
            "lance": {"critical_elemental": {"replace": 1.05}},
            "gunlance": {"critical_elemental": {"replace": 1.07}},
            "switch_axe": {"critical_elemental": {"replace": 1.07}},
            "charge_blade": {"critical_elemental": {"replace": 1.07}},
            "insect_glaive": {"critical_elemental": {"replace": 1.05}},
            "light_bowgun": {"critical_elemental": {"replace": 1.05}},
            "heavy_bowgun": {"critical_elemental": {"replace": 1.05}},
            "bow": {"critical_elemental": {"replace": 1.05}},
        },
        2: {
            "great_sword": {"critical_elemental": {"replace": 1.13}},
            "long_sword": {"critical_elemental": {"replace": 1.10}},
            "sword_and_shield": {"critical_elemental": {"replace": 1.10}},
            "dual_blades": {"critical_elemental": {"replace": 1.10}},
            "hammer": {"critical_elemental": {"replace": 1.13}},
            "hh": {"critical_elemental": {"replace": 1.13}},
            "lance": {"critical_elemental": {"replace": 1.10}},
            "gunlance": {"critical_elemental": {"replace": 1.13}},
            "switch_axe": {"critical_elemental": {"replace": 1.13}},
            "charge_blade": {"critical_elemental": {"replace": 1.13}},
            "insect_glaive": {"critical_elemental": {"replace": 1.10}},
            "light_bowgun": {"critical_elemental": {"replace": 1.10}},
            "heavy_bowgun": {"critical_elemental": {"replace": 1.10}},
            "bow": {"critical_elemental": {"replace": 1.10}},
        },
        3: {
            "great_sword": {"critical_elemental": {"replace": 1.20}},
            "long_sword": {"critical_elemental": {"replace": 1.15}},
            "sword_and_shield": {"critical_elemental": {"replace": 1.15}},
            "dual_blades": {"critical_elemental": {"replace": 1.15}},
            "hammer": {"critical_elemental": {"replace": 1.20}},
            "hh": {"critical_elemental": {"replace": 1.20}},
            "lance": {"critical_elemental": {"replace": 1.15}},
            "gunlance": {"critical_elemental": {"replace": 1.20}},
            "switch_axe": {"critical_elemental": {"replace": 1.20}},
            "charge_blade": {"critical_elemental": {"replace": 1.20}},
            "insect_glaive": {"critical_elemental": {"replace": 1.15}},
            "light_bowgun": {"critical_elemental": {"replace": 1.15}},
            "heavy_bowgun": {"critical_elemental": {"replace": 1.15}},
            "bow": {"critical_elemental": {"replace": 1.15}},
        },
    }
}

SHARPNESS_MODIFIERS = {
    "red": {
        "raw": 0.5,
        "elemental": 0.25,
    },
    "orange": {
        "raw": 0.75,
        "elemental": 0.5,
    },
    "yellow": {
        "raw": 1.0,
        "elemental": 0.75,
    },
    "green": {
        "raw": 1.05,
        "elemental": 1.0,
    },
    "blue": {
        "raw": 1.2,
        "elemental": 1.063,
    },
    "white": {
        "raw": 1.32,
        "elemental": 1.15,
    },
}
