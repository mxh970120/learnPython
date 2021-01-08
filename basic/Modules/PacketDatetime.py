from datetime import datetime, timedelta, timezone
now = datetime.now()  # 获取当前datetime
print(now)
print(type(now))

# 要指定某个日期和时间，我们直接用参数构造一个datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())  # 把本地时间转化为timestamp

t = 1429417200.0
print(datetime.fromtimestamp(t))  # timestamp转本地时间
print(datetime.utcfromtimestamp(t))  # timestamp转UTC时间

# str转换为datetime
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
tz_utc_1 = timezone(timedelta(hours=1))  # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_1)  # 强制设置为UTC+8:00
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=tz_utc_1)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)