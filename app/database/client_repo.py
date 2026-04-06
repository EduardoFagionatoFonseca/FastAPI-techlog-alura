from app.database.local import LocalDatabase
from app.models.client import Client, CreateAndUpdateClient

class ClientRepo:
  def __init__(self, database: LocalDatabase):
    self.db = database

  async def list_clients(self) -> list[Client]:
    with self.db.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("""SELECT id, name, phone, email FROM clients""")
      lines = cursor.fetchall()
      clients = [
        Client(id=line[0], name=line[1],  email=line[3], phone=line[2]) for line in lines
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
       return Client(id=client[0], name=client[1], email=client[2], phone=client[3])
    return None
    
  async def create_client(self, client: CreateAndUpdateClient) -> Client:
    with self.db.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("INSERT INTO CLIENT (name, email, phone) VALUES (?,?,?)", (client.name, client.email, client.phone))
      client_id = cursor.lastrowid
      return Client(id=client_id, name=client.name, email=client.email, phone=client.phone)
