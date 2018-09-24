import sqlite3

class Db:
    # Create database 
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName) 
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS `songs` ( `artist` TEXT PRIMARY KEY, `title` TEXT UNIQUE)')
        self.conn.commit()
    # Add song artist and title to database
    def addSong(self, artist, title):
        if (artist != ''):
            self.cursor.execute('''INSERT OR IGNORE INTO songs (artist, title) VALUES (?, ?)''', (str(artist), str(title)[3:]))
            self.conn.commit()
    # Close database
    def openDB(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
    def closeDB(self):
        self.conn.close()  