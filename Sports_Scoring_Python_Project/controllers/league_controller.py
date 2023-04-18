from flask import Blueprint, render_template, redirect, request, url_for
from models.league import League
from repositories.league_repository import league_repository

league_blueprint = Blueprint("league", __name__)

# Index
@league_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)

# Show
@league_blueprint.route("/leagues/<league_id>")
def show_league(league_id):
    league = league_repository.select(league_id)
    return render_template("leagues/show.html", league=league)

# New
@league_blueprint.route("/leagues/new", methods=["GET"])
def new_league():
    return render_template("leagues/new.html")

# Create
@league_blueprint.route("/leagues", methods=["POST"])
def create_league():
    name = request.form["league_name"]
    new_league = League(name)
    league_repository.save(new_league)
    return redirect("/leagues")

@league_blueprint.route('/leagues/delete', methods=['POST'])
def delete_league(league_id):
    league_repository.delete(league_id)
    return redirect('/leagues')