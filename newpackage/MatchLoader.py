from newpackage.Riot import Riot
from newpackage.Singleton import Singleton
from newpackage.DB import DB
from multiprocessing import Process
import newpackage.SummonerLoader as SummonerLoader
import asyncio


class MatchLoader(metaclass=Singleton):
    ignore_matches = []
    new_matches = []
    db = DB()
    summonerLoader = SummonerLoader.SummonerLoader()

    def __init__(self):
        self.__import_ignore_matches()
        if len(self.ignore_matches) == 0:
            self.__load_from_puuid(Riot.get_summoner_puuid(Riot, 'xOnionx'))


    """
    def __load_from_name(self, summoner_name):
        for match in Riot.get_matches(Riot, Riot.get_puuid(Riot, summoner_name)):
            if match not in self.ignore_matches:
                self.new_matches.append(match)
        self.__persist_matches()
    """

    def __load_from_puuid(self, puuid):
        for match in Riot.get_match_history(Riot, puuid):
            if match not in self.ignore_matches:
                self.new_matches.append(match)

    def __import_ignore_matches(self):
        ids = self.db.get_match_ids()

        for _id in ids:
            self.ignore_matches.append(_id)

    def load_match(self):
        while not self.new_matches:
            summoner = self.summonerLoader.get_fresh_summoner()
            self.__load_from_puuid(summoner)
            self.summonerLoader.save_finished_summoner(summoner)
        match_id = self.new_matches.pop()
        self.ignore_matches.append(match_id)
        self.persist_match_with_id(match_id)

    def __persist_matches(self):
        for match in self.new_matches:
            matchDict = Riot.get_match(Riot, match)
            self.db.save_match(matchDict)
            self.ignore_matches.append(match)
            self.summonerLoader.load_from_match(matchDict)
        self.new_matches = []

    def persist_match_with_id(self, match_id):
        match_dict = Riot.get_match(Riot, match_id)
        self.db.save_match(match_dict)
        self.summonerLoader.load_from_match(match_dict)
        print(f"Loaded Match {match_id}")
