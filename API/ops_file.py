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
    

    # def calculate_overall(self,single_data):
    #     overall_ratting=0#single_data["batting_rating"]+single_data["bowling_rating"]+single_data["wicket_keeper_rating"]

    #     for data in single_data:
    #         overall_ratting+=data[]
    #     print(single_data)
    #     #return (overall_ratting/11)
    
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
        
        teams = self.number_of_team()
        team_size = len(teams)
        
        # Ensure each team has exactly 11 players
        #for i in range(11):
        while len(teams[-1])<11:
            # Slice the required number of batsmen and bowlers
            sliced_batsman = self.batting[:team_size * 2]
            sliced_bowler = self.bowling[:team_size * 2]
            
            for idx in range(team_size):
                #if len(teams[idx]) < 11:
                    # Assign a batsman from the front
                    poped_bat = sliced_batsman.pop(0)
                    self.__pop_values__(poped_bat)
                    teams[idx].append(poped_bat)
                    
                #if len(teams[idx]) < 11:
                    # Assign a batsman from the back
                    poped_bat = sliced_batsman.pop(-1)
                    self.__pop_values__(poped_bat)
                    teams[idx].append(poped_bat)
                    
                #if len(teams[idx]) < 11:
                    # Assign a bowler from the front
                    poped_bow = sliced_bowler.pop(0)
                    self.__pop_values__(poped_bow)
                    teams[idx].append(poped_bow)
                    
                #if len(teams[idx]) < 11:
                    # Assign a bowler from the back
                    poped_bow = sliced_bowler.pop(-1)
                    self.__pop_values__(poped_bow)
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

        #print(self.calculate_overall(json_data))
        rating_avg["Team_overall"]=round(self.calculate_team_strength(json_data)/11,2)
        return  rating_avg
    

    def calculate_team_strength(self,json_data):
        
        overall_team_strength=0
        for single_palyer in json_data:
            overall_team_strength+=single_palyer["batting_rating"]+single_palyer["bowling_rating"]+single_palyer["wicket_keeper_rating"]

        return overall_team_strength
    
# player_list=Players(data,7)
# print(player_list.assign_players())

# datas=[{'age': 39, 'batting_rating': 9, 'bowling_rating': 1, 'name': 'Kevin Pietersen', 'player_no': 65, 'wicket_keeper_rating': 1}, {'player_no': 2, 'name': 'Rohit Sharma', 'age': 31, 'batting_rating': 8, 'bowling_rating': 3, 'wicket_keeper_rating': 1}, {'player_no': 31, 'name': 'Sunil Narine', 'age': 29, 'batting_rating': 3, 'bowling_rating': 9, 'wicket_keeper_rating': 1}, {'player_no': 34, 'name': 'Brendon McCullum', 'age': 30, 'batting_rating': 3, 'bowling_rating': 9, 'wicket_keeper_rating': 1}, {'player_no': 45, 'name': 'Ricky Ponting', 'age': 34, 'batting_rating': 8, 'bowling_rating': 2, 'wicket_keeper_rating': 9}, {'player_no': 49, 'name': 'Jacques Kallis', 'age': 32, 'batting_rating': 8, 'bowling_rating': 2, 'wicket_keeper_rating': 9}, {'player_no': 38, 'name': 'Suresh Raina', 'age': 28, 'batting_rating': 3, 'bowling_rating': 8, 'wicket_keeper_rating': 1}, {'player_no': 39, 'name': 'MS Dhoni', 'age': 29, 'batting_rating': 4, 'bowling_rating': 8, 'wicket_keeper_rating': 1}, {'player_no': 
# 15, 'name': 'Chris Gayle', 'age': 28, 'batting_rating': 7, 'bowling_rating': 4, 'wicket_keeper_rating': 1}, {'player_no': 42, 'name': 'Zaheer Khan', 'age': 33, 'batting_rating': 7, 'bowling_rating': 2, 'wicket_keeper_rating': 8}, {'age': 42, 'batting_rating': 7, 'bowling_rating': 5, 'name': 'Matt Prior', 'player_no': 67, 'wicket_keeper_rating': 9}]

# print(len(datas))