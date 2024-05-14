from data_file import player_list



data=player_list
#Overall Rating
class Calculate:

    '''
    The `Calculate` class initializes with a dataset (list of player data).
    - It defines a method `calculate_overall` that calculates the overall 
        rating of a player based on their batting,bowling, and wicket-keeper ratings.
    - The `single_data_assign` method iterates through each player's data, calculates 
        their overalPl rating, and updates the player's data with the overall rating.
    - It then sorts the player data based on the overall rating in descending order and returns the sorted data.
    '''
    def __init__(self,dataset):
        self.data=dataset
    

    def calculate_overall(self,single_data):
        overall_ratting=single_data["batting_rating"]+single_data["bowling_rating"]+single_data["wicket_keeper_rating"]

        return (overall_ratting)
    
    def final_data(self):
        for index,single_data in enumerate(self.data):
            overall_returned_data=self.calculate_overall(single_data)
            data[index]["Overall_rating"]=overall_returned_data
    

        sorted_data=sorted(data, key=lambda sort: sort['Overall_rating'],reverse=True)
        return sorted_data
    
    def sorted_data(self):
        '''
        Function which return the players based on rating by batting,bowling,wicket keeper
        '''
        final_sorted_data={}
        final_sorted_data["Batting"]=sorted(data,key=lambda sort:sort["batting_rating"],reverse=True)
        final_sorted_data["Bowling"]=sorted(data,key=lambda sort:sort["bowling_rating"],reverse=True)
        final_sorted_data["Wicket_Keeper"]=sorted(data,key=lambda sort:sort["wicket_keeper_rating"],reverse=True)
        return final_sorted_data


# print(sorted_data)

class Players(Calculate):
    '''
    Class Explanation:
    - The `Players` class inherits from the `Calculate` class.
    - It initializes with a dataset and the number of teams (default is None).
    - The `number_of_team` method creates a list of empty lists, with each sublist representing a team.
    - The `assign_players` method calls the `single_data_assign` method to get the sorted player data.
    - It then calls `number_of_team` to get the team structure and returns the sorted player data.

    Execution:
    - An instance of the `Players` class is created with the player data and the number of teams (3).
    - The `assign_players` method is called, which sorts the players based on their overall rating and returns the sorted player data.
    - The sorted player data is then printed, showing the players grouped into teams based on their overall ratings.

    '''
    
    def __init__(self,dataset,number_teams=None):

        #Inherit Superclass
        super().__init__(dataset)
        self.teams=number_teams
        self.sorted_data=self.sorted_data()

        self.batting=self.sorted_data["Batting"]
        self.bowling=self.sorted_data["Bowling"]
        self.wk=self.sorted_data["Wicket_Keeper"]

        
    def check_can_split(self):

        length_data=len(data)

        if length_data%11==self.number_of_team:
            return self.number_of_team()
        else:
            return False

    #Calculate the number of teams which I want to create from the dataset
    def number_of_team(self):
        
        list_teams=[]
        for _ in range(self.teams):
            list_teams.append([])

        #return number of teams with given N
        return list_teams
        
    def __pop_values__(self,data_pop):

        global batting,bowling,wk

        #pop data from 
        for idx,wk in enumerate(self.wk):
            if wk["name"]==data_pop["name"]:
                del self.wk[idx]
                
        for idx,bowling in enumerate(self.bowling):
            if bowling["name"]==data_pop["name"]:
                del self.bowling[idx]
                
        for idx,batting in enumerate(self.batting):
            if batting["name"]==data_pop["name"]:
                del self.batting[idx]
    
    def assign_players(self):

        #First assign the wicket keepers
        teams=self.number_of_team()
        for idx in range(len(teams)):
            poped_wicket=self.wk.pop(0)
            self.__pop_values__(poped_wicket)
            teams[idx].append(poped_wicket)

        #Assign other players
        while len(teams[-1])<11:
            for idx in range(len(teams)):
            
                poped_bat=self.batting.pop(0)
                poped_bow=self.bowling.pop(0)
                self.__pop_values__(poped_bat)
                self.__pop_values__(poped_bow)
                teams[idx].append(poped_bat)
                teams[idx].append(poped_bow)

        return teams
    def calculate_avg(self,json_data):
        rating_avg={}
        total=0
        for single_player in json_data:
            total+=single_player["batting_rating"]
        rating_avg["batting"]= round(total/11,2)

        total=0
        for single_player in json_data:
            total+=single_player["bowling_rating"]
        rating_avg["bowling"]= round(total/11,2)

        total=0
        for single_player in json_data:
            total+=single_player["wicket_keeper_rating"]
        rating_avg["wicket_keeper"]=round(total/11,2)

        return  rating_avg
    
    
    def calculate_team_strength(self):
        team_data=self.assign_players()
        team_strength={}
        for idx in range(len(team_data)):
            total_strength=0
            for single_player in range(len(team_data[idx])):
                total_strength+=(team_data[idx][single_player]["Overall_rating"])
            team_strength[f"Team {idx}"]=total_strength
        return team_strength

# player=Players(data,5)
# #print(len(player.assign_players()[0]))

# print(player.assign_players()[0])
# # for  single in player.assign_players()[0]:
# #     print(single["name"])

# calc=Calculate(data)

# sorted_data=calc.sorted_data()

# batting=sorted_data["Batting"]
# bowling=sorted_data["Bowling"]
# wk=sorted_data["Wicket_Keeper"]

# sorted_batting=sorted(batting,key=lambda d:d["batting_rating"],reverse=True)
# sorted_bowling=sorted(bowling,key=lambda d:d["bowling_rating"],reverse=True)
# sorted_wk=sorted(wk,key=lambda d:d["wicket_keeper_rating"],reverse=True)

# #Assign only wicket Keeper

# teams=[[],[],[],[],[]]

