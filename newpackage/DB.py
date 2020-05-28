from newpackage.Singleton import Singleton
from pymongo import MongoClient
import newpackage.Constants as Constants
import time
import threading


class DB(metaclass=Singleton):
    client = None
    db = None

    def __init__(self):
        self.client = MongoClient(Constants.DB_URI)
        self.db = self.client[Constants.DB_NAME]

    def save_match(self, match: dict):
        try:
            match['_id'] = match['metadata']['match_id']
            self.db['matches'].insert_one(match)
        except:
            print(f"Failed to insert Match {match['_id']}")

    def get_match_ids(self) -> list:
        matches = []
        for match in self.db['matches'].find({}, {'_id': 1}):
            matches.append(match['_id'])
        return matches

    def get_ignore_summoner_puuids(self):
        puuids = []
        for summoner in self.db['summoners'].find({'loaded': True}, {'_id': 1}):
            puuids.append(summoner['_id'])
        return puuids

    def get_new_summoner_puuids(self):
        puuids = []
        for summoner in self.db['summoners'].find({"loaded": False}, {"_id": 1}):
            puuids.append(summoner['_id'])
        return puuids

    def save_summoner(self, summoner):
        summoner['time_stamp'] = time.time()
        filter = {'_id': summoner['_id']}
        try:
            self.db['summoners'].replace_one(filter, summoner, True)
        except:
            print(f"Failed to insert Summoner {summoner}")
