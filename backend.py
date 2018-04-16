from tsp_solver.greedy import solve_tsp
from dijkstar import Graph, find_path

#-----------list for all the cost between bulidings --------
D = [
    [0,20,40,22,50,10],
    [20,0,20,50,50,15],
    [40,20,0,45,30,10],
    [22,50,45,0,15,22],
    [55,50,30,15,0,22],
    [10,15,10,22,22,0]
    ]

#--------------array with all bulidings in our town -----------
buildingsArray = ['windmill','school','university','shop','mall','fountain']

#---------- execute tsp algorithm and put the whole path in an array ---------
path = solve_tsp(D)

#----------- claculating total of costs to travel to all cites --------------
index=0
total=0
while index < len(path)-1:
    w = path[index]
    total += D[w][path[index+1]]
    index +=1

#--------------- function to put the tsp path and the total cost into string ------------
def travillingsalesMan():
    tspStr= "Go to \n"
    for i in path:
        if i < len(path)-1:
            tspStr+= str(buildingsArray[i]) + " then\n"
        else:
            tspStr+= str(buildingsArray[i]) + " \n"
    tspStr+= "total cost: " + str(total) + 'Km'
    return tspStr

print(travillingsalesMan())
#-------------- put the list in a graph for shorestpath algorithm ----------
graph = Graph()
i=0
while i < len(D):
    j=0
    while j <= len(D)-1:
        graph.add_edge(i,j,{'cost':D[i][j]})
        j+=1
    i+=1

print(graph._data)

#---------- cost function ----------
def cost_func(u, v, e, prev_e): return e['cost']
print('-----------------------')
#-------------shortest path and cost function ------------------
def shortsPath(fromBuilding,toBuilding):
    shortestPathStr= "Go to \n" 
    cost = 0.0
    #----------- fetching the index of a buliding
    fromIndex=buildingsArray.index(fromBuilding)
    toIndex= buildingsArray.index(toBuilding)
    findThePath = find_path(graph, fromIndex,toIndex, cost_func=cost_func)
    #----------- the shortest path with buildings ----------------
    for i in findThePath.nodes:
        if i < len(findThePath.nodes)-1:
            shortestPathStr+= str(buildingsArray[i]) + " then\n"
        else:
            shortestPathStr+= str(buildingsArray[i]) + "\n"
    
    #------------ calculating the cost ----------------
    for i in findThePath.costs:
        cost+= i
    
    shortestPathStr+= "cost: " + str(cost) + "Km"

    return shortestPathStr

