from flask import Flask, render_template, request
from all_dicts import ALL_WEAPONS
from all_dicts import SKILL_EFFECTS

from cls_damage import Weapon, Skill, BuildFactory, Damage

app = Flask(__name__)

@app.route("/build_calculator", methods=["GET"])
def form():
    return render_template(
        "build_form.html",
        weapons=ALL_WEAPONS,
        skills=SKILL_EFFECTS
    )

@app.route("/build_calculator/calculate", methods=["POST"])
def calculate():
    damage = calculate_damage(request.form)
    return render_template(
        "build_result.html",
        damage=damage
    )

def calculate_damage(form):
    weapon_type = form["weapon_type"]
    attack = int(form["attack"])
    elemental = int(form["elemental"])
    affinity = int(form["affinity"])

    if weapon_type not in ALL_WEAPONS:
        raise ValueError("Invalid weapon type")

    weapon = Weapon(
        type=weapon_type,
        attack=attack,
        elemental=elemental,
        affinity=affinity
    )

    skills = []
    for skill_id in form.getlist("skills"):
        if skill_id not in SKILL_EFFECTS:
            raise ValueError("Invalid skill")

        level = int(form[f"level_{skill_id}"])
        if level not in SKILL_EFFECTS[skill_id]:
            raise ValueError("Invalid skill level")

        skills.append(Skill(skill_id, level))

    factory = BuildFactory(weapon)
    build = factory.build_from_specs(skills)

    return Damage(build, raw_hitzone= 0.8, elemental_hitzone = 0.3, raw_motion_value = 0.08, elemental_motion_value = 0.6).total_damage()

if __name__ == "__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/build_calculator
#& C:/Users/mario/anaconda3/python.exe c:/Users/mario/Desktop/calculadora_daño_mh/app.py