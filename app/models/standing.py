import json
from pydantic import BaseModel

TEAM_ID_INDEX = 2
TEAM_CITY_INDEX = 3
TEAM_NAME_INDEX = 4
CONFERENCE_INDEX = 5
DIVISION_INDEX = 9
WINS_INDEX = 12
LOSSES_INDEX = 13
WIN_PCT_INDEX = 14
STREAK_INDEX = 34

class Standing(BaseModel):
    teamId: int
    teamName: str
    teamCity: str
    conference: str
    division: str
    wins: int
    losses: int
    winPct: float
    currentStreak: str