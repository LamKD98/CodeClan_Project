from flask import Blueprint, render_template, request, redirect, url_for
from repositories import team_repository
from repositories import league_repository
from models.team import Team

team_blueprint = Blueprint('teams', __name__)

# INDEX
# GET/teams
@team_blueprint.route('/teams')
def teams():
    all_teams = team_repository.select_all()
    return render_template('teams/index.html', all_teams = all_teams)


# NEW
# GET /teams/new
@team_blueprint.route('/teams/new', methods=['GET'])
def new():
    leagues = league_repository.select_all()
    return render_template('teams/new.html', leagues=leagues)

@team_blueprint.route("/teams", methods=["POST"])
def create():
    team_name = request.form["team_name"]
    league_id = request.form["league"]
    league = league_repository.select(league_id)
    wins = request.form["wins"]
    losses = request.form["losses"]
    region = request.form["region"]
    logo = request.form["logo"]

    new_team = Team(team_name, league, wins, losses, region, logo)
    team_repository.save(new_team)
    return redirect("/teams")


# SHOW
# GET /teams/<id>
@team_blueprint.route('/teams/show', methods=['GET'])
def show():
    teams = team_repository.select_all()
    leaderboard = league_repository.calculate_leaderboard()
    return render_template('teams/show.html', teams=teams, leaderboard=leaderboard)

# EDIT
# GET /teams/<id>/edit
@team_blueprint.route('/teams/<id>/edit', methods=['GET'])
def edit_team(id):
    team = team_repository.select(id)
    leagues = league_repository.select_all()
    return render_template('teams/edit.html',team=team,leagues=leagues)


# UPDATE
# POST /teams/<id>
@team_blueprint.route("/teams/<id>", methods=["POST"])
def update(id):
    team_name = request.form["name"]
    league_id = request.form["league_name"]
    league = league_repository.select(league_id)
    wins = request.form["wins"]
    losses = request.form["losses"]
    region = request.form["region"]
    logo = request.form["logo"]
    team_repository.update(Team(team_name, league, wins, losses, region, logo, id))
    return redirect("/teams")

# DELETE
# DELETE /tasks/<id>/delete
@team_blueprint.route('/teams/<id>/delete', methods=['POST'])
def delete(id):
    team_repository.delete(id)
    return redirect('/teams') 