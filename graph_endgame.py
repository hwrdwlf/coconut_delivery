#!/usr/bin/python
import sys, getopt
import csv
import collections
import random

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

class Node:
    def __init__(self, id = None, start=None, end=None, value = None, next = None, edges = None):
		self.value = value
		self.start = start
		self.end = end
		self.next = next
		self.edges = edges
		self.id = id

    def __str__(self):
        return 'Node ['+str(self.id)+']'

class LinkedList:
    def __init__(self):
		self.first = None
		self.last = None
			
    def insert(self, id, start, end, value):
		current = self.first
		
		if current == None:
			node = Node(id, start, end, value, None, None)
			self.first = node   
			self.last = self.first
			return
        
		if current.start > start:
			newNode = Node(id, start, end, value, None, None)
			newNode.next = current
			self.first = newNode
			return
			
		while current.next != None:
			if current.next.start > start:
				break
			current = current.next
		
		newNode = Node(id, start, end, value, None, None)
		newNode.next = current.next
		current.next = newNode
		if current.next is None:
			self.last = newNode

		return

    def getCurrentNode(self, id):
        node = self.first
        while node:
            if node.id == id:
                return node
            node = node.next
        return 0
					

    def in_list(self, value):
    	if self.first == None:
    		return False
    	node = self.first
    	while node:
    		if node.value == value:
    			return True
    		node = node.next
    	return False

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' + 'Current Node: ' + '(' + str(current.start) + ',' + str(current.end) + ')' + ' value->' + str(current.value) + ' edges: ' + self.printEdges(current.edges) + '\n'
            while current.next != None:
                current = current.next
                out += 'Current Node: ' + '(' + str(current.start) + ',' + str(current.end) + ')' + ' value->'  + str(current.value) + ' edges: ' + self.printEdges(current.edges) +'\n'
            return out + ']'
        return 'LinkedList []'

    def printEdges(self, edges):
    	if edges != None:
	    	if edges.first != None:
	    		current = edges.first
		    	out = '[(' + str(current.start) + ',' + str(current.end) + ') distance: ' + current.value
		    	while current.next != None:
		    		current = current.next
		    		out += ', (' + str(current.start) + ',' + str(current.end) + ') distance: ' + current.value
		    	return out + ']'
    	return 'None'

    def updateEdges(self, value, linkedlist):
    	current = self.first
    	if current.value == value:
    		current.edges = linkedlist
    	while current.next != None:
    		current = current.next
    		if current.value == value:
    			current.edges = linkedlist
	


    def clear(self):
        self.__init__()


