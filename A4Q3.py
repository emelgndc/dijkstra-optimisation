import sys
import math

#data = open('a4q3in2.txt','r')
#lines = [line.rstrip() for line in data]
lines = sys.stdin.readlines()

def dijk(g, order, sl):
    s = 0
    inf = math.inf
    colour = []
    dist = []
    
    dist.append(0)
    colour.append('black')
    
    for u in range(1, order):
        dist.append(inf)
        colour.append('white')
    
    for a in sl:
        dist[a] = g[s][a][1]
    
    while 'white' in colour:
        distlist = []
        mini = 0
        for i in range(len(colour)):
            if colour[i] == 'white':
                distlist.append(dist[i])
                
        if distlist == []:
            break
        else:
            mini = min(distlist)

        if mini == inf:
            break
        else:
            minival = dist.index(mini)
            colour[minival] = 'black'
            for x in range(order):
                if colour[x] == 'white':
                    dist[x] = min(dist[x], dist[minival] + g[minival][x][1])
    
    if dist[len(dist)-1] == inf:
        return -1
    return "{:.2f}".format(dist[len(dist)-1])
    
    
def adj(order, list1):
    inf = math.inf
    newlist = list1
    newlist.pop(0)
    coords = []
    adjlist = []
    sl = []
    
    for i in range(0, len(newlist), 2):
        x = float(list1[i])
        y = float(list1[i+1])
        adjlist.append([])
        coords.append((x,y))
    
    for j in range(len(coords)):
        for k in range(len(coords)):
            if j == k:
                adjlist[j].append([k, inf])
                continue
            else:
                dist = math.sqrt((coords[j][0]-coords[k][0])**2 + (coords[j][1]-coords[k][1])**2)
                if dist <= 100:
                    adjlist[j].append([k, dist])
                    if j == 0:
                        sl.append(k)
                else:
                    adjlist[j].append([k, inf])
                    
    print(dijk(adjlist, order, sl))
    
def processor(list1, ind):
    lines[ind].rstrip()
    full = []
    for i in range(0, len(list1)):
        temp = list1[i].split(",")
        full.append(temp)
    return full
        

def start(list1):
    ind = 0 
    for i in range(len(list1)):
        order = int((len(list1[i])-1)/2)
        adj(order, list1[i])
        

processed = processor(lines, 0)
start(processed)