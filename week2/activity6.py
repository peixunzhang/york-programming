import pymongo

result = collection.find({'age':{'$lt': 25}})
for r in result:
    print
