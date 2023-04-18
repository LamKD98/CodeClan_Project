class Team:
    def __init__(self, team_name,wins,losses,logo,region,id = None):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.region = region
        self.logo = logo
        self.id = id