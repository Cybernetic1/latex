# Elon Musk net worth as of March 2025 = 330 billion = 3.3e11
# Elon Musk peak wealth = 500 billion = 5e11
# World internet population in 2023 = 5.3 billion = 5.3e9
# Question: What's the deal with Elon Musk?
#	We want him to buy.  But shall we give him a 'fair' deal?
#	We assume 1 coin = 1 like.
#	We try to guess how much work is needed to get so many likes
#	and that his life's work so far is equivalent to so many likes
#	If we esteem Musk too high, then tyranny of traditional money persists
#	If we judge Musk too low, then current rich people won't buy
# more data:
#	* most upvoted YouTube comment: 4.1M likes
#	* most upvoted Reddit post: 486K like
#	* most viewed YouTube video: 15.2B views

import numpy as np
import matplotlib.pyplot as plt

def D1(w):
	return np.log(w)

def D1000(w):
	return 1000 * np.log(w)

w0 = []
for x in range(-1,12):
	w0.append(10**x)
w = np.array(w0)
plt.xscale('log')
plt.plot(w, 1000* np.log(w), 'r--')
plt.plot(w, 100* np.log(w), 'g--')
plt.plot(w, 1* np.log(w), 'b--')

plt.text(1e8, 19500, r'k = 1000', color='red', rotation=38)
plt.text(1e8, 2500, r'k = 100', color='green')
plt.text(1e8, 300, r'k = 1', color='blue')

plt.plot([330e9, 100e3], [D1000(330e9), D1000(100e3)], 'ro')
plt.text(330e9/10, 24000, r'Elon Musk')
plt.text(100e3/2, 9000, r'me')

plt.xlabel("Money (in log scale)")
plt.ylabel("Solidi coins")

plt.savefig("Solidi-plot.png", format='png', bbox_inches='tight')
# plt.show()

# To calculate position of Elon on the graph if it was linear:
# 7.5cm = 1e5 = me
# X cm = 3.3e11 = Musk
# X = 7.5 * 3.3e11 / 1e5 = 7.5 * 3.3e6 = 247,500,000cm = 247.5 km
