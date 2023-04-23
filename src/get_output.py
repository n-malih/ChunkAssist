import numpy as np
from pathlib import Path


def checkpath():
    folder = Path('time_series')
    if folder.is_dir():
        return
    else:
        folder.mkdir()


def single(data_array, timestep, second_header):
    checkpath()
    print('''
-----Single output-----
Enter 'b' or 'back' to return to main menu
To extract data to a file, choose a timestep''')
    print('(First: {first} - Last: {last} - Every: {every})'.format(first=timestep[0], last=timestep[-1],
                                                                  every=(timestep[1] - timestep[0])))
    while True:
        user_input = input('Enter timestep:')
        if user_input == 'back' or user_input == 'b':
            print('Back to menu!')
            return
        elif user_input == 'exit' or user_input == 'e':
            exit()
        try:
            user_input = int(user_input)
            i_step = timestep.index(user_input)
            np.savetxt('time_series\\{}.txt'.format(timestep[i_step]), data_array[i_step],
                       header='{}\n{}'.format(timestep[i_step], second_header), comments='')
        except Exception as error:
            print('Wrong timestep, enter timestep (e.g. 100)', error)


def series(data_array, timestep, second_header):
    checkpath()
    print('''
-----Series output-----
Enter 'b' or 'back' to return to main menu
Choose a timestep range to split the data into files
in format first-last-every (e.g. 100-500-100)''')
    print('(First: {first} - Last: {last} - Every: {every})'.format(first=timestep[0], last=timestep[-1],
                                                                  every=(timestep[1] - timestep[0])))
    while True:
        user_input = input('Enter first-last-every timestep:').split('-')
        if user_input[0] == 'back' or user_input[0] == 'b':
            print('Back to menu!')
            return
        elif user_input[0] == 'exit' or user_input[0] == 'e':
            exit()

        try:
            first, last, every = int(user_input[0]), int(user_input[1]), int(user_input[2])
            for mystep in range(first, (last + every), every):
                i_step = timestep.index(mystep)
                np.savetxt('time_series\\{}.txt'.format(timestep[i_step]), data_array[i_step],
                           header='{}\n{}'.format(timestep[i_step], second_header), comments='')
        except Exception as error:
            error_name = type(error).__name__
            print(error, error_name)
            print('Wrong entry, enter first-last-every (e.g. 100-500-100)')
