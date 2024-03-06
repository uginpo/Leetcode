def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if len(matrix) == 0:
        return []
    new_array = []
    x, y = 0, 0
    step = 1
    len_x, len_y = len(matrix[0]), len(matrix)
    r_x = 0
    r_y = 1

    steps = len_x * len_y
    direction = 'right'
    dx = 1
    dy = 0

    while step <= steps:
        match direction:
            case 'right':
                if x+dx > len_x-1:
                    len_x -= 1
                    direction = 'down'
                    dx = 0
                    dy = 1
            case 'down':
                if y+dy > len_y-1:
                    len_y -= 1
                    direction = 'left'
                    dx = -1
                    dy = 0
            case 'left':
                if x+dx < r_x:
                    r_x += 1
                    direction = 'up'
                    dx = 0
                    dy = -1
            case 'up':
                if y+dy < r_y:
                    r_y += 1
                    direction = 'right'
                    dx = 1
                    dy = 0
        new_array.append(matrix[y][x])
        step += 1
        x += dx
        y += dy

    return new_array


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix))
