def even_numbers(arr: list) -> list:
    return list(filter(lambda x: x % 2 == 0, arr))

arr: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(arr))