# Implementation of Dijsksta's algorithm
def shortestPath(graph, energy):
	# case for a single node
	if graph.first.next == None:
		# if our graph only has a single there are no shortest paths
		# TODO: return something more meaningful here
		return None

	# best estimated distances	
	dist = {}
	# an array of predecessors
	prevNodes = {}
	# set of vertices whose shortest paths have been determined
	VS = []
	# set of vertices we have not visited yet
	UVS = []
		
	# Now that we know we have a graph with at least 2 vertices and 1 edge
	# set the cost of the first node to zero and the first to some arbitrary value
	sourceNode = graph.first
	sourceNodeId = graph.first.id
	
	# since this is a graph and not necessarily a linked list we need to find the last
	# node in our destination
	sourceEdges = sourceNode.edges.first
	previousEndMile = 0
	while sourceEdges:
		if int(sourceEdges.end) > int(previousEndMile):
			previousEndMile = sourceEdges.end
			goalNode = sourceEdges
		sourceEdges = sourceEdges.next


	print "head: " , sourceNode
	print "goal: " , goalNode
	
	# distance from root to root
	# Normally we would assign the first value of our distance array as 0 for the source
	# but within the scope of this assignemnt we need to assign it the first energy cost
	# to travel between the two miles
	dist[sourceNode.id] = sourceNode.value
	prevNodes[sourceNode.id] = 0
	
	# now we need to initialize our vertices we have no been to yet
	while sourceNode:
		# since we have already been to the root node do not include it
		if sourceNode.id != sourceNodeId:
			dist[sourceNode.id] = 1000000000000000000
			prevNodes[sourceNode.id] = None
		# add each node to the set
		UVS.append(sourceNode.id)
		sourceNode = sourceNode.next

	# while we still have nodes we have no visited
	while UVS:
		# find the node with the smallest cost in our unvisited set
		minDist = min(dist.items(), key=lambda x: x[1]) 
		minDistKey = minDist[0]
		minDistValue = minDist[1]
		
		# remove that node from our set
		for value in UVS:
			if value == minDistValue and minDistKey in VS:
				VS.remove(minDistKey)


		currentNodeId = minDistKey
		print "current node: ", currentNodeId, " min dist: ", minDistValue

		# because of the nature of this program we have to do some slightly unortodox things
		# after we have removed it from our unvisited list
		# add it to our visited list
		VS.append(currentNodeId)

		# check to see if we are at our destination
		if currentNodeId == goalNode.id:
			break

		# get the current node that we just removed from our set
		# pull out all the adjacent nodes
		# and start comparing distances
		currentNode = graph.getCurrentNode(currentNodeId)
		endMile = currentNode.end
		adjNodes = currentNode.edges.first
		while adjNodes:
			altPath = minDistValue + energy * (int(adjNodes.start) - int(endMile)) + int(adjNodes.value)
			if altPath < dist[adjNodes.id]:
				dist[adjNodes.id] = altPath
				prevNodes[adjNodes.id] = currentNodeId
			adjNodes = adjNodes.next	

		# make sure we only try to remove things that exist
		if minDistKey in dist:
			dist.pop(minDistKey,None)

	return (VS,minDistValue)
		

def getFileNameFromOpts():
	fileName = ''
	try: 
		opts,args = getopt.getopt(sys.argv[1:], "hi:", ["inputFile="])
	except getopt.GetoptError:
		print 'usage test.py -i/--inputFile <inputFile>'
		sys.exit(2)
	for opt,arg in opts:
		if opt == '-h':
			print 'usage: test.py -i/--inputFile <inputfile>'
			sys.exit()
		elif opt in ("-i", "--inputFile"):
			fileName = arg	
	if not fileName:
		print 'missing args. usage: test.py -i/--inputFile <inputfile>'
		sys.exit()
	return fileName
	
file = open(getFileNameFromOpts(), 'r')
reader = csv.reader(file, delimiter=' ')

graph = LinkedList()
tempGraph = LinkedList()
hashMap = {}
for row in reader:
	# this means this is the first row store the energy value
	if 1 >= len(row):	
		# convert the single row list into a integer
		energy = int(''.join(row))
	else:
		v1,v2,e = row
		# to make it easier to process we need to map the vertices to a hash
		hash =  random.randint(1,1000)
		if hash in hashMap:
			# to prevent collisions make sure they is not already in the dictionary
			while hash in hashMap:
				hash =  random.randint(1,100000000000)
				#print hash
		hashMap[hash] = (v1,v2)
		
		# add nodes to linked list to start building graph
		graph.insert(hash, int(v1),int(v2),int(e))
		tempGraph.insert(hash, v1,v2,e)

print hashMap

# go through the linked list and for each node add all the edges
g = graph.first
tempList = tempGraph.first
while g:
	ll = LinkedList()
	tempList = tempGraph.first
	while tempList:
		if int(tempList.start) >= int(g.end):
			# to keep consistent keys
			for key,value in hashMap.items():
				if value == (tempList.start,tempList.end):
					ll.insert(key, tempList.start, tempList.end, tempList.value)
		tempList = tempList.next
	graph.updateEdges(g.value, ll)
	g = g.next

print shortestPath(graph,energy)













