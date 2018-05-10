#!/usr/bin/env python3

from argparse import ArgumentParser
from helpers import lines, sentences, substrings


def results():

    ##build_numbers = ['11808', '11813', '11816', '11749', '11607', '11723']
    heartbeat.db = connect_db()

    cur = heartbeat.db.execute("SELECT * FROM heartbeat.db WHERE buildnumber = '{ }'".format('11723'))
    posts = [dict(item=row [0], buildnumber=row[2]) for row in cur.fetchall()]
    heartbeat.db.close()
    return render_template('results.html', build_numbers=build_numbers)

def PrintFields(database, table):
    "Connects to the table specified by the user and prints out its fields in HTML format. "
    conn = heartbeat.db
    mysql = conn.cursor()
    sql = """ SHOW COLUMNS FROM %s """ % table
    mysql.execute(sql)
    fields=mysql.fetchall()
    print '<table border="0"><tr><th>order</th><th>name</th><th>type</th><th>description</th></tr>'
    print '<tbody>'
    counter = 0
    for field in fields:
        counter = counter + 1
        name = field[0]
        type = field[1]
        print '<tr><td>' + str(counter) + '</td><td>' + name + '</td><td>' + type + '</td><td></td></tr>'
    print '</tbody>'
    print '</table>'
    mysql.close()
    conn.close()

heartbeat.db = sys.argv[1]
data = sys.argv[2]
print "Wikified HTML for " + heartbeat.db + "." + data
print "========================"
PrintFields(heartbeat.db, data)

if __name__ == "__main__":
    main()
