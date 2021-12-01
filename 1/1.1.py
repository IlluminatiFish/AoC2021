def get_result(values):
  return len([value for index, value in enumerate(values) if value > values[index - 1]])
