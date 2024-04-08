# Номер успешной посылки 110220289
def find_amount_platforms(weight: list[int], limit: int) -> int:
    """Возвращает количество платформ, необходимых для перевозки."""
    weight.sort()
    count_value = 0
    count_value = len(weight)
    left_pointer = 0
    right_pointer = len(weight) - 1
    while left_pointer < right_pointer:
        if weight[left_pointer] + weight[right_pointer] <= limit:
            left_pointer += 1
            right_pointer -= 1
            count_value -= 1
        else:
            right_pointer -= 1

    return count_value


if __name__ == '__main__':
    weight = [int(x) for x in input().split()]
    limit = int(input())
    print(find_amount_platforms(weight, limit))