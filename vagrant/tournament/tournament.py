#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("SELECT * FROM player")
    return psycopg2.connect("dbname=tournament"),c


def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("DELETE FROM matches;")    
    DB.commit()
    DB.close()
    


def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    """1.delect all the player"""
    """c.execute("DELETE all FROM player")"""
    
    """2.delete all the player record"""
    c.execute("DELETE FROM player;")
    DB.commit()
    DB.close()
    


def countPlayers():
    """Returns the number of players currently registered."""
    
    """1)connect the databse"""
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("""SELECT COUNT(*) FROM player;""")
    result = c.fetchall() 
    return result[0][0]
    DB.close()
   
    
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("INSERT INTO player(name) VALUES(%s)",(name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    
    """1)connect to the database"""
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    """2)execute the statement"""
    c.execute("SELECT * FROM standings")
    result = c.fetchall()
    DB.commit()
    DB.close()
    return result
    


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    """1)connect to the database"""
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    
    c.execute("INSERT INTO matches(id_winner,id_looser) VALUES(%s,%s)",(winner,loser))
    DB.commit()
    DB.close()
    
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()

    query = "select count(*) from standings"
    
    c.execute(query)
    result = c.fetchall()
    
    standings = playerStandings()
    
    player = [item[0:2] for item in standings]
    index = 0
    pairings = []
    for row in result:
        
        while (index < row[0] ):
            
            pair = player[index]+player[index+1]
            pairings.append(pair)
            
            index = index + 2
        return pairings
    DB.close()
