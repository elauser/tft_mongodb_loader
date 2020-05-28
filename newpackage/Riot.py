try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import newpackage.Constants as Constants


class Riot:
    @staticmethod
    def __get_jsonparsed_data(cls, url: str):
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    @staticmethod
    def get_summoner_puuid(cls, username: str):
        url = f"https://{Constants.SUMMONER_REGION}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{username}?api_key={Constants.API_KEY}"
        return cls.__get_jsonparsed_data(Riot, url)['puuid']

    @staticmethod
    def get_match_history(cls, puuid: str):
        url = f"https://{Constants.TFT_REGION}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={Constants.MAX_MATCHES}&api_key={Constants.API_KEY}"
        return cls.__get_jsonparsed_data(Riot, url)

    @staticmethod
    def get_match(cls, matchId: str):
        url = f"https://{Constants.TFT_REGION}.api.riotgames.com/tft/match/v1/matches/{matchId}?api_key={Constants.API_KEY}"
        return cls.__get_jsonparsed_data(Riot, url)
