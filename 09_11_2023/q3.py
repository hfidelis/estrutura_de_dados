def max_min(arr: list) -> list:
    return [max(arr, key=int), min(arr, key=int)]

arr: list = [1, 20, 30, 40, 50, 100]
res: list = max_min(arr)

print(f'Maior: {res[0]} | Menor: {res[1]}')