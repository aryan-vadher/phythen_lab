#1 positional array indexing
arr = [10,"10", "20", "30", "40", "50"]
print(arr[0])
print(arr[2])
print(arr[4])

#negative

arr = [10,"10", "20", "30", "40", "50"]
print(arr[-1])
print(arr[-2])
print(arr[-4])


# modify

from array import array
my_array = array ('i',[1,2,3,4])
my_array [0] = 5
print(my_array)
