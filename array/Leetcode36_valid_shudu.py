# _*_ coding: utf-8 _*_
# @Time : 2021/6/27/0027 14:18 
# @Author : 流柯 
# @Version：V 0.1
# @File : Leetcode36_valid_shudu.py
# @desc :

# leetcode 上面的36题  就是要去计算判断给的一个数独是否是合规
def test(board):
    """
    9*9的数独
    其中要求每一行上面的数值只出现一次
    每一列上看的数值只出现一次
    简单的方法是我们利用hash映射 value-> count
    :param board:
    :return:
    """
    arr = [[1,2], [3,4]]
    # 获取数独的row去判断是不是合法的
    # row = [[x for x in y if x != '.'] for y in arr]
    # col = [[x for x in y if x != '.']for y in zip(*arr)] # zip 的操作有点像转置
    row = [set() for i in range(9)]
    col = [set() for i in range(9)]
    block = [[set() for i in range(3)] for j in range(3)] # 这个是产生一个3*3的两个维数组
    print(block)
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in block[i/3][j/3]:
                    print(i,j)
                    return False
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            block[i/3][j/3].add(board[i][j])
    return True



if __name__ == '__main__':
    test()