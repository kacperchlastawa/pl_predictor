from src.config import Config
import requests
import json

class FootballDataClient:
    def __init__(self):
        self.headers = {"X-Auth-Token": Config.FOOTBALL_DATA_API_KEY}

    def get_matches(self, force_refresh: bool = False) -> dict:
        if force_refresh == False and Config.API_CACHE_FILE.exists():
            data = json.load(Config.API_CACHE_FILE.open('r'))
            print("Matches loaded from local cache file")
            return data
        else:
            match_url = f"{Config.API_BASE_URL}/competitions/{Config.COMPETITION_CODE}/matches"
            match_response = requests.get(match_url, headers = self.headers, params={"season": Config.CURRENT_SEASON})
            match_response.raise_for_status()

            matches_json = match_response.json()
            with open(Config.API_CACHE_FILE, 'w') as f: 
                json.dump(matches_json, f, indent=4)
            return matches_json
