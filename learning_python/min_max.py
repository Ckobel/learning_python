def min_max(arr):

    _min,_max = arr[0],arr[0]

    for num in arr:
        if num < _min:
            _min = num
        if num > _max:
            _max = num
            
    return _min,_max

list_of_nums = [1,2,3,4,6,1,2,3,49,123,3,2,1,3,40,10,-9]
minimum,maximum = min_max(list_of_nums)

print minimum
print maximum
