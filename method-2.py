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
            
    #return sorted_bat,sorted_bow,sorted_wk

# for _ in range(11):
#     for idx in range(len(teams)):
#             print(_,idx)
# poped_wk=sorted_wk.pop(0)

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

team_streanght=[]

for i in range(len(teams)):
    overall=0
    for single_player in teams[i]:
       overall+=single_player["Overall_rating"]
# print(teams) 
    team_streanght.append(overall)
print(team_streanght)
            
# print(sorted_wk)



# #Assign only wicket Keeper
# for idx in range(len(teams)):
#     poped_player=sorted_wk.pop(0)
#     name=poped_player["name"]
    
#     for bowling in sorted_bowling:
#         if name==bowling["name"]:
#             sorted_bowling.remove(bowling)
#             print("Success")
#             break  
#     for batting in sorted_batting:
#         if name==batting["name"]:
#             sorted_batting.remove(batting)
#             print("Success")
#             break  
#     teams[idx].append(poped_player)
        
# for idx in range(len(teams)):
#     while len(teams[-1])<=11:
#         poped_player_bowling=sorted_bowling.pop(0)
#         poped_player_batting=sorted_bowling.pop(0)
        
        
#         for wk in sorted_wk:
#             if poped_player_bowling["name"]==wk["name"]:
#                 sorted_wk.remove(wk)
#                 print("Success")
#                 break  
#         for batting in sorted_batting:
#             if poped_player_bowling["name"]==batting["name"]:
#                 sorted_batting.remove(batting)
#                 print("Success")
#                 break  
#         teams[idx].append(poped_player_bowling)

# print(teams[0])




