from db.run_sql import run_sql
from models.league import League
from models.team import Team
import repositories.team_repository as team_repository

def save(league):
    sql = "INSERT INTO league (league_name) VALUES (%s) RETURNING *"
    values = [league.league_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id
    return league

def select_all():
    leagues = []

    sql = "SELECT * FROM league"
    results = run_sql(sql)

    for row in results:
        league = League(row['league_name'], row['id'])
        leagues.append(league)
    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM league WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results is not None:
        result = results[0]
        league = League(result['league_name'],  result['id'] )
    return league

def delete_all():
    sql = "DELETE FROM league"
    run_sql(sql)

def calculate_leaderboard():
    teams = team_repository.select_all()
    leaderboard = []

    for team in teams:
        wins = team.wins
        losses = team.losses
        points = 0
        for other_team in teams:
            if team == other_team:
                continue
            if wins > other_team.wins or (wins == other_team.wins and losses < other_team.losses):
                points += 3
            elif wins == other_team.wins and losses == other_team.losses:
                points += 1
        leaderboard.append((team, points))

    leaderboard.sort(key=lambda x: x[1], reverse=True)
    return leaderboard