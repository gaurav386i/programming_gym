"""
I|P = 1 0 1      O/P = 1 0 0
      1 1 0            1 1 0
      0 1 1            0 1 1
"""

def printSolution(sol: list[list[int]]) -> None:
    N = len(sol)
    for i in range(N):
        for j in range(N):
            print(sol[i][j], end=" ")
        print()

def isSafe(maze: list[list[int]], i: int, j: int) -> bool:
    return i < len(maze) and j < len(maze) and maze[i][j] == 1

def solveMazeRec(maze: list[list[int]], i: int, j: int, sol: list[list[int]]) -> bool:
    n = len(maze) - 1
    if i == n and j == n and maze[i][j] == 1:
        sol[i][j] = 1
        return True
    if isSafe(maze, i, j) == True:
        sol[i][j] = 1
        if solveMazeRec(maze, i + 1, j, sol) == True:
            return True
        if solveMazeRec(maze, i, j + 1, sol):
            return True
        sol[i][j] = 0
    return False

def solveMaze(maze: list[list[int]]) -> True:
    N = len(maze)

    sol = [[0 for j in range(N)] for j in range(N)]

    if solveMazeRec(maze, 0, 0, sol) == False:
        print("Solution don't exists")
    printSolution(sol)
    return True


if __name__ == "__main__":
    maze = [
        [1, 0, 1], 
        [1, 1, 0], 
        [0, 1, 1]
    ]
    solveMaze(maze)


