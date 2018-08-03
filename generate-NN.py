# -*- coding: utf-8 -*-

# Generate a neural network in TGF (trivial graph format)
# for use with yEd graph editor

# topology of neural network
topology = [3, 5, 7, 9]

# First, print all the nodes
for i, j in enumerate(topology):
	for k in range(j):
		print(chr(i + 48) + chr(k + 48))

# separator
print("#")

# Then print all the edges
for i in range(3):								# for each layer
	for j in range(topology[i]):				# for each neuron
		for k in range(topology[i + 1]):		# for each target neuron
			print(chr(i + 48) + chr(j + 48), end=' ')
			print(chr(i + 1 + 48) + chr(k + 48))
