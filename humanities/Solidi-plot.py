# Elon Musk net worth as of March 2025 = 330 billion = 330e9
# Elon Musk peak wealth = 500 billion

import numpy as np
import matplotlib.pyplot as plt

def D(w):
	return 1000 * np.log(w)

w = np.arange(0, 400e9, 4e9)
plt.xscale('log')
plt.plot(w, 100* np.log(w), 'r--')
plt.plot(w, 10* np.log(w), 'g^')
plt.plot([363e9, 100e3], [D(363e9), D(100e3)], 'ro')
plt.show()
