'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    index = 0
    arr.sort()
    while index < len(arr) - 1:
        if arr[index] == arr[index+1] and index < len(arr)-3:
            del arr[index:index+2]
        elif arr[index] == arr[index+1]:
            del arr[index:]
        else:
            index += 1
    return arr[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")