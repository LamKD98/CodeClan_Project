DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS league;

CREATE TABLE league(
    id SERIAL PRIMARY KEY,
    league_name VARCHAR(255)
);


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255) UNIQUE,
    wins INT,
    losses INT,
    region VARCHAR(255),
    logo VARCHAR(255),
    league_id INT NOT NULL REFERENCES league(id)

);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_team_score INTEGER,
    away_team_score INTEGER,
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id)
);




