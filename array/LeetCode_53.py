# _*_ coding: utf-8 _*_
# @Time : 2021/7/1/0001 22:22 
# @Author : 流柯 
# @Version：V 0.1
# @File : LeetCode_53.py
# @desc :


# 暴力法求解最大连续子序列的和
# method 01
def maxSubArray(arr):
    """
    定义两个指针i j
    i 不动，移动j
    当j到达尾部，在移动i，重复前面的操作
    """
    result = float("-inf")  # 表示的是最下值
    for i in range(0, len(arr)):
        temp = 0
        for j in range(i, len(arr)):
            temp = temp + arr[j]
            result = max(temp, result)
    return result


# dynamic programing

def maxSubArrayDP(arr):
    """
    最大子序列的和
    在遍历到每一个位置的元素，其实它可以有两种选择，要不和前面序列的最大值合并，要不不合并，自己就是最大值
    :param arr:
    :return:
    """
    # 先是创建dp数组
    dp = [0] * len(arr)
    dp[0] = arr[0]
    result = arr[0]  # 记录最大值
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        result = max(result, dp[i])
    return result


def crossSum(nums, l, r):
    """
    获取中间位置的最大子序列的和
    :param nums:
    :param l:
    :param r:
    :return:
    """
    mid = l + (r - l) // 2
    leftSum = nums[mid]
    leftMax = leftSum
    for i in range(mid - 1, l - 1, -1):
        # 从中间位置往左边走
        leftSum += nums[i]
        leftMax = max(leftMax, leftSum)

    rightSum = nums[mid + 1]
    rightMax = rightSum
    # 从中间位置往右走
    for j in range(mid + 2, r + 1):
        rightSum = nums[j]
        rightMax = max(rightMax, rightSum)

    return leftMax + rightMax


# 方法三分治法
def getMax(nums, left, right):
    """
    递归获取最大值
    :param arr:
    :param left:
    :param right:
    :return:
    """
    # 递归的终止条件是
    if left == right:
        return nums[left]
    # 接下来是二分的递归
    mid = left + (right - left) // 2
    leftSum = getMax(nums, left, mid)
    rightSum = getMax(nums, mid + 1, right)
    # 中间位置的最大值
    crosssum = crossSum(nums, l, r)


def maxSubArrayDevid(arr):
    """
    还是去递归的掉
    :param arr:
    :return:
    """
    return getMax(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2]
    res = maxSubArray(arr)
    print("最大的连续子序列和是:", res)
