import sqlite3
from contextlib import contextmanager

class LocalDatabase():
  def __init__(self, file_name = 'techlog.db'):
    self.file_name = file_name

  @contextmanager
  def connect(self):
    conn = sqlite3.connect(self.file_name)
    try:
      yield conn
      conn.commit()
    except Exception as e:
      conn.rollback()
      raise e
    finally:
      conn.close()

  def init_db(self):
    with self.connect() as conn:
      cursor = conn.cursor()
      cursor.execute('''
      CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL
                     )
  ''')
      conn.commit()