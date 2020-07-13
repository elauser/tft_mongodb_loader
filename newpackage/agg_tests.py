# Requires the PyMongo package.
# https://api.mongodb.com/python/current
from pymongo import *
import time
import re


print("Starting Aggregating")
t1 = time.clock()
"""
#time 36min

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
result = client['tft']['matches'].aggregate([
    {
        '$project': {
            '_id': False, 
            'metadata.match_id': True, 
            'info.participants': True
        }
    }, {
        '$unwind': {
            'path': '$info.participants', 
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$project': {
            '_id': False, 
            'metadata.match_id': True, 
            'info.participants.puuid': True, 
            'info.participants.units': True, 
            'info.participants.placement': True
        }
    }, {
        '$unwind': {
            'path': '$info.participants.units', 
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$group': {
            '_id': {
                'unitName': '$info.participants.units.name', 
                'unitTier': '$info.participants.units.tier'
            }, 
            'avgPosition': {
                '$avg': '$info.participants.placement'
            }
        }
    }, {
        '$out': 'aggs'
    }
])
"""
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
"""
#time 41,24
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
result = client['tft']['matches'].aggregate([
    {
        '$project': {
            '_id': False,
            'metadata.match_id': True,
            'info.participants': True
        }
    }, {
        '$unwind': {
            'path': '$info.participants',
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$project': {
            '_id': False,
            'metadata.match_id': True,
            'info.participants.puuid': True,
            'info.participants.units': True,
            'info.participants.placement': True
        }
    }, {
        '$unwind': {
            'path': '$info.participants.units',
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$unwind': {
            'path': '$info.participants.units.items',
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$group': {
            '_id': {
                'unitName': '$info.participants.units.name',
                'itemName': '$info.participants.units.items'
            },
            'avgPosition': {
                '$avg': '$info.participants.placement'
            }
        }
    }, {
        '$out': 'aggs'
    }
])
"""

"""
# 00:07,02

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
result = client['tft']['matches'].aggregate([
    {
        '$count': 'metadata'
    }, {
        '$out': 'aggs'
    }
])
"""
"""
#time 35.64641153666666
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
result = client['tft']['matches'].aggregate([
    {
        '$project': {
            '_id': False,
            'metadata.match_id': True,
            'info.participants': True
        }
    }, {
        '$unwind': {
            'path': '$info.participants',
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$project': {
            '_id': False,
            'metadata.match_id': True,
            'info.participants.puuid': True,
            'info.participants.units': True
        }
    }, {
        '$unwind': {
            'path': '$info.participants.units',
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$match': {
            'info.participants.units.name': re.compile(r".*[Aa].*[Ee].*")
        }
    }, {
        '$group': {
            '_id': '$info.participants.units.name'
        }
    }, {
        '$out': 'aggs'
    }
])
"""

"""
#time 17 minutes. Code for Python does not 100% work, this was done in the shell

#db.matches.updateMany({},{$set:{"info.participants.$[].units.$[un].name": "Richard"}},{upsert: false, arrayFilters:[{"un.name":"Malphite"}]})


client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
client['tft']['matches'].update_many(
    {},
    {'$set': {'info.participants.$[].units.$[un].name': 'Richard'}},
    {
        'upsert': False,
        'arrayFilters': {"un.name": "Malphite"}
    }
)
"""

t2 = (time.clock() - t1)/60
print(t2)
