import sqlite3
import time

class Db():
    def get_info(self, name):
        start_time = time.time()
        name = str(name).lower().replace("g'",'g‘').capitalize()
        conn = sqlite3.connect('full.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ismlar WHERE ism=(?)", (name,))
        result = c.fetchone()
        conn.commit()
        conn.close()
        try:
            duration = round(time.time()-start_time, 4)
            return {'title':result[0], 'meaning':result[2], 'types':result[3], 'category':result[4], 'views':result[5], 'duration':duration}
        except:
            return False

db = Db()