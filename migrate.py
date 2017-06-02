#!/usr/bin/python env
import sqlite3 as sql

def creat_db():
    conn = sql.connect('store.db')
    conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    conn.close()


if __name__ == '__main__':
    creat_db()


