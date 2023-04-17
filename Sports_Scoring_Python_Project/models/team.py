class Team:
    def __init__(self, team_name,wins,losses,region,id = None):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.region = region
        self.id = id