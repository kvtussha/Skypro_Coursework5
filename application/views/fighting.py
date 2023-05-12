from flask import Blueprint, render_template, Response, redirect, url_for
from application.container import heroes, arena

# fighting_bp = Blueprint('fighting_bp', __name__)

# # @fighting_bp.route("/")
# @fighting_bp.route("/fight")
# def start_fight() -> str:
#     arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
#     return render_template("fight.html", heroes=heroes, result='Бой начался!')

fighting_bp = Blueprint('fighting_bp', __name__, url_prefix='/fight')


@fighting_bp.route("/")
def start_fight() -> str:
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
    return render_template("fight.html", heroes=heroes, result='Бой начался!')

@fighting_bp.route("/hit")
def hit() -> str:
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)

@fighting_bp.route("/use-skill")
def use_skill() -> str:
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@fighting_bp.route("/pass-turn")
def pass_turn() -> str:
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.result
    return render_template("fight.html", heroes=heroes, result=result)


@fighting_bp.route("/end-fight")
def end_fight() -> Response:
    return redirect(url_for("main_bp.menu_page"))
