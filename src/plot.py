import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def animat(data, step, colname):
    data = np.copy(data)
    print('''
-----Animation-----
Enter 'b' or 'back' to return to main menu
Select two column to plot in format x-y (e.g. 2-4)''')
    colname = colname.split(' ')
    text = 'Column list:\n'
    for i in range(len(colname)):
        text += '{}) {}\t'.format(i, colname[i])
        if (i + 1) % 3 == 0: text += '\n'
    print(text)
    while True:
        try:
            user_input = input('Enter x-y:').split('-')
            if user_input[0] == 'back' or user_input[0] == 'b':
                print('Back to menu!')
                return
            elif user_input[0] == 'exit' or user_input[0] == 'e':
                exit()

            colx, coly = user_input
            colx, coly = int(colx), int(coly)

            fig, ax = plt.subplots()

            x = data[0, :, colx]
            y = data[0, :, coly]
            line, = ax.plot(x, y)

            # auto boundary:
            miny, maxy = data[0, :, coly].min(), data[0, :, coly].max()
            for i in range(data.shape[0]):
                if data[i, :, coly].min() < miny: miny = data[i, :, coly].min()
                if data[i, :, coly].max() > maxy: maxy = data[i, :, coly].max()
            print(miny, maxy)
            lengthy = maxy - miny
            ax.set(ylim=[(miny - 0.2 * lengthy), (maxy + 0.2 * lengthy)], xlabel=colname[colx], ylabel=colname[coly])

            time_text = ax.text(0.7, 0.95, 'Timestep: {}'.format(step[0]), transform=ax.transAxes)

            def animate(i):
                line.set_ydata(data[i, :, coly])  # update the data.
                time_text.set_text('Timestep: {}'.format(step[i]))
                return line, time_text,

            ani = animation.FuncAnimation(
                fig, animate, frames=data.shape[0], interval=100, blit=True, save_count=50)

            ani.save(filename="animated_plot.html", writer="html")
            print('Output created: animated_plot.html')
            plt.show()
            return

        except Exception as error:
            error_name = type(error).__name__
            if error_name == 'ValueError':
                print('Wrong entry, please enter x-y column number (e.g. 2-10))')
            elif error_name == 'IndexError':
                print('Column number out of range')
            else:
                print('--> Error:', error)
