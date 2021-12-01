def get_result(values):
    window_sums = [sum((values[index-2], values[index-1], values[index])) for index, value in enumerate(values)]
    return len([value for index, value in enumerate(window_sums) if window_sums[index] > window_sums[index-1]])
