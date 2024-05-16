from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

database=client["Cricket_team"]

collection_team=database["players"]

collection_data=database["players_info"]

def insertMany(data):
    return collection_data.insert_many(data)
    

def get_all():
    all_data=[]
    for single_data in collection_data.find():
        single_data['_id'] = str(single_data['_id'])
        all_data.append(single_data)
    return all_data

def insert_one(age=None,batting_rating=None,bowling_rating=None,name=None,wicket_keeper_rating=None):
    data_to_insert={
        "name":name,"age":age,"batting_rating":batting_rating,
        "bowling_rating":bowling_rating,"wicket_keeper_rating":wicket_keeper_rating
        }
    
    collection_data.insert_one(data_to_insert)
    return collection_data

def delete_all_team():
    return collection_team.delete_many({})
# Find the first document where the "name" field is "Alice"
# document = collection.find_one({"name": "Batsman-60"})
def delete_all_data():
    return collection_data.delete_many({})

def insert_team(team_name, players,rating_avg):
    """Inserts a team into the database."""
    team_data = {
        "team_name": team_name,
        "players": players,
        "Rating_avg":rating_avg
    }
    collection_team.insert_one(team_data)

def get_teams():
    """Retrieves all teams from the database."""
    
    all_data=[]
    for single_data in collection_team.find():
        single_data['_id'] = str(single_data['_id'])
        all_data.append(single_data)
    return all_data


print(len(get_all()))