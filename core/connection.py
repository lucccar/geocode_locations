import sqlite3
import functools

from app.settings import DATABASES


class ConnectionDecorator(object):

    @staticmethod
    def open_conn(f):
        @functools.wraps(f)
        def decorated(self, *args, **kwargs):  
            self.open_connection()
            try:
                returned = f(self, *args, **kwargs)
                return returned
            except Exception as e:
                print(e)
                raise e
            finally:
                self.close_connection()

        return decorated


class BasicDAO(object):

    def __init__(self) -> None:
        super().__init__()
        self.conn = None

    def open_connection(self):
        if self.conn is None:
            print("Connecting to the database...")
            self.conn = sqlite3.connect(DATABASES["default"]["NAME"])
            print(DATABASES["default"]["NAME"])
            

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
