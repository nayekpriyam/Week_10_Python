def largest_rectangle_histogram(heights):
    stack = []
    max_area = 0
    extended = heights + [0]
    for i, h in enumerate(extended):
        while stack and extended[stack[-1]] > h:
            height = extended[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            area = height * (i - left)
            if area > max_area:
                max_area = area
        stack.append(i)
    return max_area
