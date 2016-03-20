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
	result = (x**2) + (y**2)

	return result

def compare(d, best, bestCoords):
	change = True

	minNeighbor = min(d, key=d.get)

	if (d[minNeighbor][0] <= best):
		print (d[minNeighbor][0], " <= ", best)
		print ("in here")
		best = d[minNeighbor][0]
		bestCoords = d[minNeighbor][1]
		change = False

	return best, bestCoords, change


def hill_climb(func, step_size, xmin, xmax, ymin, ymax):
	x = randint(xmin, xmax)
	y = randint(ymin, ymax)

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
 		print("neighbors = ", neighbors)
 		best, bestCoords, min = compare(neighbors, best, bestCoords)
 		print ("BestCoords = ", bestCoords)


	print (best)
	print (bestCoords)



def hill_climb_random_restarts(func, step_size, num_restarts, xmin, xmax, ymin, ymax):
	min_restarts = dict()

	for i in range(num_restarts):
		min_restarts[i] = []

		x = randint(xmin, xmax)
		y = randint(ymin, ymax)

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
 			print("neighbors = ", neighbors)
 			best, bestCoords, MIN = compare(neighbors, best, bestCoords)
 			print ("BestCoords = ", bestCoords)


		
		min_restarts[i].append(best)
		min_restarts[i].append(bestCoords)

		globalMin = min(min_restarts, key=min_restarts.get)

		print("CHOICES: ", min_restarts)

		print (min_restarts[globalMin][0])
		print (min_restarts[globalMin][1])


def simulated_annealing(func, step_size, max_temp, xmin, xmax, ymin, ymax):

	x = randint(xmin, xmax)
	y = randint(ymin, ymax)
	
	solution = []
	new_solution = []

	old_cost = func(x,y)
  	
	while(max_temp > 0):
		print ("CURRENT SOLUTION: ", old_cost)
		new_solution = getNeighbor(xmin, xmax, ymin, ymax)
		new_cost = func(new_solution[0],new_solution[1])
		ap = acceptance_probability(old_cost, new_cost, max_temp)

		if (new_cost < old_cost):
			solution = new_solution
			old_cost = new_cost
		elif (ap > randint(0,1)):
			print("MAYBE???")
			solution = new_solution
			old_cost = new_cost
	
		max_temp = max_temp - 1
	print (solution)
	print(old_cost)
	return solution, old_cost


def getNeighbor(xmin, xmax, ymin, ymax):

	result = []
	x = randint(xmin, xmax)
	y = randint(ymin, ymax)	
	result.append(x)
	result.append(y)
	print("NEW NEIGHBOR: ", result)
	return result



def acceptance_probability(old_cost, new_cost, max_temp):

	print ("TEMP: ", max_temp)
	print ("OLD COST: ", old_cost)
	print ("NEW COSTL ", new_cost)
	result = exp((old_cost - new_cost)/max_temp)
	print ("ALPHA = ", result)
	return result



def main():

	print (FUNCTION(2,5))

	neighbors = dict()
	neighbors["up"] = []
	neighbors["down"] = []
	neighbors["right"] = []
	neighbors["left"] = []



	print (getNeighbors(FUNCTION, neighbors, 3, 3, 6))

	print("HILLCLIMBING____________________")

	hill_climb(FUNCTION, 3, -10, 10, -10, 10)


	print("HILLCLIMBING w restarts____________________")
	hill_climb_random_restarts(FUNCTION, 3, 3, -10, 10, -10, 10)

	print("SIMULATED ANNEALING____________________")
	simulated_annealing(FUNCTION, 3, 100, -10, 10, -10, 10)


main()