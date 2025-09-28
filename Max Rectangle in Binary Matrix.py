def largest_rectangle_histogram(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            L = stack[-1] + 1 if stack else 0
            max_area = max(max_area, H * (i - L))
        stack.append(i)
    return max_area

def maximal_rectangle(matrix):
    if not matrix: return 0
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' or row[i] == 1 else 0
        max_area = max(max_area, largest_rectangle_histogram(heights))
    return max_area
