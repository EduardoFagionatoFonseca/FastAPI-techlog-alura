from app.database.local import LocalDatabase
from app.models.client import Client

class ClientRepo:
  def __init__(self, database: LocalDatabase):
    self.db = database

  async def list_clients(self) -> list[Client]:
    with self.db.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("""SELECT id, name, phone, email FROM clients""")
      lines = cursor.fetchall()
      clients = [
        Client(id_=line[0], name=line[1],  email=line[3], phone=line[2]) for line in lines
        ]
      
      return clients
    
  async def get_client(self, client_id: int) -> Client | None:
    with self.db.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("""
    SELECT id, name, email, phone FROM clients WHERE id = ?
    """, (client_id,))
      client = cursor.fetchone()
      if client:
       return Client(id_=client[0], name=client[1], email=client[2], phone=client[3])
    return None
    