from flask import Flask,jsonify,request
from data_file import player_list

from ops_file import Players
import db






app=Flask(__name__)



@app.route("/generate")
def generate_players():
    get_json=request.get_json()
    number_team_requested=get_json["team"]

    data=db.get_all()
    total_players_length=len(data)
    
    max_team=total_players_length//11

    if max_team==number_team_requested:
        players=Players(data,number_team_requested)
        return jsonify(players.assign_players())
    
    elif max_team<number_team_requested:
        return jsonify(f"You can generate only {max_team} teams add {(number_team_requested*11)-total_players_length} Players, to create {number_team_requested} team")
   
    else:
        players=Players(data,number_team_requested)
        return jsonify(players.assign_players())
    
@app.route("/generate")
def generate_players():

    """Generates teams of players based on the number of teams requested."""
    get_json=request.get_json()
    number_team_requested=get_json["team"]

    data=db.get_all()
    total_players_length=len(data)
    
    max_team=total_players_length//11

    if max_team==number_team_requested:
        players=Players(data,number_team_requested)
        return jsonify(players.assign_players())
    
    elif max_team<number_team_requested:
        return jsonify(f"You can generate only {max_team} teams add {(number_team_requested*11)-total_players_length} Players, to create {number_team_requested} team")
   
    else:
        players=Players(data,number_team_requested)
        return jsonify(players.assign_players())
    
    
@app.route("/")
def team():
    return jsonify(db.get_all())

@app.route("/insert_many",methods=["POST"])
def insert_many():
    data=request.get_json()
    db.insertMany(data)
    return jsonify({"message":"Successfully"})


@app.route("/delete_all",methods=["DELETE"])
def delete():
    db.delete_all()
    return jsonify({"message":"all Data deleted Successfully"})
if __name__=="__main___":
    app.run(debug=True)