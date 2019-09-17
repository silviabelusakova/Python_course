#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import sys

con = None

try:                                                       #nahradza 'with' open 
    con = sqlite.connect('ydb.db')

    cur = con.cursor()                      #specialny objekt, na kurzore volam exe cmd ktory vykona operaciu 
    cur.execute('SELECT SQLITE_VERSION()')  #python db pep - formal doc ktory dokumentuje jednotl funkcie pre sql 

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")

except sqlite.Error as e:

    print(f"Error {e.args[0]}")
    sys.exit(1)

finally:                                                 #vykona sa vzdy, aby sa uvolnilo pripojenie resp. pristup k db/page

    if con:
        con.close()