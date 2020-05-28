import newpackage.MatchLoader as Matches
from newpackage.Constants import MAX_REQUESTS_IN_SECONDS, MAX_REQUESTS_IN_MINUTES
import time


class Extractor:
    match_loader = Matches.MatchLoader()

    def start(self, max_requests_in_seconds=MAX_REQUESTS_IN_SECONDS, max_requests_in_minutes=MAX_REQUESTS_IN_SECONDS):
        while True:
            self.load_a_minute()

    def load_a_second(self):
        starttime = time.time()
        functions = []
        for _ in range(MAX_REQUESTS_IN_SECONDS):
            self.match_loader.load_match()
        if time.time() < starttime + 1:
            time.sleep(starttime + 1 - time.time())

    def load_a_minute(self):
        starttime = time.time()
        for f in range(MAX_REQUESTS_IN_MINUTES // MAX_REQUESTS_IN_SECONDS):
            self.load_a_second()
        if time.time() < starttime + 60:
            time.sleep(starttime + 60 - time.time())
