from application.models import Media, Format
import sqlite3 as sql


class DataBase:
    def __init__(self, database):
        self.INSERT_MEDIA_VALUE = "INSERT INTO MEDIA (title, format_id, shared_disc, run_time) VALUES(?, ?, ?, ?);"
        self.INSERT_FORMAT_VALUE = "INSERT INTO FORMATS (format_name) VALUES(?);"
        self.SELECT_ALL_MEDIA = "SELECT m.title, f.format_name, m.shared_disc, m.run_time FROM media as m, formats as f WHERE f.format_id == m.format_id;"
        self.SELECT_ALL_FORMATS = "SELECT format_id, format_name FROM formats;"
        self.database = database
        self.media_list = []
        self.format_list = []
        self.__test_connection()

    def __test_connection(self):
        try:
            conn = sql.Connection(self.database)
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def insert_media(self, data: Media):
        try:
            conn = sql.Connection(self.database)
            conn.execute(self.INSERT_MEDIA_VALUE, data.media_to_tuple())
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        self.media_list = []

    def insert_format(self, data: Format):
        try:
            conn = sql.Connection(self.database)
            conn.execute(self.INSERT_FORMAT_VALUE, (data.name))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        self.format_list = []

    def get_media_list(self):
        if len(self.media_list) == 0:
            try:
                conn = sql.Connection(self.database)
                self.media_list = conn.execute(
                    self.SELECT_ALL_MEDIA).fetchall()
                conn.commit()
                conn.close()
            except Exception as e:
                print(e)
        return self.media_list

    def get_format_list(self):
        if len(self.format_list) == 0:
            try:
                conn = sql.Connection(self.database)
                self.format_list = conn.execute(
                    self.SELECT_ALL_FORMATS).fetchall()
                conn.commit()
                conn.close()
            except Exception as e:
                print(e)
        return self.format_list
