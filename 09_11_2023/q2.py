def arr_media(arr: list) -> float:
    return round(sum(arr)/len(arr), 2)

print(arr_media([10, 20, 35, 48, 75, 90]))