def max_area(height):
    max_area = 0
    len_height = len(height)

    start = 0
    end = len_height - 1
    while start < end:
        current_area = min(height[start], height[end]) * (end - start)
        max_area = max(current_area, max_area)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return max_area
