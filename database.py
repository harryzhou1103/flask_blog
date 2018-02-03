import pymongo

'''
classmethod pass the class of object instance as the first argument
you can call it from the class rather than a class instance

'''
class Database(object):
    host = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.host)
        Database.DATABASE = client["fullstack"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
