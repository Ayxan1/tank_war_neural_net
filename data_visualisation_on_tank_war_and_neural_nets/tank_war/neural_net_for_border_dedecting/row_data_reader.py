import json
with open('C:\\Users\\ayxan\\Documents\\current\\data_visualisation_python\\data_visualisation_on_tank_war\\tank_war\\coordinate_x.json', 'r') as file_object:
    data_x = json.load(file_object)
with open('C:\\Users\\ayxan\\Documents\\current\\data_visualisation_python\\data_visualisation_on_tank_war\\tank_war\\coordinate_y.json', 'r') as file_object:
    data_y = json.load(file_object)
with open('C:\\Users\\ayxan\\Documents\\current\\data_visualisation_python\\data_visualisation_on_tank_war\\tank_war\\collision_existance.json', 'r') as file_object:
    data_collision = json.load(file_object)

"""
print(data_x)
print("_______________________")
print(data_y)
print("_______________________")
print(data_collision)
print("_______________________")
print(len(data_collision))

for i in range(15):
    print(data_x[i])
"""

#data_set_NN = []
#data_set_NN.append([])

data_set_NN = [[] for _ in range(150)]

for i in range(150):
    data_set_NN[i].append(data_x[i])
    data_set_NN[i].append(data_y[i])
    if data_collision[i] == True:
        data_set_NN[i].append(1)
    else:
        data_set_NN[i].append(0)    




print(data_set_NN)

with open('training_data.json', 'a') as file_object:
            json.dump(data_set_NN, file_object)


