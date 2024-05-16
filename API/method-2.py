from ops_file import Calculate

from data_file import player_list



data=player_list



calc=Calculate(data)

sorted_data=calc.sorted_data()

batting=sorted_data["Batting"]
bowling=sorted_data["Bowling"]
wk=sorted_data["Wicket_Keeper"]

sorted_batting=sorted(batting,key=lambda d:d["batting_rating"],reverse=True)
sorted_bowling=sorted(bowling,key=lambda d:d["bowling_rating"],reverse=True)
sorted_wk=sorted(wk,key=lambda d:d["wicket_keeper_rating"],reverse=True)

teams=[[],[],[],[],[]]


def pop_values(data_pop):

    global sorted_bowling,sorted_batting,sorted_wk

    #pop data from 
    for idx,wk in enumerate(sorted_wk):
        if wk["name"]==data_pop["name"]:
            del sorted_wk[idx]
            
    for idx,bowling in enumerate(sorted_bowling):
        if bowling["name"]==data_pop["name"]:
            del sorted_bowling[idx]
            
    for idx,batting in enumerate(sorted_batting):
        if batting["name"]==data_pop["name"]:
            del sorted_batting[idx]
            
   
for idx in range(len(teams)):
    poped_wicket=sorted_wk.pop(0)
    pop_values(poped_wicket)
    teams[idx].append(poped_wicket)


# # pop_values(data_pop=poped_wk)
while len(teams[-1])<11:
    for idx in range(len(teams)):
    
        poped_bat=sorted_batting.pop(0)
        poped_bow=sorted_bowling.pop(0)
        pop_values(poped_bat)
        pop_values(poped_bow)


        teams[idx].append(poped_bat)
        teams[idx].append(poped_bow)

#Check for teams
print(len(teams[0]))

# team_streangth=[]

# for i in range(len(teams)):
#     overall=0
#     for single_player in teams[i]:
#        overall+=single_player["Overall_rating"]
# # print(teams) 
#     team_streangth.append(overall)
# print(team_streangth)
            





