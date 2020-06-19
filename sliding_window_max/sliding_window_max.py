'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here

    # not my code, still fails, but closer. included so I can try to figure out why it's better. 
    # results = []
    # n = len(nums)
    # indices = [0 for i in range(n)]
    # s = [0]
    # for i in range(1, n):
    #     while len(s) > 0 and nums[s[-1]] < nums[i]:
    #         indices[s[-1]] = i - 1
    #         del s[-1]
    #     s.append(i)
    # while len(s) > 0:
    #     indices[s[-1]] = n - 1
    #     del s[-1]
    # j = 0
    # for i in range(n - k + 1):
    #     while (j < i or indices[j] < i + k - 1):
    #         j += 1
    #     results.append(nums[j])
    # return results

    #method 2 fails large test
    arr = list(max(nums[i:i+k]) for i in range(len(nums)-(k-1)))
    return arr

    # Method 1 fails large test
    # arr = []
    # for i in range(len(nums)-(k-1)):
    #     arr.append(max(nums[i:i+k]))
    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
