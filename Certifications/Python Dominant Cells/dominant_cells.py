"""
2. Python: Dominant Cells
There is a given list of lists of integers that represent a 2-dimensional grid with n rows and m columns. 
A cell is called a dominant cell if it has a strictly greater value than all of its neighbors. 
Two cells are neighbors when they share a common side or a common corner, so a cell can have up to 8 neighbors. Find the number of dominant cells in the grid.

Function Description
Complete the function numCells in the editor below.

numCells has the following parameter(s):
    int grid[n][m]: a 2-dimensional array of integers

Returns
    int: the number of dominant cells in the grid

Constraints
    1≤n, m≤500
    There are at least 2 cells in the grid.
    1 ≤ grid[i][j] < 100


Input Format Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

The first line contains an integer n, the number of rows in the grid.
The second line contains an integer m, the number of columns in the grid.
Next, n lines follow. The i-th of them contains m integers denoting the cells in the i-th row of the grid.

Sample Case 0

Sample Input 0

STDIN             Function

3 → n = 3
3 → m = 3
grid [[1, 2, 7], [4, 5,6], [8, 8, 9]]
4 5 6
8 8 9

Sample Output 0
2

Explanation 0
There are 3 cells that have strictly greater values than all their neighboring cells. These cells are:
"""


def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Define relative positions of 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    count = 0

    for i in range(n):
        for j in range(m):
            current = grid[i][j]
            dominant = True
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] >= current:
                        dominant = False
                        break
            if dominant:
                count += 1

    return count


if __name__ == "__main__":
    grid = [
        [1, 2, 7],
        [4, 5, 6],
        [8, 8, 9]
    ]
    print(numCells(grid))  # Output: 2
