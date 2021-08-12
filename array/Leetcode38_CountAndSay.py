# _*_ coding: utf-8 _*_
# @Time : 2021/6/27/0027 15:30 
# @Author : 流柯 
# @Version：V 0.1
# @File : Leetcode38_CountAndSay.py
# @desc :



# leetcode 38题 描述数字字符串  12 --》 1112 表示的是一个1， 1个2
def get_next(res):
    # dict_ = {res: 1}
    # res = dict_.get(res) + res
    length = len(res)
    num = 1
    first = res[0]
    ans = ""
    for i in range(1, length):
        # 从第二个位置开始比较
        if res[i] == first:
            num +=1
        else:
            ans = ans +str(num) + str(first)
            first = res[i]
            num =1
    ans += str(num) + str(first)

    return  ans


def CountAndSay(num):
    """
    给定一个正数n, 输出外观描述的第n项
    :param num:
    :return:
    """
    res = "1"
    if num == 0: return None
    start = 1

    for i in range(1, num):

        get_next(res)
    return res



