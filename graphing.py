import matplotlib.pyplot as plt
import function as func
import pandas as pd
from time import time
from platform import system

class Graph:
    def __init__(self, points_data: list) -> None:
        self.points_data = points_data
       
    # def plt_maximize(self):
    #     # See discussion: https://stackoverflow.com/questions/12439588/how-to-maximize-a-plt-show-window-using-python
    #     backend = plt.get_backend()
    #     cfm = plt.get_current_fig_manager()
    #     if backend == "wxAgg":
    #         cfm.frame.Maximize(True)
    #     elif backend == "TkAgg":
    #         if system() == "Windows":
    #             cfm.window.state("zoomed")  # This is windows only
    #         else:
    #             cfm.resize(*cfm.window.maxsize())
    #     elif backend == "QT4Agg":
    #         cfm.window.showMaximized()
    #     elif callable(getattr(cfm, "full_screen_toggle", None)):
    #         if not getattr(cfm, "flag_is_max", None):
    #             cfm.full_screen_toggle()
    #             cfm.flag_is_max = True
    #     else:
    #         raise RuntimeError("plt_maximize() is not implemented for current backend:", backend)
    
    # graph each points 
    def graph_point(self) -> None:
        x_points = list(pd.DataFrame(self.points_data)[0])
        y_points = list(pd.DataFrame(self.points_data)[1])
        
        # make the limit for graphing
        x_max = max(x_points)
        x_min = min(x_points)
        
        y_max = max(y_points)
        y_min = min(y_points)
        
        plt.xlim(x_min - 2, x_max + 2)
        plt.ylim(y_min - 2, y_max + 2)
        
        plt.plot(x_points, y_points, color='black')
        
        # plot points (dot)
        plt.plot(x_points, y_points, 'o')
        
        
        # plot last point with first point
        last_stroke_x = [x_points[0], x_points[-1]]
        last_stroke_y = [y_points[0], y_points[-1]]
        plt.plot(last_stroke_x, last_stroke_y, color='black')
        
        # give the name of point in the graph
        for point in self.points_data:
            plt.text(point[0], point[1], f"{point}")
    
    # graph all the possibility
    def graph_all(self) -> None:
        # set time
        start = time()
        
        data_pos = list(func.Points(self.points_data).all_merge_length()['sequence'])
        data_length = list(func.Points(self.points_data).all_merge_length()['length'])
        
        # dummy variable for data_pos length
        data_pos_copy = data_pos.copy()
        length = len(data_pos_copy)
        
        
        # for better experince
        plt.rcParams["font.family"] = "Times New Roman"
        
        # optimization for data_pos greater than 300. The programs will slow down if this code not created
        if length > 300:
            data_pos = data_pos[length - 125:]
            data_length = data_length[length - 125:]
        
        # iteration count
        count = 1
        for index, points in enumerate(data_pos):
            if length > 300:
                plt.text(-3, -2.55, f"Note: Possibility array length is {length}. \nThe possibility data has been cut into last 125 data.")
            
            # fitness by list of points index
            plt.title(f"fitness = {data_length[index]} m\norder = {list(points)}\ncount = {count}", loc='left')
            
            count += 1
            
            Graph(points).graph_point()
            plt.pause(0.01)
            
            if count == 2:
                # Graph(points).plt_maximize()
                plt.pause(5)
            
            # clear the plot after executed
            if points != data_pos[-1]:
                plt.cla()
        
        plt.title(f"finished in = {round(time() - start, 5)} sec", loc='center')
        
        plt.show()
        
        
if __name__ == "__main__":
    data = [(1, 1), (2, 4), (9, 2), (16, 8), (13, 3), (13, 14), (31, 20)]
    Graph(data).graph_all()
