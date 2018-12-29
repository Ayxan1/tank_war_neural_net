import pygame
import json
class PlayerData():

    def __init__(self):
        # Creating coordinate database (json file) for data visualisation.
        self.x_filename = 'coordinate_x.json'
        self.y_filename = 'coordinate_y.json'
        self.collision_filename = 'collision_existance.json'
        self.tank_x_coordinates = []
        self.tank_y_coordinates = []
        self.collision = []


    def save_tank_coordinates(self, tank):
        self.tank_x_coordinates.append(tank.rect.centerx)
        self.tank_y_coordinates.append((800 - tank.rect.centery))
        
        if tank.right_wall_collision == True or  tank.left_wall_collision == True or tank.top_wall_collision == True or tank.bottom_wall_collision == True or tank.back_right_wall_collision == True or tank.back_left_wall_collision == True or tank.back_top_wall_collision == True or tank.back_bottom_wall_collision == True:
            self.collision.append(True)
        else:
            self.collision.append(False)
        


    def save_player_data_in_file(self):
        with open(self.x_filename, 'a') as file_object:
            json.dump(self.tank_x_coordinates, file_object)
        with open(self.y_filename, 'a') as file_object:
            json.dump(self.tank_y_coordinates, file_object)
        with open(self.collision_filename, 'a') as file_object:
            json.dump(self.collision, file_object)    
