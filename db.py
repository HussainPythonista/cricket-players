from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

database=client["Cricket_team"]
collection=database["players"]

def insertMany(data):
    return collection.insert_many(data)
    #print("success")

def get_all():
    all_data=[]
    for single_data in collection.find():
        single_data['_id'] = str(single_data['_id'])
        all_data.append(single_data)
    return all_data


def delete_all():
    return collection.delete_many({})
print(get_all())