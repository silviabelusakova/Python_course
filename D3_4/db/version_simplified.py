#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import sys

with sqlite.connect('ydb.db') as con:


    cur = con.cursor()                      #specialny objekt, na kurzore volam exe cmd ktory vykona operaciu 
    cur.execute('SELECT SQLITE_VERSION()')  #python db pep - formal doc ktory dokumentuje jednotl funkcie pre sql 

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")

