## coconut_delivery

This code is based on this problem: https://github.com/AdamFinch1/coconut_delivery

## HashMap Implementation
The file hashmap_endgame.py utilizes a hashmap to compute the shortest path from the lowest mile to the highest mile based on the energy constraints of the problem.  This was my initial approach to this problem as I initially thought generating a graph or tree would be too difficult for this.  The algorithm that determines the shortest path is based on making comparisons of the end mile of the current location and the start mile of the next location. 

The program stores our data as such: tree[int(v1)] = [int(v2), int(e)] where v1 is the start mile, v2 is the end mile, and e is the energy to complete the trip.  I chose this format for storing the data because I need to sort my keys by the start mile.  Since I have no way of know ahead of time what the start mile would be, I would need a method of doing so.

Given this set of mile gaps [(0,5), (1,3), (2,4), (8,11), (14,18]), the alogrithm will skip miles 1-4 because it already completes them in the first set.  

## Graph Implementation
I realized that one potential problem was that you could potentially skip some mile segments for a more optimzied route.  A graph solution seemed the most logical based on the data.  Each data subset had a start and end mile (which would represent an edge in the graph) and the energy to fly that mile (a vertex in the graph). However, because of the problem constraints this was not fesible.  So I decided to make a complete directed graph using each jet stream as a vertex in the graph and using the energy to go between two sets of miles as the edge weight.  I determined each edge of a vertex in a similar way to my hash map implementation.  An edge E of a vertex V must have its start value be large than the end value of the V.  

This worked well for the sample data, however, when it came to use the flight path data, it created a graph of over 5000 vertices which made roughly 12497500 edges.
