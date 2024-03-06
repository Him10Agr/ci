import matplotlib.pyplot as plt

keys = ['a', 'b', 'c']
values = [3, 6, 1]

plt.bar(keys, values)
plt.savefig('bars.png')
plt.close()

x = list(range(10))
y = list(range(10))
plt.plot(x, y)
plt.savefig('lines.png')
plt.close()