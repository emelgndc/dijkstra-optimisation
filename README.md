# dijkstra-optimisation
My solution to a fun question from an assignment. I didn't include comments (bad practice!!) but hopefully most of it makes sense.

The brief was as follows:
A frog needs to navigate its way from its current position to its next meal through a dangerous landscape. To do so, it leaps from boulder to boulder, but it can jump at most 1m. 
Your aim is to find the length of the shortest path to get the frog to its next meal using only boulders.
The landscape is a n × n square (units are cm) with boulders at exact positions given by coordinates (x, y) where 0 ≤ x, y ≤ n. 
Boulders are scattered across the landscape. Use Euclidean distance to calculate the distance between boulders.

Input format: The input is taken from the keyboard (e.g. by sys.stdin) as multiple lines of comma separated integers. Each line has 2p + 1 numbers where p ≥ 2. 
The first number on each line is the size of the landscape, n. The following 2p numbers give locations of p boulders, so the jth boulder is at (2j, 2j + 1). 
The first position listed on each line is the frog’s current position, the final position listed is the target boulder where the frog will find its next meal.

For example:
100,0,0,0,100,100,100
1000,20.892,986,602,138.97,206.2,10.44
200,25,25,10,1,50,25,140,30

Output format: For each line of input, output a single number to the console which is the length of the shortest path from the origin town to the desitination town. 
Use str.format to give this value to 2 decimal places. Precisely, format x using ’{:.2f}’.format(x). Do not use any other rounding throughout your algorithm. 
If the destination town is unreachable from the origin, output -1.

For the example input above, output would be:
200.00
-1
115.14
