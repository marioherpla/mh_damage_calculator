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
        from mh_damage.calculator.skill import Skill

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