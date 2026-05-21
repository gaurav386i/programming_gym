def dfs_grid(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
        return
    # mark visisted 
    grid[r][c] = "0"
    # visit all nearby cells 
    dfs_grid(grid, r + 1, c)
    dfs_grid(grid, r - 1, c)
    dfs_grid(grid, r, c + 1)
    dfs_grid(grid, r, c - 1)


def number_of_islands(grid):
    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs_grid(grid, r, c)
    return islands


"""
## 9) Search a 2D Matrix

**Topic:** Searching, Binary Search, Matrices
**Difficulty:** Medium
**Suggested time limit:** 15 minutes

You are given an `m x n` integer matrix `matrix` with the following two properties:

* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, or `false` otherwise.

### Example 1

**Input:**
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3`
**Output:**
`true`

### Example 2

**Input:**
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13`
**Output:**
`false`

### Constraints

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* `-10^4 <= matrix[i][j], target <= 10^4`

"""

def find_in_2d_matrix(mat: list[list[int]], target: int) -> bool:
    rows = len(mat)
    cols = len(mat[0])
    r = 0
    c = cols - 1
    while r < rows and c >= 0:
        if mat[r][c] == target:
            return True
        elif mat[r][c] > target:
            c -= 1
        elif mat[r][c] < target:
            r += 1
    return False


def diagonal_swap(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):   # only upper triangle
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
           


def rotate_90_manual(matrix):
    n = len(matrix)

    # Step 1: diagonal swap
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row (no built-in reverse)
    for i in range(n):
        left = 0
        right = n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]

            left += 1
            right -= 1




if __name__ == "__main__":
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    # print(number_of_islands(grid2))
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(find_in_2d_matrix(matrix1, target = 34))