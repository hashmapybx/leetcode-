# _*_ coding: utf-8 _*_
# @Time : 2021/7/6/0006 13:17 
# @Author : 流柯 
# @Version：V 0.1
# @File : Leetcode57_insert_interal.py
# @desc :



def insert(intervals, newInterval):

    result = []
    intervals.append(newInterval)
    if len(intervals) < 2:
        return intervals
    # 对区间进行排序
    intervals.sort(key=lambda x: x[0])
    for array in intervals:
        if len(result) == 0 or array[0] > result[-1][1]:
            result.append(array)
        else:
            result[-1][1] = max(result[-1][1], array[1])
    return result



"""
回溯法
    递归 
    需要判断回溯的条件。剪枝条件
    Leetcode 77 combination
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
    
    
    
    
"""

def backtracking(n, k, result, begin, param1):
    """

    :param n:
    :param k: k个数据的组合
    :param result:
    :param begin: 表示开始递归的数字
    :param param1:
    :return:
    """
    if len(param1) == k:
        result.append(param1[:])
        return
    for i in range(begin, n+1):
        param1.append(i)
        backtracking(n, k, result, i+1, param1)
        param1.pop()






def combination(n, k):
    """
    77题给定的整数
    :param n:
    :param k:
    :return:
    """
    result = []
    # 回溯
    backtracking(n,k, result, 1, [])
    return result

