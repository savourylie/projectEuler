import random

def countPaths(gridSize):
    """ (int) -> int

    Return the number of unique paths of a gridSize * gridSize lattice.

    >>> countPaths(2)
    6
    
    """
    
    # 1. Create a array of paths
    paths = []
    
    # 2. Randomly create paths with given restrictions
    i = 0

    while ((i < len(paths) * len(paths)) | (len(paths) < 6)):
        # print [i, len(paths)]
        
        path = []

        x = 0
        y = 0

        while (x + y <= 2 * gridSize):
            path.append((x, y))

            if ((random.randint(0, 1) == 0) & (x < gridSize)):
                x = x + 1
            elif (y < gridSize):
                y = y + 1
            else:
                x = x + 1
            
    # 3. Add path to the array if it's not already in it
        if (path not in paths):
            paths.append(path)    
           
        i = i + 1

    # 4. Terminate the path finding when tried iterations 10 times more than the length of the array.
    print "Awesome!"
    print len(paths)
    return len(paths)
