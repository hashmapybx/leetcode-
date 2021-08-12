# _*_ coding: utf-8 _*_
# @Time : 2021/7/24/0024 16:52 
# @Author : 流柯 
# @Version：V 0.1
# @File : monitor_memory.py
# @desc :


def memory_status():
    """
    将内存信息写入到kafka里面去，flink去实时消费数据写入到数据仓库的CDS层。
    需要注意的地方：

    """
    mem = {}
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2:
            continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = float(var)
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    # 记录内存使用率 已使用 总内存和缓存大小
    res = {}
    res['percent'] = int(round(mem['MemUsed'] / mem['MemTotal'] * 100))
    res['used'] = round(mem['MemUsed'] / (1024 * 1024), 2)
    res['MemTotal'] = round(mem['MemTotal'] / (1024 * 1024), 2)
    res['Buffers'] = round(mem['Buffers'] / (1024 * 1024), 2)
    return res

# 这个结果去写入到kafka里面去



