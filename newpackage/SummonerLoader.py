from newpackage.Riot import Riot
from newpackage.Singleton import Singleton
from newpackage.DB import DB


class SummonerLoader(metaclass=Singleton):
    ignore_summoners = []
    new_summoners = []
    db = DB()

    def __init__(self):
        self.__import_ignore_summoners()
        self.__import_new_summoners()

    def __import_ignore_summoners(self):
        ids = self.db.get_ignore_summoner_puuids()

        for _id in ids:
            self.ignore_summoners.append(_id)

    def __import_new_summoners(self):
        ids = self.db.get_new_summoner_puuids()

        for _id in ids:
            self.new_summoners.append(_id)

    def load_from_match(self, match: dict):
        for summoner in match['info']['participants']:
            if summoner['puuid'] not in self.ignore_summoners:
                self.new_summoners.append(summoner['puuid'])
        self.__persist_new_summoners()

    def save_finished_summoner(self, puuid):
        self.db.save_summoner({'_id': puuid, 'loaded': True})
        self.ignore_summoners.append(puuid)

    def __persist_new_summoners(self):
        for puuid in self.new_summoners:
            self.db.save_summoner({'_id': puuid, 'loaded': False})
            self.ignore_summoners.append(puuid)

    def get_fresh_summoner(self):
        return self.new_summoners.pop()