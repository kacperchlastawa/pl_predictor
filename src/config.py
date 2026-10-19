import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/'.env')

class Config:
    RAW_DATA_DIR = BASE_DIR/'data'/'raw'
    PROCESSED_DATA_DIR = BASE_DIR/'data'/'processed'
    MODELS_DIR = BASE_DIR/'models'

    API_BASE_URL = 'https://api.football-data.org/v4'
    FOOTBALL_DATA_API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')
    COMPETITION_CODE = "PL"
    CURRENT_SEASON = 2026
    API_CACHE_FILE = RAW_DATA_DIR/"api_matches_2026.json"

    API_TO_STANDARD_TEAM_NAMES = {
    "Manchester City FC": "Man City",
    "Manchester United FC": "Man United",
    "Newcastle United FC": "Newcastle",
    "Tottenham Hotspur FC": "Tottenham",
    "Wolverhampton Wanderers FC": "Wolves",
    "Nottingham Forest FC": "Nott'm Forest",
    "Brighton & Hove Albion FC": "Brighton",
    "West Ham United FC": "West Ham",
    "Aston Villa FC": "Aston Villa",
    "AFC Bournemouth": "Bournemouth",
    "Brentford FC": "Brentford",
    "Chelsea FC": "Chelsea",
    "Crystal Palace FC": "Crystal Palace",
    "Everton FC": "Everton",
    "Fulham FC": "Fulham",
    "Liverpool FC": "Liverpool",
    "Arsenal FC": "Arsenal",
    "Ipswich Town FC": "Ipswich",
    "Leicester City FC": "Leicester",
    "Southampton FC": "Southampton",
    "Leeds United FC": "Leeds",
    "Burnley FC": "Burnley",
    "Luton Town FC": "Luton",
    "Sheffield United FC": "Sheffield United",
    "Sunderland AFC": "Sunderland",
    "Coventry City FC": "Coventry City",
    "Hull City AFC": "Hull City"
}


