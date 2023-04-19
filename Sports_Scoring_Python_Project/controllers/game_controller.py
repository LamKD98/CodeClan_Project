from flask import Blueprint, render_template, request, redirect, url_for
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
from models.game import Game



game_blueprint = Blueprint('games', __name__)

# INDEX
# GET/games
@game_blueprint.route('/games')
def games():
    all_games = game_repository.select_all()
    # for game in all_games:
    #     print(game.__dict__)
    return render_template('games/index.html', all_games=all_games)

# NEW
# GET /games/new
@game_blueprint.route('/games/new', methods=['GET'])
def new():
    teams = team_repository.select_all()
    return render_template('games/new.html', teams=teams)

@game_blueprint.route("/games", methods=["POST"])
def create():
    home_team_id = request.form["home_team"]
    away_team_id = request.form["away_team"]
    home_team_score = request.form["home_team_score"]
    away_team_score = request.form["away_team_score"]
    game_date = request.form["game_date"]

    home_team = team_repository.select(home_team_id)
    away_team = team_repository.select(away_team_id)

    new_game = Game(home_team, away_team, home_team_score, away_team_score, game_date)
    game_repository.save(new_game)  # Updated line
    return redirect("/games")
# SHOW
# GET /games/<id>
@game_blueprint.route('/games/<id>', methods=['GET'])
def show(id):
    game = game_repository.select(id)
    return render_template('games/show.html', game=game)

# EDIT
# GET /games/<id>/edit
@game_blueprint.route('/games/<id>/edit', methods=['GET'])
def edit_game(id):
    game = game_repository.select(id)
    print(game)
    teams = team_repository.select_all()
    return render_template('games/edit.html', game=game, teams=teams)

# UPDATE
# POST /games/<id>
@game_blueprint.route('/games/<id>', methods=['POST'])
def update_game(id):
    home_team_id = request.form['home_team']
    away_team_id = request.form['away_team']
    home_team_score = request.form['home_team_score']
    away_team_score = request.form['away_team_score']
    game_date = request.form['game_date']
    new_home_team = team_repository.select(home_team_id)
    new_away_team = team_repository.select(away_team_id)

    game = game_repository.select(id)
    game.home_team = new_home_team
    game.away_team = new_away_team
    game.home_team_score = home_team_score
    game.away_team_score = away_team_score
    game.game_date = game_date
    game_repository.update(game)
    return redirect('/games')   

# DELETE
# DELETE /games/<id>/delete
@game_blueprint.route('/games/<id>/delete', methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect('/games')

# SELECT BY TEAM
# GET /games/team/<id>
@game_blueprint.route('/games/team/<id>', methods=['GET'])
def games_by_team(id):
    games = game_repository.select(id)
    return render_template('games/index.html', all_games=games)

