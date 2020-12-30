# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities

import psutil
print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_count(logical=False)) # CPU物理核心
print(psutil.cpu_times())  # 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_percent(interval=1, percpu=True))  # CPU使用率
print(psutil.virtual_memory())  # 物理内存
print(psutil.swap_memory())  # 交换内存
print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('/'))  # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO
