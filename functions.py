from itertools import permutations
from functools import cache
import pandas as pd
from math import sqrt

class Points:
    def __init__(self, points_data: list) -> None:
        # convert to tuple for each point to prevent error
        self.points_data = [tuple(point) for point in points_data]
    
    # check if the function is have 
    def inspector(self) -> None:
        for i in self.points_data:
            if self.points_data.count(i) > 1:
                raise ValueError(f"{i} is duplicated {self.points_data.count(i)} times. Please use non-duplicated point!")
    
    # display points in terminal
    def points_dataframe(self) -> pd.DataFrame:
        # prevent for errorness
        Points(self.points_data).inspector()
        
        key = {'point' : self.points_data}
        df = pd.DataFrame(key)
        return df
        
    # length betweenn two points
    def points_length(self, point1: tuple, point2: tuple) -> int:
        # prevent for errorness
        Points(self.points_data).inspector()
        
        length_x = point1[0] - point2[0]
        length_y = point1[1] - point2[1]
        
        length = sqrt(length_x**2 + length_y**2)
        return length    
        
    # all possible combination
    def all_permutation_length(self) -> pd.DataFrame:
        # prevent for errorness
        Points(self.points_data).inspector()
        
        
        # make list
        perm_data = list(permutations(self.points_data))
        
        # calculate the length each possibility
        list_of_length = []
        for possibility in perm_data:
            length = 0
            for point in range(len(possibility)): # for the index
                # if the point reach last index, make an exception
                if point == len(possibility) - 1:
                    length += Points(self.points_data).points_length(possibility[0], possibility[point])
                
                else:    
                    length += Points(self.points_data).points_length(possibility[point], possibility[point + 1])
            
            list_of_length.append(round(length, 4))
        
        # diplay the length and point sequence
        key = {'sequence' : perm_data, 'length' : list_of_length}
        df = pd.DataFrame(key)
        
        # ascending
        return df.sort_values(by='length')


    # if the reluts of function above is have points with same length, then merge it to one.
    def all_merge_length(self) -> pd.DataFrame:
        # prevent for errorness
        Points(self.points_data).inspector()
        
        length_data = Points(self.points_data).all_permutation_length()
        
        
        # filter by length
        # delete and keep the first length where have duplicate items
        filtered_data = length_data.drop_duplicates(subset='length', keep='first').sort_values('length', ascending=False)
        return filtered_data
    

if __name__ == "__main__":
    data = [(1, 1), (1, 4), (9, 2), (8, 7), (1, 5)]
    print(Points(data).all_merge_length())
