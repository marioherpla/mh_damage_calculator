from dataclasses import dataclass


@dataclass
class Statistics:
    attack: int = 0
    elemental: int = 0
    affinity: float = 0.0
    critical: float = 1.25
    critical_elemental: float = 1.0