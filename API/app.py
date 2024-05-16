from flask import Flask,jsonify,request
from data_file import player_list

from ops_file import Players
import db



app=Flask(__name__)



def calculate_avg(team):
    return "done"
@app.route("/generate_post", methods=["POST"])
def generate_players_post():

    """Generates teams of players based on the number of teams requested."""
    data = request.get_json()
    number_team_requested = data["team"]

    all_players = db.get_all()
    total_players_length = len(all_players)
    
    max_teams = total_players_length // 11

    if max_teams == number_team_requested:
        players = Players(all_players, number_team_requested)
        teams = players.assign_players()
        battingAvg=0
        for idx, team in enumerate(teams):
            avg=players.calculate_avg(team)
            
            db.insert_team(f"Team {idx+1}", team,avg)
            
        return jsonify(teams)
    
    elif max_teams < number_team_requested:
        return jsonify(f"You can generate only {max_teams} teams. Add {(number_team_requested * 11) - total_players_length} players to create {number_team_requested} teams.")
   
    else:
        players = Players(all_players, number_team_requested)
        teams = players.assign_players()
        for idx, team in enumerate(teams):
            avg=players.calculate_avg(team)
            db.insert_team(f"Team {idx+1}", team,avg)
            
        return jsonify(teams)



#Retrive the information of team with Players
@app.route("/teams")
def get_teams():
    """Retrieves all teams from the database and returns them as JSON."""
    teams = db.get_teams()
    return jsonify(teams)

@app.route("/")
def team():
    return jsonify(db.get_all())




#Insert data into main Collection
@app.route("/insert_many",methods=["POST"])
def insert_many():
    data=request.get_json()
    db.insertMany(data)
    return jsonify({"message":"Successfully"})



@app.route("/insert_one",methods=["POST"])
def insert_one():
    data=request.get_json()
    
    name=data["name"]
    bowling_rating=int(data["bowling_rating"])
    batting_rating=int(data["batting_rating"])
    age=data["age"]
    wicket_keeper_rating=int(data["wicket_keeper_rating"])
    
    db.insert_one(name=name,age=age,wicket_keeper_rating=wicket_keeper_rating,batting_rating=batting_rating,bowling_rating=bowling_rating)
    return jsonify({"message":"Inserted Succesfully"})
    

@app.route("/delete_all_teams",methods=["DELETE"])
def delete_team():
    db.delete_all_team()
    return jsonify({"message":"All Teams deleted Successfully"})



@app.route("/delete_all_data",methods=["DELETE"])
def delete_data():
    db.delete_all_data()
    return jsonify({"message":"All Data deleted Successfully"})
if __name__=="__main___":
    app.run(debug=True)