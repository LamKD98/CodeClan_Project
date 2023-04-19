import pdb
from models.team import Team
from models.league import League
from models.game import Game
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository
import repositories.game_repository as game_repository

team_repository.delete_all()
league_repository.delete_all()
game_repository.delete_all()

league_1 = League('VCT Tournament')
league_repository.save(league_1)

league_repository.select_all()

team_1 = Team('Sentinels', league_1, 4,2,'North America', 'Sentinels_logo.png')
team_repository.save(team_1)

team_2 = Team('Team Liquid', league_1,2,4,'North America', 'Team_Liquid_logo.png')
team_repository.save(team_2)

team_3 = Team('Fnatic', league_1, 6,0,'Europe', 'fnatic_logo.png')
team_repository.save(team_3)

team_4 = Team('DRX', league_1,0,6,'South Korea', 'DRX_logo.png')
team_repository.save(team_4)

# team1 = team_repository.select(team_1.id)
# team2 = team_repository.select(team_2.id)
game1 = Game(team_1, team_2, 10, 8 , '2023-04-10')
game_repository.save(game1)
game2 = Game(team_2, team_1, 13, 11, '2023-04-19')
game_repository.save(game2)


# CREATE TABLE games (
#     id SERIAL PRIMARY KEY,
#     home_team_id INTEGER,
#     away_team_id INTEGER,
#     home_team_score INTEGER,
#     away_team_score INTEGER,
#     game_date DATE NOT NULL DEFAULT CURRENT_DATE,
#     FOREIGN KEY (home_team_id) REFERENCES teams(id),
#     FOREIGN KEY (away_team_id) REFERENCES teams(id)
# );

