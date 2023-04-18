import pdb
from models.team import Team
from models.league import League

import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

team_repository.delete_all()
league_repository.delete_all()

league_1 = League('VCT Tournament')
league_repository.save(league_1.id)

league_repository.select_all()

team_1 = Team('Sentinels', league_1, 4,2,'North America')
team_repository.save(team_1.id)

team_2 = Team('Team Liquid', league_1,2,4,'North America')
team_repository.save(team_2.id)

team_3 = Team('Fnatic', league_1, 6,0,'Europe')
team_repository.save(team_3.id)

team_4 = Team('DRX', league_1,0,6,'South Korea')
team_repository.save(team_4.id)