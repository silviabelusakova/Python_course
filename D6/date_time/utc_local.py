#!/usr/bin/python3

import arrow

now = arrow.now()
print(now)
print(now.to('UTC'))

# import datetime
# print(datetime.datetime.utcnow())
# print(datetime.datetime.now())