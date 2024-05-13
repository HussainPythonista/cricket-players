from ops_file import Players

from data_file import player_list



data=player_list
players=Players(data,6)

sorted_dataset=players.assign_players()

teams=[[],[],[],[],[],[]]
for _ in range(11):
    for team in range(len(teams)):
        teams[team].append(sorted_dataset.pop(0))

for single_player in teams[0]:
    print(single_player["name"])