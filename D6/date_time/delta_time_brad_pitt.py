#!/usr/bin/env python 

import datetime

dob = datetime.date(1963, 12, 18)
print(dob)

now = datetime.date.today()
print(now)

delta = now - dob
print(delta)