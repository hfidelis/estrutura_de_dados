def bubble_sort(arr: list) -> list:
    sorted: bool = False
    
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = True
        if not sorted:
            return
    return arr
 

arr: list = list(map(int, input().split())) + list(map(int, input().split()))
print(bubble_sort(arr))