# ---------------------------------Subarrays in Python---------------------------

# Creating Subarray
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub1 = arr[2:5]  # Elements from index 2 to 4 (5 is excluded)
print(sub1)  # Output: [3, 4, 5]

sub2 = arr[:3]  # Elements from beginning to index 2 (3 is excluded)
print(sub2)  # Output: [1, 2]

sub3 = arr[6:]  # Elements from index 6 to end
print(sub3)  # Output: [7, 8, 9]

sub4 = arr[:]  # Entire array (a copy of the original)
print(sub4)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generate All Subarray
def sub_Array(arr):
    for i in range (0,len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
arr=[1,2,3,4,5]
print("All Non-empty Subarrays")
sub_Array(arr)



