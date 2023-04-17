from db.run_sql import run_sql

from models.team import Team
from models.league import League
import repositories.league_repository as league_repository


def save(team):
    sql = "INSERT INTO teams (team_name, league_id, wins,losses,region) VALUES (%s, %s,%s,%s,%s) RETURNING *"
    values = [team.team_name, team.league.id, team.wins, team.losses, team.region]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id=%s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        league = league_repository.select(result['league_id'])
        team = Team(result['team_name'],league, result['wins'], result['losses'],result['region'], result['id'] )
    return team


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results =  run_sql(sql)

    for row in results:
        league = league_repository.select(row['league_id'])
        team = Team(row['team_name'],league, row['wins'], row['losses'],row['region'], row['id'] )
        teams.append(team)

    return teams

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET team_name = %s, league_id = %s, wins = %s, losses = %s, region = %s WHERE id = %s"
    values = [team.team_name, team.league.id, team.wins, team.losses, team.region, team.id]
    run_sql(sql, values)

