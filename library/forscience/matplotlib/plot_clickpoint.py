import matplotlib.pyplot as plt
def onclick(event):
    plt.scatter(event.xdata,event.ydata)

fig = plt.figure()
plt.xlim([0,10])
plt.ylim([0,10])
fig.canvas.mpl_connect('button_press_event',onclick)
