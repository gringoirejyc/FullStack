-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--create datebase
create database tournament;
\c tournament

--create table player include the player id as an unique and player fullname
create table player (
    id serial,
    name text,
    
    primary key(id)
);

--create table matches include the match id,the winner id and the looser id
create table matches(
    id_match serial,
    id_winner integer null references player(id),
    id_looser integer null references player(id),
    primary key(id_match)
);

--create countWins view to count each player win how many times
create view countWins as
     select player.id as ID,player.name as Name,coalesce(count(matches.id_winner),0) as Record
     from player left join matches
     on player.id = matches.id_winner
     group by player.id
     order by player.id;
     
--create countLoses view to count each player lose how many times
create view countLoses as
     select player.id as ID,player.name as Name,coalesce(count(matches.id_looser),0) as Record
     from player left join matches
     on player.id = matches.id_looser
     group by player.id
     order by player.id;
     
--create view to count each player attent how many matches
create view countMatches as
      select player.id as ID,player.name as Name,count(matches.id_match) as Played
      from player left join matches
      on player.id = matches.id_winner or player.id = matches.id_looser
      group by player.id
      order by player.id;
      
--create view standing
create view standings as
      select countMatches.ID as ID,countMatches.Name as Name,coalesce(countWins.Record,'0'),countMatches.Played
      from countMatches left join countWins 
      on countWins.ID = countMatches.ID 
      order by coalesce(countWins.Record) ASC
      ;
