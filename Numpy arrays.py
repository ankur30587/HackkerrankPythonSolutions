import numpy

def arrays(arr):
    # Convert the list to a NumPy array with float type
    numpy_array = numpy.array(arr, float)
    
    # Reverse the NumPy array
    reversed_array = numpy.flip(numpy_array)
    
    return reversed_array
arr = input().strip().split(' ')
result = arrays(arr)
print(result)