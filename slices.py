# basic slices

arr = [10,"10", "20", "30", "40", "50"]
print(arr[1:4])
print(arr[:3])
print(arr[3:])
print(arr[:])

# slice with step

arr = [10,"10", "20", "30", "40", "50"]
print(arr[::2])
print(arr[1::2])
print(arr[::3])

# negative

arr = [10,"10", "20", "30", "40", "50"]
print(arr[-4:-1])
print(arr[-1::-2])
print(arr[::-3])

# reverse slicing

arr = ('i', [1,2,3,4])
print(arr[::-1])

# modify 
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30] 
print(numbers)