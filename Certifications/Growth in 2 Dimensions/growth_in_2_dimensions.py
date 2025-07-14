"""
1. Growth in 2 Dimensions

Determine the highest value after executing in steps on an infinite 2D grid that initially contains all zeros. 
The grid is indexed from (1,1) at the bottom-left corner with coordinates increasing upwards and to the right.

For each given coordinate pair (r, c), the row and column, increment every cell in the range from (1,1) to (r, c) inclusive by 1. 
After processing all coordinates, return the number of cells that contain the maximum value in the grid.

Example
upRight["14", "23", "41"]

The two space-separated integers within each string represent r and c respectively. 
The following diagrams show each iteration starting at zero. The maximal value in the grid is 3, and there is 1 occurrence at cell (1, 1)


Function Description
Complete the function countMax in the editor with the following parameter(s):
    string upRight[n]: an array of strings made of two space-separated integers, r and c

Return
    long: the number of occurrences of the final grid's maximal element

Constraints
1 <= n <= 100
1 <= number of rows, number of columns ≤ 10^6

▼Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

The first line contains an integer n, the size of the array upRight.
Each of the next n lines contains a string of two space-separated integers representing coordinates r and c for element upRight[i].

▼ Sample Case 0

Sample Input

STDIN          Function

3          -->     upRight[ ] size n = 3
2   3    -->      upRight = ['2 3', '3 7', '4 1')
3   7
4  1

Sample Output
2
"""


def countMax(upRight):
    # Initialize with very large values
    min_row = float('inf')
    min_col = float('inf')
    
    # Parse each "r c" string and track the minimums
    for coord in upRight:
        r, c = map(int, coord.split())
        min_row = min(min_row, r)
        min_col = min(min_col, c)
    
    # The intersection area is the number of max-value cells
    return min_row * min_col    


if __name__ == '__main__':
    # Sample input
    upRight = ["2 3", "3 7", "4 1"]

    # Output should be 2 (cells in the 2x1 area)
    print(countMax(upRight))  # Output: 2