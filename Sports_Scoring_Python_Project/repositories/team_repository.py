from db.run_sql import run_sql

from models.team import Team
from models.league import League
import repositories.league_repository as league_repository

def save(team):
    sql = "INSERT INTO teams (team_name, league_id, wins, losses, region, logo) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [team.team_name, team.league.id, team.wins, team.losses, team.region, team.logo]
    results = run_sql(sql, values)
    if results:
        team.id = results[0]['id']
        return team
    else:
        return None

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id=%s"
    values = [id]
    results = run_sql(sql,values)

    if results is not None:
        result = results[0]
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
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET team_name = %s, league_id = %s, wins = %s, losses = %s, region = %s WHERE id = %s"
    values = [team.team_name, team.league.id, team.wins, team.losses, team.region, team.id]
    run_sql(sql, values)




