
# Taking positions of Ladders and Snakes as inputs. The player just has to enter 1 or 2 digit integers a/c to the question.
lad1t=int(input("Which cell should have the 1st ladder base:"))
lad1h=int(input("Which cell should have the 1st ladder top:"))
lad2t=int(input("Which cell should have the 2nd ladder base:"))
lad2h=int(input("Which cell should have the 2nd ladder top:"))
lad3t=int(input("Which cell should have the 3rd ladder base:"))
lad3h=int(input("Which cell should have the 3rd ladder top:"))
sn1h=int(input("Which cell should have the 1st snake top:"))
sn1t=int(input("Which cell should have the 1st snake base:"))
sn2h=int(input("Which cell should have the 2nd snake top:"))
sn2t=int(input("Which cell should have the 2nd snake base:"))
sn3h=int(input("Which cell should have the 3rd snake top:"))
sn3t=int(input("Which cell should have the 3rd snake base:"))


lst=[0,lad1t,lad1h,lad2t,lad2h,lad3t,lad3h,99]

def is_empty(lst):



    if len(lst) != 0:
        return False
    else:
        return True


def Dequeue(queue):
    x = queue.pop(0) 
    return x

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []

    return G

G = {}
x = addNodes(G, lst)

# Creating a list to extract edges of the graph from for shortest path calculation
lst1=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if i == 1 and j == 2:
            tup=(lst[i],lst[j],0)
            lst1.append(tup)
        if i == 3 and j == 4:
            tup=(lst[i],lst[j],0)
            lst1.append(tup)
        if i == 5 and j == 6:
            tup=(lst[i],lst[j],0)
            lst1.append(tup)
        else:
            tup=(lst[i],lst[j],(((abs(lst[j]-lst[i]))//6)+1))
            print(lst[j])
            print(lst[i])
            lst1.append(tup)





def addEdges(G, edges):

        for i in G:
            for j in range(len(edges)):
                if edges[j][0] == i:
                    
                    lst = []
                    lst.append(edges[j][1])
                    lst.append(edges[j][2])
                    tup = tuple(lst)
                    G[i].append(tup)
        return G

# Path for Dijkstra
def path(G,lst,a,b):
    for i in G:
        if i[1] == b:
            x = i
    if x[0] == a:
        tup=(x[0],x[1])
        lst.append(tup)
    else:
        tup=(x[0],x[1])
        lst.append(tup)
        y=x[0]
        path(G,lst,a,y)

# Dijkstra
def getshortestpath(G,From,To):
    listofnodes=list(G.keys())
    infinity=9999
    shortestdistance=[]
    for i in listofnodes:
        if i == listofnodes[0]:
            tup=(i, i, 0)
            shortestdistance.append(tup)
        else:
            tup=("", i, infinity)
            shortestdistance.append(tup)
    unvisited=listofnodes.copy()
    visited=[]        
    while is_empty(unvisited) == False:
        lowest_distance=infinity
        current_vertex=""
        for i in shortestdistance:
            if i[2] <= lowest_distance and i[1] not in visited:
                    lowest_distance = i[2] 
                    current_vertex = i[1]
        for i in G[current_vertex]:
            Neighbor=i[0]
            Neighborsweightingraph=i[1]
            Neighborsweightinshortestdistance=0   
            for k in shortestdistance:
                if current_vertex == k[1] and current_vertex not in visited:
                    currentvertexweightinshortestdistance = k[2]  
            for j in range(len(shortestdistance)):
                if Neighbor not in visited:
                    if Neighbor in shortestdistance[j]:
                        Neighborsweightinshortestdistance = shortestdistance[j][2]   
                        if Neighborsweightinshortestdistance>(currentvertexweightinshortestdistance+Neighborsweightingraph):
                            tup1=(current_vertex,Neighbor,Neighborsweightingraph+currentvertexweightinshortestdistance)
                            shortestdistance[j] = tup1
                        
        if current_vertex in unvisited:
            unvisited.remove(current_vertex)
        if current_vertex not in visited:
            visited.append(current_vertex)

    lst=[]
    path(shortestdistance,lst,From,To)
    lst1=[]
    for i in range(len(lst)-1,-1,-1):
        lst1.append(lst[i])
    return lst1

# Functions to assist the placement of snakes, ladders and pieces on the board. To be called in the display function.
def ladderlsts1(lad1t,lad1h):
    lst=[]
    lst.append(lad1t)
    lst.append(lad1h)
    return lst

def ladderlsts2(lad2t,lad2h):
    lst=[]
    lst.append(lad2t)
    lst.append(lad2h)
    return lst

def ladderlsts3(lad3t,lad3h):
    lst=[]
    lst.append(lad3t)
    lst.append(lad3h)
    return lst
    
def snklsts1(sn1t,sn1h):
    lst=[]
    lst.append(sn1t)
    lst.append(sn1h)
    return lst

def snklsts2(sn2t,sn2h):
    lst=[]
    lst.append(sn2t)
    lst.append(sn2h)
    return lst

def snklsts3(sn3t,sn3h):
    lst=[]
    lst.append(sn3t)
    lst.append(sn3h)
    return lst

 
 
def enqueue(lst,item):
    lst.append(item)
 
# BFS function to find out the minimum number of movies required to win the game.
def Mindierolls(lad1t,lad1h,lad2t,lad2h,lad3t,lad3h,sn1t,sn1h,sn2t,sn2h,sn3t,sn3h):

    Noofcells = 100
    cells = []
    visitedcells = []
    
    for i in range(Noofcells):
        cells.append(-1)
        visitedcells.append(False)

    cells[lad1t] = lad1h
    cells[lad2t] = lad2h
    cells[lad3t] = lad3h
    
    if sn1h == 99: 
        cells[93] = sn1t
    else:
        cells[sn1h] = sn1t
    if sn2h == 99:
        cells[93] = sn2t
    else:
        cells[sn2h] = sn1t
    if sn3h == 99:
        cells[93] = sn3t
    else:
        cells[sn3h] = sn1t

    BFSqueue = []

    visitedcells[0] = True
 
    tup=(0,0)
    enqueue(BFSqueue,tup)

    Search = True
    while Search:
        x = BFSqueue.pop(0)
        c=x[0]
        cd = x[1]

        visitedcells[c] = True  

        if c == Noofcells - 1:
            Search = False
 
        next = c + 1

        while next <= c + 6 and next < Noofcells:
            if visitedcells[next] is False:
                visitedcells[next] = True
                if cells[next] != -1:
                    a = cells[next]
                else:
                    a = next

                z = cd + 1
                tup1=(a,z)
                BFSqueue.append(tup1)
            next += 1
    return x[1]

G = addEdges(x,lst1)
x = getshortestpath(G,0,99)
print(x)
# Creating a list with all the names of all the cells visited in the shortest path. This list will be used to create snakes, ladders and pieces at those cells.
lst3 = []
for i in x:
    for j in i:
        if j != 0 and 'cell'+ str(j) not in lst3:
            if j != 99:
                n= 'cell' + str(j)
                lst3.append(n)
            else:
                n= 'cell' + str(100)
                lst3.append(n)


rolls  = Mindierolls(lad1t,lad1h,lad2t,lad2h,lad3t,lad3h,sn1t,sn1h,sn2t,sn2h,sn3t,sn3h) 
print("Minimum die rolls needed to win the game are", rolls)     

# A dictionary containing x and x coordinates of all the cells on the board.
dic1={"cell1":(22,610),"cell2":(88,610),"cell3":(154,610),"cell4":(220,610),"cell5":(286,610),"cell6":(352,610),"cell7":(418,610),"cell8":(484,610),"cell9":(550,610),"cell10":(616,610),"cell20":(22,544),"cell19":(88,544),"cell18":(154,544),"cell17":(220,544),"cell16":(286,544),"cell15":(352,544),"cell14":(418,544),"cell13":(484,544),"cell12":(550,544),"cell11":(616,544),"cell21":(22,478),"cell22":(88,478),"cell23":(154,478),"cell24":(220,478),"cell25":(286,478),"cell26":(352,478),"cell27":(418,478),"cell28":(484,478),"cell29":(550,478),"cell30":(616,478),"cell40":(22,412),"cell39":(88,412),"cell38":(154,412),"cell37":(220,412),"cell36":(286,412),"cell35":(352,412),"cell34":(418,412),"cell33":(484,412),"cell32":(550,412),"cell31":(616,412),"cell41":(22,346),"cell42":(88,346),"cell43":(154,346),"cell44":(220,346),"cell45":(286,346),"cell46":(352,346),"cell47":(418,346),"cell48":(484,346),"cell49":(550,346),"cell50":(616,346),"cell60":(22,280),"cell59":(88,280),"cell58":(154,280),"cell57":(220,280),"cell56":(286,280),"cell55":(352,280),"cell54":(418,280),"cell53":(484,280),"cell52":(550,280),"cell51":(616,280),"cell61":(22,214),"cell62":(88,214),"cell63":(154,214),"cell64":(220,214),"cell65":(286,214),"cell66":(352,214),"cell67":(418,214),"cell68":(484,214),"cell69":(550,214),"cell70":(616,214),"cell80":(22,148),"cell79":(88,148),"cell78":(154,148),"cell77":(220,148),"cell76":(286,148),"cell75":(352,148),"cell74":(418,148),"cell73":(484,148),"cell72":(550,148),"cell71":(616,148),"cell81":(22,82),"cell82":(88,82),"cell83":(154,82),"cell84":(220,82),"cell85":(286,82),"cell86":(352,82),"cell87":(418,82),"cell88":(484,82),"cell89":(550,82),"cell90":(616,16),"cell100":(22,16),"cell99":(88,16),"cell98":(154,16),"cell97":(220,16),"cell96":(286,16),"cell95":(352,16),"cell94":(418,16),"cell93":(484,16),"cell92":(550,16),"cell91":(550,16)}

# The following functions take the bases and tops of ladders and snakes and give out to the position of those cells as a string "celli".
firstlad = ladderlsts1(lad1t,lad1h)
stpfl="cell"+str(firstlad[0])
endpfl="cell"+str(firstlad[1])
if stpfl in dic1 and endpfl in dic1:
    stp1=dic1[stpfl]
    endp1=dic1[endpfl]

secondlad = ladderlsts2(lad2t,lad2h)
stpsl="cell"+str(secondlad[0])
endpsl="cell"+str(secondlad[1])
if stpsl in dic1 and endpsl in dic1:
    stp2=dic1[stpsl]
    endp2=dic1[endpsl]

thirdlad = ladderlsts3(lad3t,lad3h)
stptl="cell"+str(thirdlad[0])
endptl="cell"+str(thirdlad[1])
if stptl in dic1 and endptl in dic1:
    stp3=dic1[stptl]
    endp3=dic1[endptl]

firstsnk = snklsts1(sn1t,sn1h)
stpfs="cell"+str(firstsnk[0])
endpfs="cell"+str(firstsnk[1])
if stpfs in dic1 and endpfs in dic1:
    stp4=dic1[stpfs]
    endp4=dic1[endpfs]

secsnk = snklsts2(sn2t,sn2h)
stpss="cell"+str(secsnk[0])
endpss="cell"+str(secsnk[1])
if stpss in dic1 and endpss in dic1:
    stp5=dic1[stpss]
    endp5=dic1[endpss]

thirdsnk = snklsts3(sn3t,sn3h)
stpts="cell"+str(thirdsnk[0])
endpts="cell"+str(thirdsnk[1])
if stpts in dic1 and endpts in dic1:
    stp6=dic1[stpts]
    endp6=dic1[endpts]


# Front end function
def display():

    import pygame
    pygame.init()
    pygame.display.set_caption("Snake & Ladder Game")
    screen_size=pygame.display.set_mode((660,660))
    playerimg = pygame.image.load('board.png')
    playerimg1 = pygame.image.load('smallgreenlad1.jpg')
    playerimg2 = pygame.image.load('smallbluelad1.jpg')
    playerimg3 = pygame.image.load('smallredlad1.jpg')
    playerimg4 = pygame.image.load('smallgreensnake.jpg')
    playerimg5 = pygame.image.load('smallbluesnake.jpg')
    playerimg6 = pygame.image.load('smallredsnake.jpg')
    playerimg7 = pygame.image.load('bluepiece.jpg')

    plx= 0
    ply = 0
    # Function for displaying the board.
    def player():
        screen_size.blit(playerimg,(plx,ply))
    # Functions for displaying the snakes, ladders and pieces.   
    def lad1():
        screen_size.blit(playerimg1,stp1)
        screen_size.blit(playerimg1,endp1)

    def lad2():
        screen_size.blit(playerimg2,stp2)
        screen_size.blit(playerimg2,endp2)
    
    def lad3():
        screen_size.blit(playerimg3,stp3)
        screen_size.blit(playerimg3,endp3)

    def snk1():
        screen_size.blit(playerimg4,stp4)
        screen_size.blit(playerimg4,endp4)

    def snk2():
        screen_size.blit(playerimg5,stp5)
        screen_size.blit(playerimg5,endp5)

    def snk3():
        screen_size.blit(playerimg6,stp6)
        screen_size.blit(playerimg6,endp6)

    def piece():
        for i in lst3:
            o = dic1[i]
            y = o[1] + 25
            h = (o[0],y)
            screen_size.blit(playerimg7,h)

    screen = True

    c = (0,150,255)

    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen = False
        player()
        lad1()
        lad2()
        lad3()
        snk1()
        snk2()
        snk3()
        piece()
        pygame.display.update()

display()