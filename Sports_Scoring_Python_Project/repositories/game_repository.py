from db.run_sql import run_sql
from models.game import Game
from models.team import Team
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

def save(game):
    sql = "INSERT INTO games (home_team, away_team, home_team_score, away_team_score, game_date) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [game.home_team.id, game.away_team.id, game.home_team_score, game.away_team_score, game.game_date]
    results = run_sql(sql, values)
    id = results[0]["id"]
    game.id = id
    return game
    

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        home_team = team_repository.select(result["home_team"])
        away_team = team_repository.select(result["away_team"])
        home_score = result["home_team_score"]
        away_score = result["away_team_score"]
        game_date = result["game_date"]
        game = Game(home_team, away_team, home_score, away_score, game_date, id)
    return game


def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    print(results)

    for row in results:
        home_team = team_repository.select(row['home_team'])
        away_team = team_repository.select(row['away_team'])
        game = Game(home_team, away_team, row['home_team_score'], row['away_team_score'], row['game_date'], row['id'])
        games.append(game)

    return games


def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM games WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def update(game):
    sql = "UPDATE games SET home_team = %s, away_team = %s, home_team_score = %s, away_team_score = %s, game_date = %s WHERE id = %s"
    values = [game.home_team.id, game.away_team.id, game.home_team_score, game.away_team_score, game.game_date, game.id]
    run_sql(sql, values)


# def select_by_team(team_id):
#     games = []

#     sql = "SELECT * FROM games WHERE home_team = %s OR away_team = %s"
#     values = [team_id, team_id]
#     results = run_sql(sql, values)

#     for row in results:
#         home_team = team_repository.select(row['home_team'])
#         away_team = team_repository.select(row['away_team'])
#         game = Game(home_team, away_team, row['home_team_score'], row['away_team_score'], row['game_date'], row['id'])
#         games.append(game)

#     return games

