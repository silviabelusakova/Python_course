#!/usr/bin/python3

from datetime import datetime

now = datetime.now()
print(now.isoformat())

# dt1 = datetime.strptime('Jun 1 2018 5:33PM', '%b %d %Y %I:%M%p')
# print(dt1)

# dt2 = datetime.strptime('23:33:45', '%H:%M:%S')
# print(dt2.time())


#uloha - rozparsovat zadany datum

# ds = 'August 20 2020'
# ds_parse = datetime.strptime(ds, '%B %d %Y' )     #argument za % pozriet podla typu kodovania napr %B - full month name 
# print(ds_parse)

