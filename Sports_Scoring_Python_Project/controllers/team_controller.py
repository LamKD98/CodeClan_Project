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

#CREATE
@team_blueprint.route('/teams', methods=['POST'])
def create():
    team_name = request.form['team_name']
    league_id = request.form['league']
    region = request.form['region']
    wins = request.form['wins']
    losses = request.form['losses']

    league = league_repository.select(league_id)
    team = Team(team_name, league, wins=int(wins), losses=int(losses), region=region)
    team_repository.save(team)
    return redirect(url_for('teams.new'))


# SHOW
# GET /teams/<id>
@team_blueprint.route('/teams/show', methods=['GET'])
def show():
    teams = team_repository.select_all()
    leaderboard = league_repository.calculate_leaderboard()
    return render_template('teams/show.html', teams=teams, leaderboard=leaderboard)

# EDIT
# GET /teams/<id>/edit
@team_blueprint.route('/teams/<id>/edit', methods=['GET', 'POST'])
def edit_team(id):
    team = team_repository.select(id)
    league = league_repository.select_all()
    return render_template('teams/edit.html',team=team,league=league)


# UPDATE
# POST /teams/<id>
@team_blueprint.route('/teams/edit', methods=['POST'])
def update():
    team_id = request.form['team_id']
    team_name = request.form['team_name']
    league_id = request.form['league_id']
    region = request.form['region']

    league = league_repository.select(league_id)
    team = team_repository.select(team_id)
    team.team_name = team_name
    team.league = league
    team.region = region
    team_repository.update(team)
    return redirect(url_for('teams.index'))   

# DELETE
# DELETE /tasks/<id>/delete
@team_blueprint.route('/teams/delete', methods=['POST'])
def delete():
    team_id = request.form['team_id']
    team_repository.delete(team_id)
    return redirect(url_for('teams.index'))