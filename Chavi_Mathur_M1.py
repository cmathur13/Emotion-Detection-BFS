import collections

with open("m1_input.txt", "r") as file:
        grid = file.read()

# Split the grid_string into rows
rows = grid.split('\n')

# Split each row into individual elements and create a 2D list
grid = [list(row) for row in rows]

# Print the 2D array
for row in grid:
    print(row)

def emotion(grid: list[list[str]]) -> int:
    if not grid:
        return "No Emotion Found"
    
    rows, cols = len(grid), len(grid[0])
    visit=set()
    Emotion = ['Happy','Sad','Neutral']
    count = 0
    sad_count = 0
    happy_count = 0
    neutral_count = 0

    def bfs(r,c):
        q = collections.deque()
        nonlocal sad_count, happy_count, neutral_count, count
        visit.add((r,c))
        q.append((r,c))

        while q and count<=3:
            row, col = q.popleft()
            directions = [[-1,-1], [-1,1], [1,1], [1,-1],[0,1]]
            for dr, dc in directions :
                r, c = row + dr, col + dc
                
                if(r in range(rows) and
                c in range(cols) and
                 grid[r][c] == "1" and
                (r,c) not in visit):
                    q.append((r,c))
                    visit.add((r,c))
                    if(r<row or r==row): 
                        sad_count = sad_count+1
                        count = count+1
                    if(r>row or r==row):
                        happy_count= happy_count+1
                        count = count +1
                    if(r==row):
                        neutral_count = neutral_count +1
                        count = count +1    
                    
    for c in range(cols):
        for r in range(rows):
            if grid[r][c] == "1" and(r,c) not in visit:
                bfs(r,c)

                
    emoti = max(sad_count,happy_count,neutral_count)

    if neutral_count==emoti:
        return "The Emotion Detected is "+Emotion[2]
    elif sad_count==emoti:
        return "The Emotion Detected is "+Emotion[1]
    elif happy_count==emoti:
        return "The Emotion Detected is "+Emotion[0]

    
emotion(grid)