import matplotlib.pyplot as plt
import random

keys = ['a', 'b', 'c']
values = [3, 6, 1]

plt.bar(keys, values)
plt.savefig('bars.png')
plt.close()

x = list(range(10))
y = [random.randrange(10) * i for i in x]
plt.plot(x, y)
plt.savefig('lines.png')
plt.close()

