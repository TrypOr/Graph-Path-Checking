def main():
    V = 6 # Intialise the vertices
    #Initialise the edges
    E = [[0, 2], [0, 1],[1, 2],
        [2, 3],[2, 0],[4,5]] 
    G=(V,E) #Create the graph 

    #Call the function to creathe the path array
    path = create_path_matrix(G)

    #Enter the 2 vertices you want to see if there is a path
    #like path[u][v]
    if path[0][3]:
        print("Path between u and v found")
    else:
        print("No path between u and v")
        
def create_path_matrix(G):
    #Intiliase the 2D array for the algorithm
    path = [[False for i in range(G[0])] for j in range(G[0])] 

    # Set path=True for vertices according to edges
    for edge in G[1]:
        path[edge[0]][edge[1]] = True

    # Check for all intermediate vertices
    for k in range(G[0]):
        for i in range(G[0]):
            for j in range(G[0]):
                path[i][j] = path[i][j] or (path[i][k] and path[k][j])

    return path

if __name__ == "__main__":
    main()
