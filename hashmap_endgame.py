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
			
def findBestRoute2(dict, constantEnergy):
	totalEnergy = 0
	routeList = []
	hashMap = {}
	first = True
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
tree = {}
firstLine = True
for line in reader:
	if firstLine:
		constantEnergy = int(''.join(line))
		firstLine = False
	else:
		v1, v2, e = line
		tree[int(v1)] = [int(v2), int(e)]

sortedKeys = merge_sort(tree.keys())

dict = collections.OrderedDict()
for keys in sortedKeys:
	dict[keys] = tree[keys]
print findBestRoute(dict, constantEnergy)
	
