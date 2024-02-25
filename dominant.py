"""
There is a given list of lists of integers that represent a 2-dimensional grid with n rows and m  columns. 
A cell is called a dominant cell if it has a strictly greater value than all of its neighbors. Find the number of dominant cells in the grid.
"""


def is_greater(grid, i ,j):
    for k in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            if i == k and j == m:
                continue
            if grid[i][j] <= grid[k][m]:
                return False
    return True

def numCells(grid):
    count = 0
    n = len(grid)
    m = len(grid[0])
    newgrid = []
    newgrid.append([0]*(m + 2))
    for arr in grid:
        tmp = [0]
        for elem in arr:
            tmp.append(elem)    
        tmp.append(0)
        newgrid.append(tmp)
    newgrid.append([0]*(m + 2))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if is_greater(newgrid, i, j):
                count += 1
    print(count)

if __name__ == '__main__':
    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)
