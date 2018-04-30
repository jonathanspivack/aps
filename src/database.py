import pymongo


class Database:
    db = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient()
        Database.db = client.amazon

    @staticmethod
    def insert(collection,data):
        Database.db[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.db[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.db[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.db[collection].update(query,data,upsert=True)

    @staticmethod
    def remove(collection,query):
        Database.db[collection].remove(query)


