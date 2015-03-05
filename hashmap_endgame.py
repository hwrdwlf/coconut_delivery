#!/usr/bin/python
import collections
import csv
import operator
from heapq import merge
import sys, getopt

		
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def findBestRoute(dict, constantEnergy):
	totalEnergy = 0
	routeList = []
	hashMap = {}
	first = True
	# start at the first key (first mile) and go through each one that fits the constraint
	# if the next start mile is less than the previous end mile we cant go to that mile gap 
	# so skip that key
	for key in dict:
		start = int(key)	
		if first:
			routeList.append((key,dict[key][0]))
			end = int(dict[key][0])
			energy = int(dict[key][1])
			first = False
			totalEnergy = energy
			continue
		if start > end:
			energy = dict[key][1]
			#print "Total:" , totalEnergy, " difference: " , start-end, " key:", start, " end:" , end
			extraEnergy = int(constantEnergy * (start-end))
			#print "extra: ", extraEnergy, " energy: ", energy
			totalEnergy = int(totalEnergy + extraEnergy + energy)
			#print "after total: ", totalEnergy
			routeList.append((key,dict[key][0]))
			end = dict[key][0]
			
		
	
	hashMap[totalEnergy] = routeList
	return hashMap 
				
		
	
	hashMap[totalEnergy] = routeList
	return hashMap 
	
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
	
# read each line into object	
file = open(getFileNameFromOpts(), 'r')
reader = csv.reader(file, delimiter=' ')
tree = {}
firstLine = True
for line in reader:
	# since the first line is always the energy jump, capture it first
	if firstLine:
		constantEnergy = int(''.join(line))
		firstLine = False
	else:
		v1, v2, e = line
		tree[int(v1)] = [int(v2), int(e)]

# since we have no way of knowing ahead of time what the start mile is, we need to sort the keys to determine
# at starting and ending point
sortedKeys = merge_sort(tree.keys())

dict = collections.OrderedDict()
# once we have the keys sorted created a new ordered dictionary to perserve insertion order
for keys in sortedKeys:
	dict[keys] = tree[keys]
print findBestRoute(dict, constantEnergy)
	
