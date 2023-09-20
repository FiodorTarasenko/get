import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,100)
def f(x):
    return np.sqrt (1-x**2)
def g(x):
    return -1*(np.sqrt (1-x**2))
y1=f(x)
y2=g(x)
plt.plot(x,y1, color='black')
plt.plot(x,y2, color='black')
plt.show()
