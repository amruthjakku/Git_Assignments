
def swap_elements(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
    return arr
my_list = [10, 20, 30, 40, 50]
swap_elements(my_list, 1, 3)
print(my_list)  # [10, 40, 30, 20, 50]