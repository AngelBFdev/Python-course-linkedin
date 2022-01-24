#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sqlite3

def main():
    print('connect')
    # connect to the database name db-api.db
    # if doesn't exist create one
    db = sqlite3.connect('db-api.db')
    # with this we can execute sql consults
    cur = db.cursor()

    print('create')
    # drop the table if already exist
    cur.execute("DROP TABLE IF EXISTS test")
    # create table name test with id, string and number
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)

    print('insert row')
    # insert in test table, values: string='one', number=1
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)

    print('commit')
    # we commit the inserts
    db.commit()

    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    # save the result of the last query
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')

    print('read')
    # print all rows
    for row in cur.execute("SELECT * FROM test"):
        print(row)

    print('drop')
    cur.execute("DROP TABLE test")

    print('close')
    # close the table
    db.close()

if __name__ == '__main__': main()
