from flask import Flask, jsonify, request
from ops_file import Players
import db

app = Flask(__name__)

@app.route("/generate_post", methods=["POST"])
def generate_players():
    """Generates teams of players based on the number of teams requested."""
    data = request.get_json()
    number_team_requested = data["team"]

    all_players = db.get_all()
    total_players_length = len(all_players)
    
    max_teams = total_players_length // 11

    if max_teams == number_team_requested:
        players = Players(all_players, number_team_requested)
        teams = players.assign_players()
        for idx, team in enumerate(teams):
            db.insert_team(f"Team {idx+1}", team)
        return jsonify(teams)
    
    elif max_teams < number_team_requested:
        return jsonify(f"You can generate only {max_teams} teams. Add {(number_team_requested * 11) - total_players_length} players to create {number_team_requested} teams.")
   
    else:
        players = Players(all_players, number_team_requested)
        teams = players.assign_players()
        for idx, team in enumerate(teams):
            db.insert_team(f"Team {idx+1}", team)
        return jsonify(teams)

@app.route("/teams")
def get_teams():
    """Retrieves all teams from the database and returns them as JSON."""
    teams = db.get_teams()
    return jsonify(teams)

if __name__ == "__main__":
    app.run(debug=True)
