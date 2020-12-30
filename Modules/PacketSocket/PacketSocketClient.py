# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
                                                       # SOCK_STREAM指定使用面向流的TCP协议
# 建立连接:
# IP地址和端口号，SMTP服务是25端口，FTP服务是21端口，web服务是80
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)  # recv(max)方法，一次最多接收指定的字节数，
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('../sina.html', 'wb') as f:
    f.write(html)