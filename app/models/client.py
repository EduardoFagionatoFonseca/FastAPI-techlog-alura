from pydantic import BaseModel

class Client(BaseModel):
  id_: int | None
  nome: str
  email: str
  phone: str