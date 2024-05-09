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
        Function which return the players based on rating by batting,bowling,wiket keeper
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
    
    def check_can_split(self):

        length_data=len(data)

        if length_data%11==self.number_of_team:
            return self.number_of_team()
        else:
            return False

    #Calculate the number of teams which I want to create from the dataset
    def __number_of_team__(self):

        #number of teams
        list_teams=[]
        for _ in range(self.teams):
            list_teams.append([])

        #return number of teams with given N
        return list_teams

    def assign_players(self):
        teams=self.__number_of_team__()


        return self.sorted_data()
    
    def calculate_team_strength(self):
        team_data=self.assign_players()
        team_strength={}
        for idx in range(len(team_data)):
            total_strength=0
            for single_player in range(len(team_data[idx])):
                total_strength+=(team_data[idx][single_player]["Overall_rating"])
            team_strength[f"Team {idx}"]=total_strength
        return team_strength

player=Players(data,6)
sorted_data=player.assign_players()
team=[[],[],[],[],[]]


while  len(team[-1])<=10:
    for idx in range(5):
    
        team[idx].append(sorted_data["Batting"].pop(0))
        team[idx].append(sorted_data["Bowling"].pop(0))
        team[idx].append((sorted_data["Wicket_Keeper"].pop(0)))
        print(team[0])
print(len(team[-1]))
