import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
def f(x):
    if x<1:
        return -20
    else:
        return x**2


vec_f=np.vectorize(f)
y=vec_f(x)
plt.plot(x,y)
plt.show()