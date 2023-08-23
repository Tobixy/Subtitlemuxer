import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('muxdb.sqlite', check_same_thread=False)
        self.setup()

    def setup(self):
        cmd = """CREATE TABLE IF NOT EXISTS muxbot(
        user_id INTEGER PRIMARY KEY,
        vid_name TEXT,
        sub_name TEXT,
        filename TEXT
        );"""
        self.conn.execute(cmd)
        self.conn.commit()

    def put_video(self, user_id, vid_name, filename):
        ins_cmd = 'INSERT OR REPLACE INTO muxbot VALUES (?,?,?,?);'
        data = (user_id, vid_name, None, filename)
        self.conn.execute(ins_cmd, data)
        self.conn.commit()

    def put_sub(self, user_id, sub_name):
        ins_cmd = 'INSERT OR REPLACE INTO muxbot VALUES (?,?,?,?);'
        data = (user_id, None, sub_name, None)
        self.conn.execute(ins_cmd, data)
        self.conn.commit()

    def check_sub(self, user_id):
        cmd = f'SELECT sub_name FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        return bool(res and res[0])

    def check_video(self, user_id):
        cmd = f'SELECT vid_name FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        return bool(res and res[0])

    def get_vid_filename(self, user_id):
        cmd = f'SELECT vid_name FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        return res[0] if res else None

    def get_sub_filename(self, user_id):
        cmd = f'SELECT sub_name FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        return res[0] if res else None

    def get_filename(self, user_id):
        cmd = f'SELECT filename FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        return res[0] if res else None

    def erase(self, user_id):
        erase_cmd = f'DELETE FROM muxbot WHERE user_id={user_id};'
        try:
            self.conn.execute(erase_cmd)
            self.conn.commit()
            return True
        except:
            return False
