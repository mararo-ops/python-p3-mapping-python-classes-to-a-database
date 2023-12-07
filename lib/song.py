import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:
    CURSOR = CURSOR
    CONN = CONN

    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.id = None

    def save(self):
        sql = """
        INSERT INTO songs(name, album) VALUES (?, ?)"""
        self.CURSOR.execute(sql, (self.name, self.album))
        self.CONN.commit()
        self.id = self.CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
        )"""
        cls.CURSOR.execute(sql)

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song

# Example usage
Song.create_table()
song = Song.create("Hold On", "Born to Sing")