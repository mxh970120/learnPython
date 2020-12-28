# 一般方法
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 简洁方法
with open('/path/to/file', 'r') as f:
    print(f.read())

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
f = open('/Users/michael/test.jpg', 'rb')

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
# 务必要调用f.close()来关闭文件
f.close()

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')