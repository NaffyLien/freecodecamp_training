def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n <= 1:
        return "Argument must be an integer greater than 0."

    pattern = []
    for i in range(n):
        pattern.append(str(i+1))
    pattern = " ".join(pattern)
    return pattern

print(number_pattern(5))