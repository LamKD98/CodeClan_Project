from db.run_sql import run_sql
from models.league import League
from models.team import Team

def save(league):
    sql = "INSERT INTO league (team_name, position) VALUES (%s,%s) RETURNING *"
    values = (league.team_name, league.position)
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id
    return league