def search_for_number(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

array = [1,2,3,4]
result = search_for_number(array, 4)
print("index of 4:", result)