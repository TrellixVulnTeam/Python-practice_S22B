#!/user/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timezone, timedelta


# now = datetime.now()
# print(now)
# print(type(now))
# print(now.timestamp())

# dt = datetime(2016, 4, 17, 14, 34, 15)
# print(dt)
# print(type(dt))
# print(dt.timestamp())

# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))

# str转换为datetime
# cday = datetime.strptime('2016-06-01 18:19:57', '%Y-%m-%d %H:%M:%S')
# print(cday)

# datetime转换为str
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# now = datetime.now()
# print(now)
# print(datetime(2015, 5, 18, 16, 57, 3, 540997))
# print(now + timedelta(hours=10))
# print(now + timedelta(days=2, hours=12))
# print(datetime(2015, 5, 18, 16, 57, 3, 540997) + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
# tz_utc_8 = timezone(timedelta(hours=8))

# now = datetime.now()
# print(now)
# print(now.replace(tzinfo=tz_utc_8))

# print(datetime.utcnow())
# print(datetime.utcnow().replace(tzinfo=timezone.utc))
# print(datetime.utcnow().replace(tzinfo=tz_utc_8))

# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)

# bj_dt = utc_dt.astimezone(tz_utc_8)
# print(bj_dt)

# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)

# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    re_tz = re.compile(r'UTC([+-]\d+):00')
    tz_hour = re_tz.match(tz_str).group(1)
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt_tz = dt.replace(tzinfo=timezone(timedelta(hours=int(tz_hour))))
    return dt_tz.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')