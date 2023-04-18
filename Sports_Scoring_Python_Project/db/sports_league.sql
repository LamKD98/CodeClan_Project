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



