class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        i, j = 0,0
        UP, RIGHT, DOWN, LEFT = 0, 1 , 2, 3

        TOP_WALL = 0
        RIGHT_WALL = n
        BOTTOM_WALL = m
        LEFT_WALL = -1

        direction = RIGHT

        while len(res) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                i,j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < BOTTOM_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                BOTTOM_WALL -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = UP

            else:
                while i > TOP_WALL:
                    res.append(matrix[i][j])
                    i -= 1

                i,j = i+1, j+1
                TOP_WALL += 1
                direction = RIGHT

        return res


