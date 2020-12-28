# logging模块可以非常容易地记录错误信息
import logging
# 它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        logging.info('error')

main()
print('END')