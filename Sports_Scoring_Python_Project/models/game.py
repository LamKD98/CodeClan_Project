class Game:
    def __init__(self, home_team, away_team, home_score, away_score , game_date, id = None):
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = home_score
        self.away_team_score = away_score
        self.game_date = game_date
        self.id = id