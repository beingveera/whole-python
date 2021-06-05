# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:14:08 2020

@author: techno
"""
import sqlite3 as sq 

dbs=sq.connect('vee.db')
#mem=sq.connect(':memory:')
#print(dbs)
#print(mem)

cur=dbs.cursor()

#cur.execute('CREATE TABLE data(id INTEGER PRIMARY KEY, name VARCHAR(50),email VARCHAR(50))')
nam='lokesh'
mail='veera@gmail.com'
cur.execute("INSERT INTO names VALUES(null,'sharma','veera123@gmail.com')")

dbs.commit()