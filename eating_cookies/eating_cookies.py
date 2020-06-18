'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, optional = 0):
    # Your code here
    prev1, prev2, prev3 = 1, 1, 0
    combinations = 1
    for i in range (1, n):
        combinations = prev1 + prev2 + prev3
        prev3, prev2, prev1 = prev2, prev1, combinations

    return combinations



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
