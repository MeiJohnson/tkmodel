import matplotlib as mpl
import matplotlib.pyplot as plt
import math

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 60, 0, 100])

plt.title('Закон теплопроводности')
plt.xlabel('t')
plt.ylabel('T(t)')

xs = []
vals = []

temp = 22-83
x = 0.0
while x < 60.0:
    vals += [ 22 - temp*math.exp(-0.0373*x) ]
    xs += [x]
    x += 1

plt.plot(xs, vals, color = 'blue', linestyle = 'solid',
         label = 'T(t)')

plt.legend(loc = 'upper right')
fig.savefig('temper.png')