# Номер успешной посылки 111692299
def find_amount_platforms(weights, limit):
    """Возвращает количество платформ, необходимых для перевозки."""
    weights_sorted = sorted(weights.copy())
    count_value = len(weights)
    light_pointer = 0
    heavy_pointer = count_value - 1
    while light_pointer < heavy_pointer:
        if (weights_sorted[light_pointer] +
                weights_sorted[heavy_pointer] <= limit):
            light_pointer += 1
            count_value -= 1
        heavy_pointer -= 1
    return count_value


if __name__ == '__main__':
    print(find_amount_platforms(weights=[int(x) for x in input().split()],
                                limit=int(input())))

