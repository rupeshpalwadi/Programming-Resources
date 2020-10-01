from pprint import pprint

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]


def psa_2d(grid):
    # Adding 1 to each dimension for easy query
    grid_w = len(grid[0]) + 1
    grid_h = len(grid) + 1

    query = [[0]*(grid_w) for i in range(grid_h)]
    query[1][1] = grid[0][0]

    # Exception 1: Filling row 1 (query[1])
    for i in range(1, grid_w):
        query[1][i] = query[1][i-1] + grid[0][i-1]

    # Exception 2: Filling column 1 (query[1])
    for i in range(1, grid_h):
        query[i][1] = query[i-1][1] + grid[i-1][0]

    # From row 1 and column 1 fill the rest by performing following operations
    # Adding the 4x4 grid, minus top left, plus current in grid
    for i in range(2, grid_h):
        for j in range(2, grid_w):
            query[i][j] = query[i - 1][j] + query[i][j - 1] - query[i - 1][j - 1] + grid[i-1][j-1]
    
    return query

# Printing the 2D PSA
pprint(psa_2d(grid))

# Querying the 2D PSA: Sum of values from (a1, b1) to (a2, b2) where (a1, a1) <= (b1, b2)
a1, a2 = (0, 0)
b1, b2 = (1, 1)

print(psa_2d(grid)[a1][a2] + psa_2d(grid)[b1+1][b2+1] - psa_2d(grid)[a1][b2+1] - psa_2d(grid)[b1+1][a2])
