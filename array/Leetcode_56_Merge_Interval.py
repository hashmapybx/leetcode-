# _*_ coding: utf-8 _*_
# @Time : 2021/7/2/0002 13:09 
# @Author : 流柯 
# @Version：V 0.1
# @File : Leetcode_56_Merge_Interval.py
# @desc :


## leetcode 56题的操作是合并区间


# 首席将各个区间按照开始的左区间值排序。



def merge(arr):
    """
    传入是[[1,2], [3,6], [4,9]]
    输出[[1,9]]
    :param arr:
    :return:
    """
    # corner case
    if len(arr) <2:
        return arr

    result = [] # [[1,2]]
    for array in arr:
        if len(result) or array[0] > result[-1][1]:
            # 当result 最后一个元素里面的右边界
           result.append(array)
        else:
            # 当右边界大于array[0]
            result[-1][1] = max(array[1], result[-1][1])

    return result




