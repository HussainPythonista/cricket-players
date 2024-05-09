from flask import Flask,jsonify
from data_file import player_list

from ops_file import Players

data=player_list

player=Players(data,6)



app=Flask(__name__)

@app.route("/")
def home():
    return jsonify(player.calculate_team_strength())

if __name__=="__main___":
    app.run(debug=True)