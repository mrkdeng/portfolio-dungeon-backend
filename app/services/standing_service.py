from typing import List
from fastapi import HTTPException
from nba_api.stats.endpoints import leaguestandings
import json

from app.models.standing import *

def get_standings_from_nba_api():
    try:
        standings_json = json.loads(leaguestandings.LeagueStandings().get_json())
        standings = parse_standings_from_json(standings_json)
        return standings
    except Exception as e:
        print(f"An error occurred while getting standings: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch or parse league standings."
        )

def parse_standings_from_json(standings_json) -> List[Standing]:
    return [
        Standing(
            teamId=row[TEAM_ID_INDEX],
            teamCity=row[TEAM_CITY_INDEX],
            teamName=row[TEAM_NAME_INDEX],
            conference=row[CONFERENCE_INDEX],
            division=row[DIVISION_INDEX],
            wins=row[WINS_INDEX],
            losses=row[LOSSES_INDEX],
            winPct=row[WIN_PCT_INDEX],
            currentStreak=row[STREAK_INDEX]
        )
        for row in standings_json["resultSets"][0]["rowSet"]
    ]