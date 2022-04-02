import numpy as np

x = np.random.randn(2, 10000)
y = np.sqrt(x)
z = np.nansum(np.dstack(y), 2)
w = np.sum(z)
print(w)
