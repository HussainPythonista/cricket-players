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

def insert_one(player_no=None,age=None,batting_rating=None,bowling_rating=None,name=None,wicket_keeper_rating=None):
    
    data_to_insert={
        'player_no':player_no,"name":name,"age":age,"batting_rating":batting_rating,
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

def get_one_data(player_id):
    data=collection_data.find_one({'player_no':player_id},{'_id':0})
    if data==None:
        return None
    else:
        return data 

def delete_one_record(player_id):
    if get_one_data(player_id=player_id)==None:
        return "No data to delete"
    else:
        (collection_data.delete_one({'player_no':player_id}))
        return "Succesfully Deleted"

def update_player_info(player_no,age,batting_rating,bowling_rating,name,wicket_keeper_rating):
    filter_={"player_no":player_no}

    update_info={'$set':{
        "name":name,"age":age,"batting_rating":batting_rating,
        "bowling_rating":bowling_rating,"wicket_keeper_rating":wicket_keeper_rating}}
    collection_data.update_one(filter_,update_info)
    
def deleted_many_selected(list_data):
    query={"player_no": {"$in": list_data}}
    return collection_data.delete_many(query)

print(len(get_all()))