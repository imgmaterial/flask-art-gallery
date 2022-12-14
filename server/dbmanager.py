import sqlite3 as sl

con = sl.connect("image_info.db")

with con:
    
    #con.execute("DROP TABLE IF EXISTS info; CREATE TABLE info(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,image_name TEXT, author TEXT, neural_network TEXT);")
    #con.execute("DROP TABLE IF EXISTS tags; CREATE TABLE tags(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, tag_name TEXT)")

    #con.execute("""INSERT INTO info (image_name) VALUES ("00001.png")""")
    #con.execute("""INSERT INTO tags (tag_name) VALUES ("1girl")""")
    #con.execute("""CREATE TABLE IF NOT EXISTS object_tag_mapping (object_reference INTEGER, tag_reference INTEGER);""")
    #con.execute("""INSERT INTO object_tag_mapping VALUES (1,1)""")
    output = con.execute("SELECT * FROM TAGS WHERE id = 2")
    print(output.fetchall())