import numpy as np
from plot import animat
import get_output
from pathlib import Path

# Open LAMMPS ave/chunk out file
print("Enter 'e' or 'exit' to exit program")
while True:
    user_input = input('Enter file name:')
    if user_input == 'e' or user_input == 'exit':
        print('Exit program!')
        exit()
    elif Path(user_input).is_file():
        data = open(user_input, 'r')
        break
    else:
        print('File does not exist')

# read file
# comment and 2 headers
data.readline()
first_header = data.readline().lstrip('# ').rstrip('\n').split(' ')
second_header = data.readline().lstrip('# ').rstrip('\n')
# main part
timestep = []  # list of timestep
all_step = []  # list of data in each timestep
data_line = data.readline()
while data_line:
    time_header = data_line.lstrip(' ').rstrip('\n').split(' ')
    time_header = [int(i) for i in time_header]
    timestep.append(time_header[0])
    every_step = []
    for row in range(time_header[1]):  # read data in each timestep
        data_line = data.readline().lstrip(' ').rstrip('\n').split(' ')
        every_step.append(data_line)
    all_step.append(every_step)
    data_line = data.readline()

data_array = np.array(all_step, dtype=np.float64)  # convert data list to np array

while True:
    print('''
----------------------
Select option number:
1) Animation
2) Single output
3) Series output
4) Exit''')
    task = input('-->')
    if task == '1':
        animat(data_array, timestep, second_header)  # make animate plot
    elif task == '2':
        get_output.single(data_array, timestep, second_header)
    elif task == '3':
        get_output.series(data_array, timestep, second_header)
    else:
        print('Exit code!')
        exit()
