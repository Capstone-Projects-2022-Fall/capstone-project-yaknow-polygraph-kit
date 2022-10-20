from matplotlib import pyplot as plt

BPM = [65,67,70,72,80,85,90,95,110,115]
TIME = [1,2,3,4,5,6,7,8,9,10]

SIEMENS = [2, 3, 4, 4.6, 6, 5.3, 4.4, 4, 5, 6.8]

RESPIRATION = [12, 12, 13, 15, 14, 17, 16, 15, 15, 20]

fig, (graph0, graph1, graph2) = plt.subplots(nrows= 3, ncols=1)

graph0.plot(TIME, BPM)
graph0.set_xlabel("Time (minutes)")
graph0.set_ylabel("BPM")

graph1.plot(TIME, SIEMENS)
graph1.set_xlabel("Time (minutes)")
graph1.set_ylabel("Siemens")

graph2.plot(TIME, RESPIRATION)
graph2.set_xlabel("Time (minutes)")
graph2.set_ylabel("Respiration")

plt.tight_layout()

plt.show()