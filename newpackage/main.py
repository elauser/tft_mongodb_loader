from newpackage.Riot import Riot
from newpackage.MatchLoader import MatchLoader
from newpackage.DB import DB
import time
import newpackage.Extractor
import cProfile
import pstats
import asyncio

def main():
    extractor = newpackage.Extractor.Extractor()
    extractor.start()

if __name__ == "__main__":
    main()

