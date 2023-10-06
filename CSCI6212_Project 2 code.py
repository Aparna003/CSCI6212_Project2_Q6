#Import libraries
import time
import random

# Function to generate circularly shifted array of different sizes for the algorithm
def circular_shifted_array_generation(n):
    # Generate a sorted array of random numbers
    array = [random.randint(1, 10000) for _ in range(n)]
    array.sort()

    # Choose a random shift position
    shift_pos = random.randint(0,n-1)
    
    # Perform circular shift to create the shifted array
    shifted_array = array[shift_pos:] + array[:shift_pos]
    return shifted_array

# circular shifted array size
arr_size = 10

# Generates a circular shifted array
shiftedArray = circular_shifted_array_generation(arr_size)

# Print the original sorted array and the circular shifted array
print("\nCircularly shifted and sorted array:")
print(shiftedArray)

start = time.time_ns()

#Function maxNumber finds the maximum number in the circular shifted array 
#using binary search approach. ( l - lower bound index, h - higher bound index)
def maxNumber(arr,l,h):

        # if only one element exists in array, return that as maximum 
        if(l==h): 
            return arr[l]
        # Finds the mid position of the array space
        mid = int((l+h)/2)
        # when mid element is largest (compared to)
        if (arr[mid]> arr[mid+1] and arr[mid]>arr[mid-1]):
            return (arr[mid])
        if (mid==0): # When current array size reduces and largest element is in index 0
            return (arr[mid])
        # searches the maximum element on left half of array if mid value is smaller 
        # than element at lowest index 
        if (arr[l] > arr[mid] ): 
            return maxNumber(arr, l, mid) 
        # Otherwise search in the right half of the array (recursive call) 
        return maxNumber(arr, mid + 1, h) 
        
#Function call to find maximum number from the shifted array
print(maxNumber(shiftedArray,0,arr_size-1))
# Calculates the algorithm execution end time
end= time.time_ns()
# Prints the total experimental time to execute the algorithm
print("Execution time=",end-start)