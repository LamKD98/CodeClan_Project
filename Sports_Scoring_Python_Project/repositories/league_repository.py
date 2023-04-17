from db.run_sql import run_sql
from models.league import League
from models.team import Team

def save(league):
    sql = "INSERT INTO league (team_name, position) VALUES (%s,%s) RETURNING *"
    values = (league.league_name, league.position)
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id
    return league

def select_all():
    leagues = []

    sql = "SELECT * FROM league"
    results = run_sql(sql)

    for row in results:
        league = League(row['league_name'], row['position'], row['id'])
        leagues.append(league)
    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM league WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['league_name'], result['position'], result['id'] )
    return league

