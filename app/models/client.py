from pydantic import BaseModel

class Client(BaseModel):
  id_: int | None
  name: str
  email: str
  phone: str