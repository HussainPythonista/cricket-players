from flask import Flask, jsonify, request
from flask_cors import CORS
import re
import db  # Assuming db.py contains the MongoDB operations
from ops_file import Players  # Assuming this contains the Players class

app = Flask(__name__)
CORS(app)

@app.route("/generate_post", methods=["POST"])
def generate_players_post():
    delete_team()
    data = request.get_json()
    number_team_requested = data["team"]
    all_players = db.get_all()

    total_players_length = len(all_players)
    max_teams = total_players_length // 11

    if max_teams == number_team_requested:
        players = Players(all_players, number_team_requested)
        teams = players.assign_players()
        for idx, team in enumerate(teams):
            avg = players.calculate_avg(team)
            db.insert_team(f"Team {idx+1}", team, avg)
        return jsonify(teams)
    elif max_teams < number_team_requested:
        return jsonify(f"You can generate only {max_teams} teams. Add {(number_team_requested * 11) - total_players_length} players to create {number_team_requested} teams.")
    else:
        players = Players(all_players, number_team_requested)
        teams = players.assign_players()
        for idx, team in enumerate(teams):
            avg = players.calculate_avg(team)
            db.insert_team(f"Team {idx+1}", team, avg)
        return jsonify(teams)

@app.route("/teams")
def get_teams():
    teams = db.get_teams()
    return jsonify(teams)

@app.route("/players")
def team():
    return jsonify(db.get_all())

@app.route("/insert_many", methods=["POST"])
def insert_many():
    data = request.get_json()
    db.insertMany(data)
    return jsonify({"message": "Successfully"})

@app.route("/insert_one", methods=["POST"])
def insert_one():
    data = request.get_json()
    player_no = data['player_no']
    name = data["name"]
    bowling_rating = float(data["bowling_rating"])
    batting_rating = float(data["batting_rating"])
    age = data["age"]
    wicket_keeper_rating = float(data["wicket_keeper_rating"])

    if db.get_one_data(player_no) is None:
        db.insert_one(player_no=player_no, name=name, age=age, wicket_keeper_rating=wicket_keeper_rating,
                      batting_rating=batting_rating, bowling_rating=bowling_rating)
        return jsonify({"message": "Inserted Successfully"})
    else:
        db.update_player_info(player_no=player_no, name=name, age=age, wicket_keeper_rating=wicket_keeper_rating,
                              batting_rating=batting_rating, bowling_rating=bowling_rating)
        return jsonify({"message": "Updated Successfully"})

@app.route("/delete_all_teams", methods=["DELETE"])
def delete_team():
    db.delete_all_team()
    return jsonify({"message": "All Teams deleted Successfully"})

@app.route("/delete_all_data", methods=["DELETE"])
def delete_data_all():
    db.delete_all_data()
    return jsonify({"message": "All Data deleted Successfully"})

@app.route("/delete_one_data/<id>", methods=["DELETE"])
def delete_data_one(id):
    id = int(id)
    return jsonify(db.delete_one_record(id))

@app.route("/one_student/<player_no>", methods=["GET"])
def one_player(player_no):
    player_no = int(player_no)
    single_player = db.get_one_data(player_no)
    return jsonify(single_player)

@app.route("/delete_selected/<list_data>", methods=["DELETE"])
def delete_selected(list_data):
    numbers = re.findall(r'\d+', list_data)
    numbers = [int(num) for num in numbers]
    numbers = list(set(numbers))
    db.deleted_many_selected(numbers)
    return jsonify("Deleted successfully")

@app.route("/edit_selected/<list_data>", methods=["GET"])
def get_selected(list_data):
    numbers = re.findall(r'\d+', list_data)
    numbers = [int(num) for num in numbers]
    numbers = list(set(numbers))
    return db.get_selected_data(numbers)
    
@app.route('/update_player_selected', methods=['POST'])
def update_player_selected():
    data_list = request.get_json()
    for data in data_list:
        player_no = data['player_no']
        name=data['name']
        age = data["age"]
        bowling_rating = float(data["bowling_rating"])
        batting_rating = float(data["batting_rating"])
        wicket_keeper_rating = float(data["wicket_keeper_rating"])

        db.update_player_info(player_no=player_no, age=age,name=name, batting_rating=batting_rating, bowling_rating=bowling_rating, wicket_keeper_rating=wicket_keeper_rating)
    return jsonify("Updated Succesfully")


@app.route('/bulk_update/<bulk_list>', methods=['POST'])
def bulk_update_selected(bulk_list):
    numbers = re.findall(r'\d+', bulk_list)
    numbers = [int(num) for num in numbers]
    numbers = list(set(numbers))
    
    data=request.get_json()
    bowling_rating = float(data["bowling_rating"])
    batting_rating = float(data["batting_rating"])
    wicket_keeper_rating = float(data["wicket_keeper_rating"])
    db.bulk_update(player_no=numbers,batting_rating=batting_rating,bowling_rating=bowling_rating,wicket_keeper_rating=wicket_keeper_rating)
    return jsonify("Bulk update Success")

if __name__ == "__main__":
    app.run(debug=True)
