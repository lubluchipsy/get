import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import matplotlib.ticker as ticker

with open("settings.txt", "r") as sett:
    settings = [float(i) for i in sett.read().split('\n')]

volts = np.loadtxt("data.txt", dtype=int)*settings[1]
seconds = np.array([i*settings[0] for i in range(volts.size)])

fig, ax = plt.subplots(figsize=(16,10), dpi=400)

ax.axis([volts.min(), seconds.max()+1, volts.min(), volts.max()+0.2])

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

time1 = str(volts.argmax()*settings[0])
time2 = str((len(volts)-1-volts.argmax())*settings[0])
print(time1, time2)

ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC-цепочке', 60)), loc = 'center')
plt.text(8, 2, 'Время зарядки: ' + time1, fontsize=20)
plt.text(8, 1.8, 'Время разрядки: ' + time2, fontsize=20)

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

ax.plot(seconds, volts, c='blue', linewidth=1, label = 'V(t)')
ax.scatter(seconds[0:volts.size:25], volts[0:volts.size:25], marker = 's', c = 'red', s=15)

ax.legend(shadow = True, loc = 'right', fontsize = 30)

fig.savefig('graph.png')
fig.savefig('graph.svg')