class Team:
    def __init__(self, team_name,league,wins,losses,region,logo = None,id = None):
        self.team_name = team_name
        self.league = league
        self.wins = wins
        self.losses = losses
        self.region = region
        self.logo = logo
        self.id = id