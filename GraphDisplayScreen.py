from matplotlib import pyplot as plt
import csv
import matplotlib.animation as animation
import datetime
import time

BPM = [65,67,70,72,80,85,90,95,110,115]
TIME = [1,2,3,4,5,6,7,8,9,10]

SIEMENS = [2, 3, 4, 4.6, 6, 5.3, 4.4, 4, 5, 6.8]

RESPIRATION = [12, 12, 13, 15, 14, 17, 16, 15, 15, 20]

fig, (graph0, graph1, graph2, graph3)= plt.subplots(nrows=4, ncols=1, sharex=True)

fig.subplots_adjust(hspace=0)

#CSVPath = str(pathlib.Path().absolute())+'\TestData.csv'

'''f = open("test.csv", 'w')
CurrentTime = datetime.datetime.now()
CurrentTimeOrg = CurrentTime.strftime("%H:%M:%S")
counter = 0
while counter < 10:
    f.write(str(CurrentTimeOrg)+"\n")
    time.sleep(1)
    counter+=1
    print(counter)'''


def animate(i):
    x = []
    y = []
    with open('TestData.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))

        graph0.clear()
        graph1.clear()
        graph2.clear()
        graph3.clear()

        graph0.plot(x, y, color='b', marker='o')
        graph0.set_ylabel("BPM")

        graph1.plot(x, y, color='k', marker='o')
        graph1.set_ylabel("Siemens")

        graph2.plot(x, y, color='g', marker='o')
        graph2.set_ylabel("Respiration")

        graph3.plot(x, y, color='b', marker='o')
        graph3.set_ylabel("BPM")

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()


