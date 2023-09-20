import matplotlib.pyplot as plt
x = []
y = []
with open('text3.txt', 'r') as f:
    for line in f:
        s = line.rstrip().split(sep=' ')
        x.append(float(s[0]))
        y.append(float(s[1]))
plt.plot(x, y)
plt.show()