#!/usr/bin/env python3

import requests as req

resp = req.get("http://www.webcode.me/about2.html")



print(resp.text)
print('****************************')
print(resp.status_code)
#print(resp.url) #### vylistujeme text, url, cookies, history, etc. 