import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import random


from random import randint
from math import exp

def getNeighbors(func, d, step_size, x, y):

	dic = dict()
	dic["up"] = []
	dic["down"] = []
	dic["right"] = []
	dic["left"] = []


	dic["up"].append(func(x,y+step_size))
	dic["down"].append(func(x,y-step_size))
	dic["right"].append(func(x+step_size,y))
	dic["left"].append(func(x-step_size,y))

	dic["up"].append([x,y+step_size])
	dic["down"].append([x,y-step_size])
	dic["right"].append([x+step_size,y])
	dic["left"].append([x-step_size,y])



	return dic




def FUNCTION(x,y):
	r = math.sqrt((x**2) + (y**2))
	result = ((math.sin(x**2 + 3*x**2))/(.01+r**2)) + (x**2 + 5*y**2) * ((exp(1-r**2))/2)
	return result

def compare(d, best, bestCoords):
	change = True

	minNeighbor = min(d, key=d.get)

	if (d[minNeighbor][0] <= best):
		best = d[minNeighbor][0]
		bestCoords = d[minNeighbor][1]
		change = False

	return best, bestCoords, change


def hill_climb(func, step_size, xmin, xmax, ymin, ymax):
	min_restarts = dict()
	square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	xx = yy = np.arange(-3.0, 3.0, 0.05)
	X, Y = np.meshgrid(xx, yy)
	zs = np.array([fun(xx,yy) for xx,yy in zip(np.ravel(X), np.ravel(Y))])
	Z = zs.reshape(X.shape)

	x = random.uniform(xmin, xmax)
	y = random.uniform(ymin, ymax)

	bestCoords = [x,y]
	best = func(x,y)

	neighbors = dict()
	neighbors["up"] = []
	neighbors["down"] = []
	neighbors["right"] = []
	neighbors["left"] = []

	min = False

	while (min == False):
 		neighbors = getNeighbors(func, neighbors, step_size, bestCoords[0], bestCoords[1])
 		best, bestCoords, min = compare(neighbors, best, bestCoords)
 		xs = bestCoords[0]
 		ys = bestCoords[1]
 		zs = best
 		ax.scatter(xs, ys, zs, c="r", marker=">")
 		ax.plot_surface(X, Y, Z)


	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.title('Hill-Climbing')

	plt.show()




def hill_climb_random_restarts(func, step_size, num_restarts, xmin, xmax, ymin, ymax):
	min_restarts = dict()
	square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	xx = yy = np.arange(-3.0, 3.0, 0.05)
	X, Y = np.meshgrid(xx, yy)
	zs = np.array([fun(xx,yy) for xx,yy in zip(np.ravel(X), np.ravel(Y))])
	Z = zs.reshape(X.shape)


	for i in range(num_restarts):
		min_restarts[i] = []

		x = random.uniform(xmin, xmax)
		y = random.uniform(ymin, ymax)

		bestCoords = [x,y]
		best = func(x,y)

		neighbors = dict()
		neighbors["up"] = []
		neighbors["down"] = []
		neighbors["right"] = []
		neighbors["left"] = []

		MIN = False

		while (MIN == False):
 			neighbors = getNeighbors(func, neighbors, step_size, bestCoords[0], bestCoords[1])
 			best, bestCoords, MIN = compare(neighbors, best, bestCoords)
 			xs = bestCoords[0]
 			ys = bestCoords[1]
 			zs = best
 			ax.scatter(xs, ys, zs, c="r", marker=">")
 			ax.plot_surface(X, Y, Z)


		
		min_restarts[i].append(best)
		min_restarts[i].append(bestCoords)

		globalMin = min(min_restarts, key=min_restarts.get)

		ax.set_xlabel('X Label')
		ax.set_ylabel('Y Label')
		ax.set_zlabel('Z Label')
		plt.title('Hill-Climbing with Random Restarts')

		plt.show()


def simulated_annealing(func, step_size, max_temp, xmin, xmax, ymin, ymax):
	min_restarts = dict()
	square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	xx = yy = np.arange(-3.0, 3.0, 0.05)
	X, Y = np.meshgrid(xx, yy)
	zs = np.array([fun(xx,yy) for xx,yy in zip(np.ravel(X), np.ravel(Y))])
	Z = zs.reshape(X.shape)




	x = random.uniform(xmin, xmax)
	y = random.uniform(ymin, ymax)
	
	new_solution = []
	solution = []



	old_cost = func(x,y)
  	
	while(max_temp > 0):
		new_solution = getNeighbor(xmin, xmax, ymin, ymax)
		new_cost = func(new_solution[0],new_solution[1])
		ap = acceptance_probability(old_cost, new_cost, max_temp)

		xs = new_solution[0]
		ys = new_solution[1]
		zs = new_cost
		ax.scatter(xs, ys, zs, c="r", marker=">")
		ax.plot_surface(X, Y, Z)


		if (new_cost < old_cost):
			solution = new_solution
			old_cost = new_cost
		elif (ap > randint(0,1)):
			solution = new_solution
			old_cost = new_cost
	
		max_temp = max_temp - 1


	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.title('Simulated Annealing')

	plt.show()


	return solution, old_cost


def getNeighbor(xmin, xmax, ymin, ymax):

	result = []
	x = random.uniform(xmin, xmax)
	y = random.uniform(ymin, ymax)	
	result.append(x)
	result.append(y)
	return result



def acceptance_probability(old_cost, new_cost, max_temp):

	result = exp((old_cost - new_cost)/max_temp)
	return result


#---------------------------------------






def fun(x, y):
	r = math.sqrt((x**2) + (y**2))
	result = ((math.sin(x**2 + 3*x**2))/(.01+r**2)) + (x**2 + 5*y**2) * ((exp(1-r**2))/2)
	return result




def plot_points():
	square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	x = y = np.arange(-3.0, 3.0, 0.05)
	X, Y = np.meshgrid(x, y)
	zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
	Z = zs.reshape(X.shape)

	xs = 3
	ys = 4
	zs = 5
	ax.scatter(xs, ys, zs, color="r")

	ax.plot_surface(X, Y, Z)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	plt.show()




def main():
	hill_climb(FUNCTION, 1, -2.5, 2.5, -2.5, 2.5)
	hill_climb_random_restarts(FUNCTION, 1, 5, -2.5, 2.5, -2.5, 2.5)
	simulated_annealing(FUNCTION, 1, 100, -2.5, 2.5, -2.5, 2.5)



main()
