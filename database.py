import sqlite3

# create database
conn = sqlite3.connect('new.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txt TEXT \
        )")
    
    conn.commit()
conn.close()


conn = sqlite3.connect('new.db')


with conn:
    cur = conn.cursor()
    item = cur.typeof()
    for item in fileList:
        fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg').format(item)
        
       
    
