"""Сортировка слиянием"""
import time
from random import randint

arr = [randint(0,999) for i in range(200000)]
#arr = [1, 5, 3, 2, 4, 7, 6, 9, 8]

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_it = f'время выполнения {(end - start)*1000:.3f} ms'

        return result, time_it
    return wrapper

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_sort = merge_sort(arr[:mid])
    right_sort = merge_sort(arr[mid:])

    return merge_arr(left_sort, right_sort)

def merge_arr(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
            result.append(right[j])
            j += 1
    return result

@timeit
def run_func(func, arr):
    return func(arr)

result, time_it = run_func(merge_sort, arr)
print(*result[:10],"\n"+time_it)
log = f"Для массива {len(arr)} элементов - {time_it}\n"
with open("log_merge_sort.txt", "a",encoding="utf-8") as f:
    f.write(log)




