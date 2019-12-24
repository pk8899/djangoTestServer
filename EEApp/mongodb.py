from pymongo import MongoClient
from pprint import pprint
mongoClient=MongoClient("mongodb://localhost:27020")
db=mongoClient.admin

sysStatus=db.command("serverStatus")
pprint(sysStatus)