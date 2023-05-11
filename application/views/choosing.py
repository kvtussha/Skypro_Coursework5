from flask import Blueprint, render_template, request, redirect, url_for, Response
from application.container import unit_classes
from application.container import creating_units, heroes, equipment
from application.unit import PlayerUnit, EnemyUnit

choosing_bp = Blueprint("choosing_bp", __name__)
@choosing_bp.route("/choose-hero/", methods=['post', 'get'])
def choose_hero() -> Response | str:
    if request.method == "GET":
        creating_units["header"] = "Выберите героя"
        return render_template("hero_choosing.html", result=creating_units)
    if request.method == "POST":
        name = request.form["name"]
        unit_class = request.form["unit_class"]
        armor = request.form["armor"]
        weapon = request.form["weapon"]
        player = PlayerUnit(name=name, unit_class=unit_classes[unit_class])
        player.equip_armor(equipment.get_armor(armor))
        player.equip_weapon(equipment.get_weapon(weapon))
        heroes["player"] = player
        return redirect(url_for("choosing_bp.choose_enemy"))


@choosing_bp.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy() -> Response | str:
    if request.method == "GET":
        creating_units["header"] = "Выберите противника"
        return render_template("hero_choosing.html", result=creating_units)
    if request.method == "POST":
        name = request.form["name"]
        unit_class = request.form["unit_class"]
        armor = request.form["armor"]
        weapon = request.form["weapon"]
        enemy = EnemyUnit(name=name, unit_class=unit_classes[unit_class])
        enemy.equip_armor(equipment.get_armor(armor))
        enemy.equip_weapon(equipment.get_weapon(weapon))
        heroes["enemy"] = enemy
        return redirect(url_for("fighting_bp.start_fight"))
