def gridChallenge(grid):
    for i in range(0,len(grid)):
        grid[i]=''.join(sorted(grid[i]))
    
    for col in range(0,len(grid[0])):
        anch=-999
        for row in range(0,len(grid)):
            if anch> ord(grid[row][col]) :
                return "NO"
            anch=ord(grid[row][col])
    
    return "YES"