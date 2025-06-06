# Generic Binary Search Algorithm

# Problem: Find a given value in an list

# Helper function which captures edge case when the val is an element of arr multiple times 
def test_location(arr, val, midIndex):
    mid_number = arr[midIndex]

    if mid_number == val:
        # We only want to move left if values are repeated
        if midIndex-1 >=0 and arr[midIndex-1] == val:
            return 'left'
        else:
            return 'found'
        # This assumes the list is sorted from high to low 
    elif mid_number < val:
        return 'left'
    else:
        return 'right'

def locate_val(arr, val):
    # Set pointers to [0,N) 
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        midIndex = (lo + hi) // 2
        result = test_location(arr, val, midIndex)

        if result == 'found':
            return midIndex
        elif result == 'left':
            hi = midIndex - 1
        elif result == 'right':
            lo = midIndex + 1
    
    # val not found in arr
    return -1

tests = []

tests.append({ 
    'input': {
        'arr': [13,11,10,7,4,3,0],
        'val': 1
    },
    'output': 6
})

for i in range(0,len(tests)-1):
    result = locate_val(tests[i][{'arr'}], tests[i][{'val'}])
    output = tests[i]['output']
    print('Result: ',result)
    if result != output:
        print('Test Failed. \n Expected: ', output,'\n Detected: ',result)
    else:
        print ('Test Passed')