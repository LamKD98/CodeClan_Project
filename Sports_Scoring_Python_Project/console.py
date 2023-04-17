import pdb
from models.team import Team
from models.league import League

import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

team_repository.delete_all()
league_repository.delete_all()

