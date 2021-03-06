"""
Author :    Kumar Shanu
Problem :   Subset of given sum is exists or not

Dynamic Programming
"""


def isSubset_rec(arr: "list[int]", n: "int", target: "int") -> bool:
    """Subset sum problem recursive solution

    Args:

        arr (list[int]): array of integer
        n (int): lenght of the array
        target (int): given sum

    Returns:

        bool: True or False
    """
    if(target == 0):
        return True

    if(n == 0):
        return False

    if(arr[n-1] <= target):
        return isSubset_rec(arr, n-1, target-arr[n-1]) or isSubset_rec(
            arr, n-1, target)
    else:
        return isSubset_rec(arr, n-1, target)


def isSubset_sum(arr: "list[int]", target: "int") -> bool:
    """Subset sum problem

    Find out if subset is exists in the given set with the given sum
    using dynamic programming

    Args:

        arr (list[int]): set/array/list of elements
        target (int): target sum

    Returns:

        bool: True if subset exists otherwise False
    """
    dp = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]

    for i in range(len(arr)+1):
        dp[i][0] = True

    for i in range(1, len(arr)+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[-1][-1]


if __name__ == "__main__":
    arr = [2, 3, 5, 7, 10]
    S = 14
    print("Subset exists with the given sum? ", isSubset_sum(arr, S))
