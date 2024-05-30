from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017")

# Select the database and collections
database = client["Cricket_team"]
collection_team = database["players"]
collection_data = database["players_info"]

# Function to insert multiple documents
def insertMany(data):
    return collection_data.insert_many(data)



# Function to insert a single document
def insert_one(player_no=None, age=None, batting_rating=None, bowling_rating=None, name=None, wicket_keeper_rating=None):
    data_to_insert = {
        'player_no': player_no,
        "name": name,
        "age": age,
        "batting_rating": batting_rating,
        "bowling_rating": bowling_rating,
        "wicket_keeper_rating": wicket_keeper_rating
    }
    collection_data.insert_one(data_to_insert)
    return collection_data

# Function to get all documents
def get_all():
    all_data = []
    for single_data in collection_data.find():
        single_data['_id'] = str(single_data['_id'])
        all_data.append(single_data)
    return all_data


# Function to delete all documents from the team collection
def delete_all_team():
    return collection_team.delete_many({})

# Function to delete all documents from the players_info collection
def delete_all_data():
    return collection_data.delete_many({})

# Function to insert a team
def insert_team(team_name, players, rating_avg):
    team_data = {
        "team_name": team_name,
        "players": players,
        "Rating_avg": rating_avg
    }
    collection_team.insert_one(team_data)

# Function to get all teams
def get_teams():
    all_data = []
    for single_data in collection_team.find():
        single_data['_id'] = str(single_data['_id'])
        all_data.append(single_data)
    return all_data

# Function to get a single player data
def get_one_data(player_id):
    data = collection_data.find_one({'player_no': player_id}, {'_id': 0})
    return data

# Function to delete a single player data
def delete_one_record(player_id):
    if get_one_data(player_id) is None:
        return "No data to delete"
    else:
        collection_data.delete_one({'player_no': player_id})
        return "Successfully Deleted"

# Function to update player information
def update_player_info(player_no, age, batting_rating, bowling_rating, name, wicket_keeper_rating):
    filter_ = {"player_no": player_no}
    update_info = {'$set': {
        "name": name,
        "age": age,
        "batting_rating": batting_rating,
        "bowling_rating": bowling_rating,
        "wicket_keeper_rating": wicket_keeper_rating}}
    result = collection_data.update_one(filter_, update_info)
    if result.matched_count > 0:
        print(f"Updated player {player_no} successfully.")
    else:
        print(f"Player {player_no} not found.")

# Function to delete multiple selected players
def deleted_many_selected(list_data):
    query = {"player_no": {"$in": list_data}}
    return collection_data.delete_many(query)

def get_selected_data(list_data):
    query = {"player_no": {"$in": list_data}}

    selected_data = []
    for single_data in collection_data.find(query):
        single_data['_id'] = str(single_data['_id'])
        selected_data.append(single_data)
    return selected_data
     

